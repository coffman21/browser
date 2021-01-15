from tinydb.queries import Query
from player.data.track import Track
from tinydb import TinyDB

class ORM:
    def __init__(self, path):
        self.db = TinyDB(path)

    def addTrack(self, track: Track):
        trackTable = self.db.table('Track')
        trackTable.insert(track.dict())

    def addTracks(self, tracks: list):
        trackTable = self.db.table('Track')
        # trackTable.insert_multiple([t.dict() for t in tracks])
        for t in tracks:
            try:
                trackTable.insert(t.dict())
            except Exception as e:
                print(e)

    def getTracks(self):
        trackTable = self.db.table('Track')
        return trackTable.all()
        # return self.db.search(tQ.artist == 'Skrill')
        
