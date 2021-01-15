class TrackMeta():
    def __init__(self, name, artist, album, releaseDate, genre, rating=None, artists=[], links=[]):
        self.name = name
        self.artist = artist
        self.album = album
        self.releaseDate = releaseDate
        self.genre = genre
        self.rating = rating

        self.artists = artists
        self.links = links
        