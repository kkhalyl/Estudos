class Televisao:
    def __init__(self):
        self.marca = "LG"
        self.volume = 0

    def aumentarvolume(self):
        if self.volume<10:
            self.volume+=1

    def diminuirvolume(self):
        if self.volume>0:
            self.volume-=1

tv = Televisao()