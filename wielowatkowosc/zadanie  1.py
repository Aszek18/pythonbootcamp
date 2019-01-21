from threading import Thread
from time import time, sleep


from urllib.request import urlopen

class MyThread(Thread):
    def run(self):
        with urlopen("https://www.metaweather.com/api/location/search/?query=Warsaw") as file:
            print(file.read())

przed = time()

watki= []
for i in range(100):
    watek = MyThread()
    watek.start()
    watki.append(watek)

for watek in watki:
    watek.join()

po = time()

print(f"Czas: ({po-przed}s")