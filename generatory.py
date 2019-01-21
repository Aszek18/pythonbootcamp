Samogloski = "aeiou"

def generator(napis):
    for litera in napis:
        if litera in Samogloski:
            yield litera


for litera in generator("ala ma kota, a kot ma ale"):
    print(litera)
