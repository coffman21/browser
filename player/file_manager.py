import os
from player.data.track import Track

class FileManager:
    def __init__(self, basePath):
        self.basePath = basePath
    
    def walk(self):
        tracks = []
        for root, _, filenames in os.walk(self.basePath):
            for filename in filenames:
                tracks.append(Track(root, filename, "bass", 5))
        return tracks
