import inspect
from player.track_meta import TrackMeta

class Track:
    def __init__(self, path, meta: TrackMeta):
        self.path = path
        self.meta = meta
    
    @staticmethod
    def attributes():
        forAttrs = TrackMeta("", "", "", "", "")
        return list(forAttrs.__dict__.keys())
    
    def dict(self):
        return vars(self.meta)