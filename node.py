from blockchain import Blockchain
from uuid import uuid4
from verification import Verification


class Node:

    def __init__(self) -> None:
        #self.id = str(uuid4())
        self.id = 'Max'
        self.blockchain = Blockchain(self.id)

    def get_transaction_value(self):
        tx_recipient = input("Enter recipient: ")
        tx_amount = float(input("Your transaction amout please: "))
        return tx_recipient, tx_amount


    def get_user_choice(self):
        user_input = input("Your choice: ")
        return user_input

    def print_blockchain_elements(self):
        for block in self.blockchain.get_chain():
            print("Outputting Block")
            print(block)
        else:
            print('-' * 20)


    def listen_for_input(self):
        waitting_for_input = True
        while waitting_for_input:
            print("please choose")
            print("1: add a new transaction value")
            print("2: mine a block")
            print("3: output the blockchain blocks")
            print("4: check transaction validity")
            print("q: exit")
            user_choice = self.get_user_choice()
            if user_choice == '1':
                tx_data = self.get_transaction_value()
                recipient, amount = tx_data
                if self.blockchain.add_transaction(recipient=recipient, sender=self.id, amount=amount):
                    print("Add transaction success!")
                else:
                    print("Add transaction fail!")
                print('open_transaction = ', self.blockchain.get_open_transactions())
            elif user_choice == '2':
                self.blockchain.mine_block()
            elif user_choice == '3':
                self.print_blockchain_elements()
            elif user_choice == '4':
                if Verification.verify_transactions(self.blockchain.get_open_transactions(), self.blockchain.get_balance):
                    print("全部交易均合法")
                else:
                    print("存在非法交易")
            elif user_choice == 'q':
                waitting_for_input = False
            else:
                print("invalid input!")
            verifier = Verification()
            if not verifier.verify_chain(self.blockchain.get_chain()):
                self.print_blockchain_elements()
                print("invalid blockchain")
                break
            print("balance of {}: {:6.2f}".format(self.id, self.blockchain.get_balance()))
            print('---------------------------------------\n\n\n')
        else:
            print("User left")

node = Node()
node.listen_for_input()


