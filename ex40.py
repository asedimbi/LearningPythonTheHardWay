#classes and objects

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def singMeASong(self):
        for line in self.lyrics:
            print(line)
        

happy_bDay = Song(["Happy Birthday to you!", "I dont want to get sued","So I will stop right there"])

bulls_On_Parade = Song(["They rally around the family", "With pockets full of shells"])

happy_bDay.singMeASong()
bulls_On_Parade.singMeASong()