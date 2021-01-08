import inspect

class Track:
    def __init__(self, name, artist, genre, rating=None):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.rating = rating
    
    @staticmethod
    def attributes():
        forAttrs = Track("", "", "", 0)
        return list(forAttrs.__dict__.keys())