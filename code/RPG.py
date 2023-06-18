
#Shop conversation

village_choice_list = ['enter the shop', 'go to the town square', 'Duck!', 'go to the castle', 'go the well' ]
player_inventory_values = {
    "rusty sword": 2,
    "ragged tunic": 1,
    "rope": 3,
    "old boots": 0.5,
    "purse": 7,
}
shop_inventory_values = {
    "hat": 5,     #hat <4 ch, will not allign with other items
    "gloves": 3,
    "shoes": 7,  # use colons for dict, "", tab values
    "cape": 11,
    "boots": 10,
}  # dictionary to recall values
# use_snake_case


def purse_check(shop_item, item_values, purse_value):
    """check player can afford item
    a function to check whether the player has enough money in their purse to afford the selected item

    :param shop_item: selected item from item values
    :param item_values: value of all items
    :param purse_value: current value of purse
    """
    if item_values[shop_item] <= purse_value:
        print(
            f'you can afford the {shop_item}! the {shop_item} will cost {item_values[shop_item]} gold and you have {purse_value} gold in your purse')
    else:
        print(
            f"you can't afford the {shop_item}! the {shop_item} will cost {item_values[shop_item]} gold and you only have {purse_value} gold in your purse")

def show_shop_inventory(item_values):
    """list a shop inventory
    prints all items in a list on separate lines

    :param item_values: the selected list
    """
    print("Here's what's in stock")
    for item in item_values.keys():
        print(f'\t{item} = {item_values[item]} gold')

#def sell(sale_item_values, sale_purse_value):
    #show_shop_inventory(player_inventory_values)
    #sale = input('What would you like sell? ')
    #if sale in sale_item_values.keys():
        #print(f"a fine piece, I'll give you {sale_item_values[item]} gold for it")
        #player_inventory_values['purse'] += {sale_item_values[item]}
        #del sale_item_values.keys[item]

def buy(item_values, purse_value):
    """initial interaction for item selection

    :param item_values: selected list
    :param purse_value: value of selected purse
    """
    shop = input('Would you like to see my wares? ')
    if shop == 'yes':
        show_shop_inventory(item_values)
        next = input('What would you like to buy? ')
        if next in item_values.keys():
            purse_check(shop_item=next, item_values=item_values, purse_value=purse_value)
        else:
            print(f"I don't have any {next}s here sunshine!")
            buy(item_values=item_values,purse_value=purse_value)   #recursion
    if shop == 'no':
        qu_sell = input('Do you have anything to sell? ')
        if qu_sell == 'yes':
            print('cool')
            #sell(sale_item_values=player_inventory_values, sale_purse_value= player_inventory_values['purse'])
        elif qu_sell == 'no':
            print('Piss off then, I have other customers waiting!')


print('Greetings traveller!')
buy(item_values=shop_inventory_values, purse_value=player_inventory_values['purse'])
shop_qu1 =input('Anything else? ')
if shop_qu1 == 'yes':
    buy(item_values=shop_inventory_values, purse_value=player_inventory_values['purse'])
if shop_qu1 =='no':
    print("On your way then, I've got work to do")

print('//////////////////////////////////////////////////////////////////////////////////////////////////')



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


