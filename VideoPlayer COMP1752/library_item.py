class LibraryItem:
    def __init__(self, name, director, rating=0, play_count =0, url =None  ):
        self.name = name
        self.director = director
        self.rating = rating
        self.play_count = play_count
        self.url = url
#function
    def info(self):
        return f"{self.name} - {self.director} {self.stars()}"
    
    def stars(self):
        stars = ""
        for i in range(self.rating):
            stars += "*"
        return stars
  
    def update_rating(self, new_rating):
        self.rating = float(new_rating)

    def increment_play_count(self):
        self.play_count += 1