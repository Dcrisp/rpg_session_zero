
#Shop conversation
inventory = ['hat', 'gloves', 'shoes', 'cape', 'boots']
hatvalue = 5
glovesvalue = 3
shoesvalue = 7
capevalue = 11
bootsvalue = 10
Playerpurse = 6
Shop = input('Would you like to see my wares? ')
if Shop == 'yes':
    for item in inventory:
        print(item)
if Shop == 'no':
    print('Piss off then, I have other customers waiting!')

Next = input('What would you like to buy? ')
if Next == 'hat':
    print('That will be 5 gold')
elif Next == 'gloves':
    print('That will be 3 gold')
elif Next == 'shoes':
    print('That will be 7 gold')
elif Next == 'cape':
    print('That will be 11 gold')
elif Next == 'boots':
    print('That will be 10 gold')

Buy = input('Can you afford that? ')
if Buy == 'yes':
    print('You have ' + str(Playerpurse))
Check = input('Are you sure? ')
if Check == 'yes':
    print('Excellent, thank-you for your custom')
elif Check =='no':
    print('Out of my sight peasant!')


import random
c1ra = 'Craven!'
c1rb = "You peer into the gloom, there isn't much to see initially but then you see a small chest"
c1rc = "You whistle a familiar tune, it's nice but it doesn't achieve much"
c1rd = "Ach ya wee scamp!"
GO = 'Game over!'
Treasurelist = ["Strange ring", "Dagger", "Rusted sword", "Precious gem", "Mysterious note"]
chestroll = random.randrange(0,4)
Item = Treasurelist[int(chestroll)]
txtc = "You open the chest and find a {}"

print('You enter a small room dimly lit by a lantern')
choicelist1 = ['turn back', 'look around', 'whistle a tune', 'take the lantern']
for item in choicelist1:
    print(item)
print("/////////////////////////////////////////////////////////////////////////////////////")
choice1 = input('What do you do? ')
if choice1 == 'turn back':
    print(c1ra)
    print(GO)
elif choice1 == 'look around':
    print(c1rb)
    c1rb1 = input('Will you open the chest?  ')
    if c1rb1 == 'yes':
        print(txtc.format(Item))
    if c1rb1 == 'no':
        print('Rude')
elif choice1 == 'whistle a tune':
    print(c1rc)
    print(GO)
elif choice1 == 'take the lantern':
    print(c1rd)

print("/////////////////////////////////////////////////////////////////////////////////////")


