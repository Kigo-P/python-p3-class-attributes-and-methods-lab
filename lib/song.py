class Song:
    # creating a class attribute called count which is set at 0
    count = 0
    # creating a class attribute called genres which is set an empty list
    genres = []
    # creating a class attribute called artists which is set an empty list
    artists = []
    # creating a class attribute called genre_count which is set to an empty dictionary
    genre_count = {}
    # creating a class attribute called artist_count which is set to an empty dictionary
    artist_count = {}

    #initialization
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        # calling the class method  that increaments the value by 1
        Song.add_song_to_count()
        Song.add_to_genres(self.genre)
        Song.add_to_artists(self.artist)
        Song.add_to_genre_count(self.genre)
        Song.add_to_artist_count(self.artist)

    # class method for adding a new song to the count 
    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment
    
    # class method for genre that adds a new genre to the list
    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
        return [genre for genre in cls.genres]
    
    # class method for artists that adds a new artists to the list
    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    # class method for genre that adds a genre count
    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    # class method for artist that adds a artist count
    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] +=1
        else:
            cls.artist_count[artist] =1
        pass

        

        

# ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
# print(ninety_nine_problems.name)
# print(ninety_nine_problems.artist)
# print(ninety_nine_problems.genre)
# print(Song.count)
# print(ninety_nine_problems.add_to_genres("Rap"))
# print(ninety_nine_problems.add_to_genres("rock"))
# print(ninety_nine_problems.genre_count())





