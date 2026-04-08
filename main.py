import json
import random
import string
from pathlib import Path


class Bank:

    data=[] #creating a list of dummy data to store the details of the account
    database='data.json'

    try:
        if Path(database).is_file(): #checking if the json file exists or not
            
            with open(database,'r') as file: #opening the json file in read mode
                data=json.load(file) #loading the data from the json file and storing it in the data variable
    except Exception as err:
        print(f"Error occurred: {err}")

    @classmethod
    def update(cls):   #THIS FUNCTION IS USED TO UPDATE THE DATA IN THE JSON FILE
        try:
            with open(cls.database,'w') as fs:#opening the json file in write mode
                fs.write(json.dumps(cls.data)) #dumping the data into the json file
        except Exception as err:
            print(f"Error occurred: {err}")

    @staticmethod
    def __accountgenerate(): #THIS FUNCTION IS USED TO GENERATE A RANDOM ACCOUNT NUMBER
        aplha=random.choices(string.ascii_uppercase,k=2) #generating 2 random uppercase letters
        num=random.choices(string.digits,k=4) #generating 4 random digits
        spchar=random.choices("!@#$%^&*()_+",k=2) #generating 2 random special characters
        id=aplha+num+spchar #combining the random letters, digits and special characters to form the account number
        random.shuffle(id) #shuffling the account number to make it more random 

        return "".join(id) #joining the list of characters to form a string and returning it
    def create_account(self):
        info= {
            "name": input("enter your name: "),
            "age": int(input("enter your age: ")),
            "email": input("enter your email: "),
            "pin": int(input("enter your pin: ")),
            "account_number": Bank.__accountgenerate(), #generating a random account number using the __accountgenerate function
            "balance": 0
        }
        if info["age"] < 18 or len(str(info["pin"])) != 4:
            print("you are not eligible to create an account")

        else:
            print("account created successfully")
            for i in info:
                print(f"{i}: {info[i]}")
            print("please remember your account number and pin for future use")    

            Bank.data.append(info) #appending the data to the data list

            Bank.update()

    def deposit_money(self):
        account_number=input("enter your account number: ")
        pin=int(input("enter your pin: "))
        amount=int(input("enter the amount you want to deposit: "))

        for i in Bank.data:
            if i["account_number"] == account_number and i["pin"] == pin:
                i["balance"] += amount
                print(f"your new balance is: {i['balance']}")
                Bank.update()
                break
        else:
            print("invalid account number or pin")

print("press 1 for creating an account")                  #{first step
print("press 2 for deposit money in the bank")            #      |
print("press 3 for withdraw money from the bank")         #      |
print("press 4 for details of the account")               #      |
print("press 5 for updating the details of the account")  #      |
print("press 6 for deleting the account")                 #      |
print("press 7 for exit")                                 #      }


user=Bank()
check=int(input("enter your choice: "))              #SECOND STEP
if check==1:
    user.create_account()
elif check==2:
    user.deposit_money() 
