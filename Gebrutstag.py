import datetime
import math
import time
from datetime import date

print("--------------------------------------------------")
print("                   GEBURTSTAG                     ")
print("--------------------------------------------------")

print("Wann wurdest du geboren?")
Jahr = int(input("In welchem Jahr [JJJJ]:"))
Monat = int(input("In welchem Montat [MM]:"))
Tag = int(input("An welchem Tag [TT]:"))

Date1 = datetime.date(Jahr, Monat, Tag)
Date2 = datetime.date.today()
delta = Date2 - Date1
Today = date.today()
Today == date.fromtimestamp(time.time())

Bday = date(Today.year, Monat, Tag)

if Bday < Today:
    Bday = Bday.replace(year=Today.year + 1)
    Dleft = abs(Bday - Today)
    print("Dein Geburtstag ist erst nächstes Jahr und in " + str(Dleft.days) + " Tagen.")
elif Bday > Today:
    Dleft = abs(Bday - Today)
    print("dein Geburtstag ist dieses Jahr und in " + str(Dleft.days) + " Tagen.")
else:
    print("Du hast Heute Gebrutstag.")

Age = delta.days / 365
print("Du bist " + str(math.floor(Age)) + " Jahre und am " + str(Tag) + "." + str(Monat) + "." + str(Jahr) + " geboren.")