# python cmd prompt login using deta
from deta import Deta

 # make sure to replace this with your project key
deta = Deta("projectkeyhere")

# name this to whatever you want your database to be
db = deta.Base("LoginDB") 
        
choice = input("Hello! Welcome to the login screen.\n 1: Register\n 2: Existing Account\n\n")

if choice == "1":
    username = input('Enter a username: ')
    password = input('Enter a password: ')
    
    verify = input(f'Is this correct: user: {username}  pass: {password} [Y] or [N]: ')
    
    if verify == "Y":
        try:
            if not db.get(username):
                db.put({"key":f"{username}","pass":f"{password}"})
                print('Successfully made account!')
            else:
                print('You already have a account!')
        except:
            print('error ocurred trying to make account!')
    elif verify == "N":
        print("Account Deleted!")
elif choice == "2":
    username = input("Please Enter Your Username: ")
    
    if not db.get(username):
        print('username is incorrect or not found, please retry again')
    else:
        mydb = db.get(username)
        print('Valid User!')
        password = input('Enter your Password: ')
        try:
            if mydb and mydb['pass'] == password:
                print('Successfully Logged in!')
            else:
                print('Wrong password, retry again!')
        except:
            print('Error ocurred')
        
