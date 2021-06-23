###
### Author: Navneeth Mohan Kunkatla
###

import webbrowser
def get_content():
    info = open (input('Enter info file name:'), 'r').readlines()
    inventory = {}
    for line in info:
        line_broken = line.split()
        inventory[line_broken[0]] = (line_broken[1], line_broken[2])
    return inventory

def print_inventory(inventory):
    print('These are items in inventory:')
    for key in inventory:
        print(key + ' - $'+inventory[key][0])

def print_belongings(curr_money, bought_items):
    print('You have $'+ str(curr_money) + ' in your wallet.')
    if bought_items == {}:
        print('No items have been purchased.')
    else:
        print('You have purchased these items:')
        for key in bought_items:
            print(key + ' - '+ str(bought_items[key]))


def add_to_wallet(curr_money, money):
    if curr_money + int(money) > 10000:
        print('Wallet can not exceed $10000. Current wallet $' + str(curr_money))
        return 0
    else:
        curr_money += int(money)
        print('$' + str(money) +' has been added.')
        return int(money)

def buy_item(money, inventory, bought_items, buying):
    if buying not in inventory:
        print('Item does not exist.')
        return 0
    elif money< int(inventory[buying][0]):
        print("Sorry, you don't have enough money in your wallet.")
        return 0
    else:
        if buying not in bought_items:
            bought_items[buying] = 0
        bought_items[buying] += 1
        return int(inventory[buying][0])


def return_item(inventory, bought_items, returning):
    if returning not in bought_items:
        print('Item has not been bought')
        return 0
    else:
        value = int(inventory[returning][0])
        if bought_items[returning] > 1:
            bought_items[returning] = bought_items[returning] -1
        else:
            del bought_items[returning]
            print('Item has been returned.')
            return value


def view_item_on_web(inventory, item_name):
    url_str = 'https://www.amazon.com/dp/' + inventory[item_name][1]
    webbrowser.open(url_str)

def main():

    # The inventory should be a dictionary mapping product name (string) to tuples.
    # The tuples will be of length two - the first element being the item's price (int)
    # and the second being the item's Amazon ID.
    inventory = get_content()


    # Keeps track of items bought by user.
    # Key is the item name and value is the number of those items that have been bought.
    belongings = {}

    print("\n------ Welcome to Amayzeon! ------")
    balance = 100

    while True:
        user_input = input("What would you like to do?\n")
        if user_input.startswith('buy'):
            value = buy_item(balance, inventory, belongings, user_input.split()[1])
            balance = balance - value
            if value > 0:
                print('Item bought.')

        elif user_input.startswith('return'):
            balance += return_item(inventory, belongings, user_input.split()[1])
        elif user_input.startswith('add'):
            balance += add_to_wallet(balance, user_input.split()[1])
        elif user_input.startswith('view'):
            view_item_on_web(inventory, user_input.split()[1])
        elif user_input == 'belongings':
            print_belongings(balance, belongings)
        elif user_input == 'inventory':
            print_inventory(inventory)
        elif user_input == 'exit':
            return
        else:
            print("Huh?")


main()