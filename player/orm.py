from tinydb.queries import Query
from player.data.track import Track
from tinydb import TinyDB

class ORM:
    def __init__(self, path):
        self.db = TinyDB(path)

    def addTrack(self, track: Track):
        trackTable = self.db.table('Track')
        trackTable.insert(vars(track))

    def addTracks(self, tracks: list):
        trackTable = self.db.table('Track')
        trackTable.insert_multiple([vars(t) for t in tracks])

    def getTracks(self):
        trackTable = self.db.table('Track')
        return trackTable.all()
        # return self.db.search(tQ.artist == 'Skrill')
        
