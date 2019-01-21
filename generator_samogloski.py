
class Vowels:
    def __init__(self,napis):
        self.napis = napis


    def __iter__(self):
        self.pozycja=0
        return self

    def __next__(self):
        while self.pozycja < len(self.napis):
            litera = self.napis[self.pozycja]
            self.pozycja +=1
            if litera in "aeiou":
                return litera
        raise StopIteration



for char in Vowels("alde xdlaae"):
    print(char)