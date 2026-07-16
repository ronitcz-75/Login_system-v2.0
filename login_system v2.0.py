import random as r

# SECURTIY SCANNER

# *************************WELLCOME USER **********************************
 
Operation=input("Login or Sign up : ")

#login page 
def login():
    login=input("Enter Name: ")
    if login=="admin123":
        print("Valid admin")
    else:
       print("wrong admin!!")
    password=input("Password: ")
    if password=="hey":
      print("Access Granted")
      print("Wellcome back....")
    else:
      print("Not granted!!")
# sign up page 
def sign_up():
    sign=input("Create name: ")
    if len(sign)>3:
        print("Welcome",sign)
    else:
        print("Please keep letter above 3")
    password1=int(input("Create password: "))
    if password1>6:
        print("welcome",sign)
    else:
        print("Password is too short")
if Operation=="login":
    print(login())
elif  Operation=="sign up":
    print(sign_up())
else:
    print("Atleast choose one option!!!")

# SECURITY PIN CREATION 
Enter=input("Are you want to Create security pin: ")

def pin_create():
    real=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",1,2,3,4,5,6,7,8,9,0,"₹","_","&",":",";","!","?"]
    for i in real:
        print(r.choice(real))

if Enter=="yes":
    print(pin_create())
else:
    print("Thank you and welcome back")