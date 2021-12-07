import json, socket

def pre_send(IP, PORT, ID_LENGTH):
    acceptable = False
    receiver = input('Enter receiver or number, or "_" to go back: ')
    if receiver == '_':
        return
    while not acceptable:
        try:
            int(receiver)
            if len(receiver) == ID_LENGTH:
                acceptable = True
            else:
                print(f'Entered a wrong number. A number must be {ID_LENGTH} characters long')
                receiver = input('Enter receiver or number, or "_" to go back: ')
                if receiver == '_':
                    return
        except ValueError:
            index = json.load(open('./Client/contacts.json'))
            for i in index:
                print(i)
                if i == receiver:
                    acceptable = True
                    num = index[i]
            if acceptable == False:
                print(f'No contacts named {receiver} has been saved on this device.')
                receiver = input('Please enter a number, or "_" to go back: ')
                if receiver == '_':
                    return
    
    msg = input('Enter the message:\n\n')

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto((msg, num), (IP, PORT))