

class Iterator:
    def __init__(self,limit):
        self.limit = limit

    def __iter__(self):
        self.licznik=0
        return self
    def __next__(self):
        if self.licznik > self.limit:
            raise StopIteration
        liczba = self.licznik
        self.licznik +=1
        return liczba

limit = int(input(f"Limit:"))
for i in Iterator(limit):
    print(i)

