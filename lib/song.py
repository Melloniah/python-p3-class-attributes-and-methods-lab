class Song:
    # Class attributes to track overall song data
    count = 0                          # Total number of songs created
    genres = []                        # List of unique genres
    artists = []                       # List of unique artists
    genre_count = {}                  # Dictionary to count songs per genre
    artist_count = {}                 # Dictionary to count songs per artist

    def __init__(self, name, artist, genre):
        # Instance attributes
        self.name = name              # Song name
        self.artist = artist          # Song artist
        self.genre = genre            # Song genre

        # Update class-level statistics
        self.__class__.add_song_to_count()        # Increment song count
        self.__class__.add_to_genres(genre)       # Add genre to list if new
        self.__class__.add_to_artists(artist)     # Add artist to list if new
        self.__class__.add_to_genre_count(genre)  # Count how many songs in each genre
        self.__class__.add_to_artist_count(artist)  # Count how many songs per artist

    @classmethod
    def add_song_to_count(cls):
        # Increments the total number of songs created
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        # Adds a genre to the genres list if it's not already present
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        # Adds an artist to the artists list if it's not already present
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        # Updates the genre_count dictionary: adds 1 if genre exists, or creates key
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        # Updates the artist_count dictionary: adds 1 if artist exists, or creates key
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
