import random
print("--------------------------------------------------")
print("                ABI ORAKEL                        ")
print("--------------------------------------------------")
print("Bremer Abiturienten können maximal 900 Punkte im Abitur erreichen. Sie brauchen mindestens 300 um zu bestehen.")
guess = int(input("Wie viele Punkte wirst du im Abi erreichen?"))
points = random.randint(0, 900)

while guess != points:
    if guess > points:
        print("Nein, du wirst WENIGER als " + str(guess) + " Punkte erreichen!")
        guess = int(input("Wie viele genau?"))
    else:
        print("Nein, du wirst MEHR als " + str(guess) + " Punkte erreichen!")
        guess = int(input("Wie viele genau?"))
else:
    if guess == 0:
        print('RICHTIG! Du wirst genau keinen Punkt erreichen')
    else:
        print('RICHTIG! Du wirst genau ' + str(guess) + ' Punkte erreichen.')
