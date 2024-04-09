blockchain = []

def get_last_block_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])

def get_transaction_value():
    user_input = float(input("Your transaction amout please: "))
    return user_input



tx_amount  = get_transaction_value()
add_value(tx_amount)

def get_user_choice():
    user_input = input("Your choice: ")
    return user_input

def print_blockchain_elements():
    for block in blockchain:
        print("Outputting Block")
        print(block)

while True:
    print("please choose")
    print("1: add a new transaction value")
    print("2: output the blockchain blocks")
    print("q: exit")
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_block_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'q':
        break
    else:
        print("invalid input!")



print("Done!")