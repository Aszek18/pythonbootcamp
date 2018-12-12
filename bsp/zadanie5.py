import re

kod_pocztowy = re.compile("\d{2}-\d{3}")
email = re.compile("[\w]+@[\w+]+[.]+[a-z]+")
test_db= re.compile("[0-3]*[0-9]\s[A-Z][a-z]{2}\s[1-9][0-9]{2,3}")

kod_pocztowy1 = kod_pocztowy.findall("n02-681stdflf02-681lftek12stekstfkfkkfkdjslf")
email1 = email.findall("n02asd@wp.pl, askdj2345@ksks.ol,02-681lftek12stekstfkfkkfkdjslf")
test_db1 = test_db.findall("21 Maj 1990, askdj2345@ksks.ol,02-681lftek12stekstfkfkkfkdjslf")


print(kod_pocztowy1)
print(email1)
print(test_db1)


# with open("dane.txt") as file:
#     tekst = file.read()

