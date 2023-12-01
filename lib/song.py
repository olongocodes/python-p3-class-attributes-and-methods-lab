class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    


    def __init__(self, name, artist, genre):
        self.name = name 
        self.artist = artist
        self.genre = genre
        Song.count += 1
        # Call the class methods to add the genre and artist to their respective lists
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    @classmethod
    def add_to_genres(cls, new_genre):
        # Add the new genre to the genre list if it's not already present
        if new_genre not in cls.genres:
            cls.genres.append(new_genre)

    @classmethod
    def add_to_artists(cls, new_artist):
        # Add the new artist to the artist list if it's not already present
        if new_artist not in cls.artists:
            cls.artists.append(new_artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        #Update the genre count dictionary
        if genre in cls.genre_count:
            # Increment the count if the genre already exists in the dictionary
            cls.genre_count[genre] += 1
        else:
            # Create a new key/value pair if the genre is not in the dictionary
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        #Update the artist count dictionary
        if artist in cls.artist_count:
            # Increment the count if the artist already exists in the dictionary
            cls.artist_count[artist] += 1
        else:
            # Create a new key/value pair if the artist is not in the dictionary
            cls.artist_count[artist] = 1

    





# Example usage:
# song1 = Song("Song 1", "Artist 1", "Rap")
# song2 = Song("Song 2", "Artist 2", "Rock")
# song3 = Song("Song 3", "Artist 1", "Rap")
# song4 = Song("Song 4", "Artist 3", "Country")
# song5 = Song("Song 5", "Artist 2", "Rap")
# song6 = Song("Song 6", "Artist 3", "Country")
# song7 = Song("Song 7", "Artist 7", "Rhumba")

# Display the unique genres, artists, genre count, and artist count
# print(Song.genres)
# print(Song.artists)
# print(Song.genre_count)
# print(Song.artist_count)