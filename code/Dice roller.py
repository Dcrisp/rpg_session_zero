import random

def D20roll():
    Roll = random.randrange(1, 20)
    txt = "Roll the dice, you rolled a {}"
    print(txt.format(Roll))
    if Roll == 20:
        print('Nat 20!')
    elif Roll == 1:
        print('Critical failure!')
    elif Roll > 10:
        print('Success!')
    elif Roll < 10:
        print('Failure!')

D20roll()

