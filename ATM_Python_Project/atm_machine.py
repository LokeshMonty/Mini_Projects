import getpass

# User data
users = ['user', 'user2', 'user3']
pins = ['1234', '2222', '3333']
amounts = [1000, 2000, 3000]

# User login
count = 0
while True:
    user = input('\nENTER USER NAME: ').lower()
    if user in users:
        n = users.index(user)
        break
    else:
        print('INVALID USERNAME\n')

# PIN validation
while count < 3:
    pin = getpass.getpass('PLEASE ENTER PIN: ')
    if pin.isdigit() and pin == pins[n]:
        break
    else:
        print('INVALID PIN\n')
        count += 1
if count == 3:
    print('3 UNSUCCESSFUL PIN ATTEMPTS, EXITING')
    print('!!!!!YOUR CARD HAS BEEN LOCKED!!!!!')
    exit()

print('\nLOGIN SUCCESSFUL, CONTINUE')
print(f"\n{users[n].capitalize()}, welcome to ATM")
print('----------ATM SYSTEM-----------')

# ATM menu
while True:
    print()
    response = input('SELECT FROM FOLLOWING OPTIONS:\nStatement__(S) \nWithdraw___(W) \nAdd Balance__(L)  \nChange PIN_(P)  \nQuit_______(Q) \n: ').lower()
    if response == 's':
        print(f"{users[n].capitalize()}, YOU HAVE {amounts[n]} MONEY IN YOUR ACCOUNT.")
    elif response == 'w':
        try:
            cash_out = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))
            if cash_out % 10 != 0:
                print('AMOUNT MUST BE IN MULTIPLES OF 10')
            elif cash_out > amounts[n]:
                print('YOU HAVE INSUFFICIENT BALANCE')
            else:
                amounts[n] -= cash_out
                print('YOUR NEW BALANCE IS:', amounts[n])
        except ValueError:
            print('ENTER A VALID AMOUNT')
    elif response == 'l':
        try:
            cash_in = int(input('ENTER AMOUNT YOU WANT TO ADD: '))
            if cash_in % 10 != 0:
                print('AMOUNT MUST BE IN MULTIPLES OF 10')
            else:
                amounts[n] += cash_in
                print('YOUR NEW BALANCE IS:', amounts[n])
        except ValueError:
            print('ENTER A VALID AMOUNT')
    elif response == 'p':
        new_pin = getpass.getpass('ENTER A NEW PIN: ')
        if new_pin.isdigit() and new_pin != pins[n] and len(new_pin) == 4:
            new_ppin = getpass.getpass('CONFIRM NEW PIN: ')
            if new_ppin == new_pin:
                pins[n] = new_pin
                print('NEW PIN SAVED')
            else:
                print('PIN MISMATCH')
        else:
            print('NEW PIN MUST BE 4 DIGITS AND DIFFERENT FROM PREVIOUS')
    elif response == 'q':
        print('THANK YOU FOR USING ATM. GOODBYE!')
        break
    else:
        print('RESPONSE NOT VALID')