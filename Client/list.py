import json

class List:
    def __init__(self):
        self.index = json.load(open('./Client/contacts.json'))

    def contacts(self):
        print('\n\nWelcome in your index. Here you can find all of your contacts, and save others')
        print('Please select an action:\n')
        print('1) Get the list of contacts with their numbers')
        print('2) Save a new contact')
        print('3) Eliminate an existing contact')
        print('0) Exit\n')

        while True:
            a = input(']>[Index]> ')
            if a == '1':
                self.displayIndex()
            elif a == '2':
                self.appendToIndex()
            elif a == '3':
                self.killIndexContact()
            elif a == '0':
                return
            else:
                print('Enter a number from 0 to 2')

    def displayIndex(self):
        print(' ___________________________________________ ')
        for i in self.index:
            spaces = ' ' * (30 - len(i))
            print('|' + i + spaces + '| ' + str(self.index[i]) + ' |')
            if i != list(self.index.keys())[-1]:
                print('|———————————————————————————————————————————|')
        print(' ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞')

    def appendToIndex(self):
        numIsOk = False
        num = input('Enter the contact\'s number, or "_" to go back: ')
        if num == '_':
            return

        if len(num) != 10:
            numIsOk = False

        while not numIsOk:
            if len(num) != 10:
                print('The number must be 10 characters long')
                num = input('Enter the contact\'s number, or "_" to go back: ')
                if num == '_':
                    return
            else:
                try:
                    num = int(num)
                    numIsOk = True
                except ValueError:
                    print('Only number are allowed')
                    num = input('Enter the contact\'s number, or "_" to go back: ')
                    if num == '_':
                        return
            
        
        name = input('Enter the contact\'s name, or "_" to go back: ')
        if name == '_':
            return

        i = 0
        while i < len(self.index):
            print(i)
            while len(name) >= 30 or len(name) < 3:
                print('The name length must be beetween 3 and 30 characters')
                name = input('Enter the contact\'s name, or "_" to go back: ')
                if name == '_':
                    return
            if name == list(self.index.keys())[i]:
                print(f'You have already saved a contact with this name. His number is {self.index[list(self.index.keys())[i]]}')
                name = input('Enter the contact\'s name, or "_" to go back: ')
                if name == '_':
                    return
                i = 0
            else:
                i += 1
        self.index[name] = num
        with open('./Client/contac.json', 'w') as f:
            json.dump(self.index, f, indent=4)

    def killIndexContact(self):
        c = True
        name = input('Enter the name of the contact you want to remove, or "_" to go back: ')
        if name == '_':
            return
        
        del self.index[name]
        with open('./Client/contacts.json', 'w') as f:
            json.dump(self.index, f, indent=4)

        print(f'Every {name} has been removed from your contact list')