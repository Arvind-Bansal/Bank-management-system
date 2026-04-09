import json
import random
import string
from pathlib import Path


class Bank:

    data=[] #creating a list of dummy data to store the details of the account
    database='data.json'

    def __init__(self):
        # Load data from file when Bank object is created
        try:
            if Path(self.database).is_file():
                with open(self.database,'r') as file:
                    loaded_data = json.load(file)
                    if loaded_data and not Bank.data:  # Only load if Bank.data is still empty
                        Bank.data = loaded_data
                        print(f"DEBUG: Loaded {len(Bank.data)} accounts from data.json")
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

        print(f"DEBUG: Bank.data = {Bank.data}")  # Show what accounts exist
        print(f"DEBUG: Looking for account_number='{account_number}', pin={pin}")
        
        userdata=[i for i in Bank.data if str(i["account_number"]) == account_number and i["pin"] == pin]
        
        print(f"DEBUG: Found {len(userdata)} matching accounts")  # Show if match was found
        
        if not userdata:
            print("invalid account number or pin")
        else:
            if amount<=0 or amount>200000:
                print("invalid amount")
            
            else:
                userdata[0]['balance']+=amount #adding the amount to the balance
                Bank.update() #updating the json file with the new balance
                print("amount deposited successfully")




    def withdraw_money(self):
        account_number=input("enter your account number: ")
        pin=int(input("enter your pin: "))
        amount=int(input("enter the amount you want to withdraw: "))

        userdata=[i for i in Bank.data if str(i["account_number"]) == account_number and i["pin"] == pin] #checking if the account number and pin matches with the data in the json file
        
        if not userdata:
            print("invalid account number or pin")
        else:
            if userdata[0]['balance']<amount:
                print("invalid amount")
            
            else:
                userdata[0]['balance']-=amount #subtracting the amount from the balance
                Bank.update() #updating the json file with the new balance
                print("amount withdrawn successfully")





    def show_details(self):
        account_number=input("enter your account number: ")
        pin=int(input("enter your pin: "))

        userdata=[i for i in Bank.data if str(i["account_number"]) == account_number and i["pin"] == pin] #checking if the account number and pin matches with the data in the json file
        
        if not userdata:
            print("invalid account number or pin")
        else:
            for i in userdata[0]:
                print(f"{i}: {userdata[0][i]}") #printing the details of the account



    def update_details(self):
        account_number=input("enter your account number: ")
        pin=int(input("enter your pin: "))

        userdata=[i for i in Bank.data if str(i["account_number"]) == account_number and i["pin"] == pin] #checking if the account number and pin matches with the data in the json file
        
        if not userdata:
            print("invalid account number or pin")
        else:
           print("you can't change the age,account number and balance of the account")
           
           print("fill the details for the fields you want to update and leave the rest blank")

           newdata={
            "name": input("enter your name: ") or userdata[0]['name'], #if the user leaves the input blank, it will keep the old value
            "email": input("enter your email: ") or userdata[0]['email'], #if the user leaves the input blank, it will keep the old value
            "pin": int(input("enter your pin: ") or userdata[0]['pin']), #if the user leaves the input blank, it will keep the old value
            "age": userdata[0]['age'], #keeping the age same as the old value
            "account_number": userdata[0]['account_number'], #keeping the account number same as
            "balance": userdata[0]['balance'] #keeping the balance same as the old value
           }


           if type(newdata['pin'])==str:
                newdata['pin']=int(newdata['pin']) #converting the pin to integer if the user enters a string


           for i in newdata:
            if newdata[i] == userdata[0][i]:
                continue
            else:
                userdata[0][i]=newdata[i] #updating the details of the account
            
            
            Bank.update() #updating the json file with the new details
            print(f"{i} updated successfully")






    def delete_account(self):
        account_number=input("enter your account number: ")
        pin=int(input("enter your pin: "))

        userdata=[i for i in Bank.data if str(i["account_number"]) == account_number and i["pin"] == pin] #checking if the account number and pin matches with the data in the json file
        
        if not userdata:
            print("invalid account number or pin")
        else:
            check=input("are you sure you want to delete your account? (y/n): ")
            if check=='n' or check=='N':
                print("account deletion cancelled")
            else:
                Bank.data.remove(userdata[0]) #removing the account from the data list
                Bank.update() #updating the json file after deleting the account
                print("account deleted successfully")





        
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

elif check==3:
    user.withdraw_money()

elif check==4:
    user.show_details()

elif check==5:
    user.update_details()

elif check==6:
    user.delete_account()