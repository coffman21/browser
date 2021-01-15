import os

from eyed3.core import Date
from player.track_meta import TrackMeta
from player.data.track import Track
import eyed3
import mimetypes

class FileManager:
    def __init__(self, basePath):
        self.basePath = basePath
    
    def walk(self):
        tracks = []
        for root, _, filenames in os.walk(self.basePath):
            for filename in filenames:
                pathToFile = root + "/" + filename
                if mimetypes.guess_type(pathToFile)[0] == 'audio/mpeg':
                    try:
                        mp3 = eyed3.load(pathToFile)
                        tagsFromMp3 = TrackMeta(
                            mp3.tag.title,
                            mp3.tag.artist,
                            mp3.tag.album,
                            str(mp3.tag.getBestDate()) if mp3.tag.best_release_date else None,
                            mp3.tag.genre.name if mp3.tag.genre else None,
                            None, # eyed3.id3.frames.PopularityFrame.rating ?
                            )
                        tracks.append(Track(pathToFile, tagsFromMp3))
                    except Exception as e:
                        print("error while reading file {} {}".format(pathToFile, e))
        return tracks
