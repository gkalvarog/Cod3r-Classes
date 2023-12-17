# Blind Auction Program
import os

def clear_screen():
    os.system('clear')

def open_script():
    global book_of_bids
    book_of_bids = {}

    global wanna_bid
    wanna_bid = True

def ask_bid():
    global name, bid, id

    name = input("What is your name?\n").capitalize()
    bid = int(input('What is your bid?\n'))
    id = input('What is your ID number?\n')

def close_script():
    global wanna_bid
    wanna_bid = False

    clear_screen()

def add_to_book(id, name, bid):
    book_of_bids[id] = {'name': name, 'bid': bid}

    global bids
    bids = []

    bids.append(bid)

def someone_else():
    return input('Is there someone else to bet?\n').lower()[0]

def check_higher_bidder():
    higher_bid = max(bids)

    message = ''

    for k, v in book_of_bids.items():
        if v['bid'] == higher_bid:
            message =  f"{v['name'].capitalize()} wins the auction with a bid of ${higher_bid}."
        
    return message

open_script()

while wanna_bid:
    ask_bid()

    while id in book_of_bids:
        clear_screen()
        print('You have already placed your bid. Let another person participate.')
        ask_bid()

    add_to_book(id, name, bid)
    clear_screen()
    print(f"Current bid: {book_of_bids[id]['bid']}")

    is_someone_else = someone_else()

    clear_screen()

    if is_someone_else == 'n':
        close_script()
        print(check_higher_bidder())
    elif is_someone_else != 'n' and is_someone_else != 'y':
        close_script()
        print("I do not understand what you say. Refresh the page, and next time, write ONLY 'Yes' or 'No'.")
    

        
        
        
    

