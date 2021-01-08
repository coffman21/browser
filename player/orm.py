from tinydb.queries import Query
from player.data.track import Track
from tinydb import TinyDB

class ORM:
    def __init__(self, path):
        self.db = TinyDB(path)


    def addTrack(self, track: Track):
        self.db.insert(vars(track))

    def getTracks(self):
        tQ = Query()
        return self.db.search(tQ.artist == 'Skrill')
        
