#!/usr/bin/env python3.7
from credentials import Credentials
from user import User
import random

def create_credentials(fname,lname,user_name,password,email):
    '''
    Function to create new credentials
    '''
    new_credentials = Credentials(fname,lname,user_name,password,email)
    return new_credentials
def create_user(user_name,email,password):
    '''
    Function that creates new user
    '''
    new_user = User(user_name, email, password)
    return new_user
        

def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()  

def save_user(user):
    '''
    saves user details
    '''
    user.save_user_details()

def del_credentials(credentials):
    '''
    Function to delete credentials
    '''
    credentials.delete_credentials()

def find_credentials(email):
    '''
    Function that finds credentials by email and returns the credentials
    '''
    return Credentials.find_by_email(email)

def checking_existing_credentials(email):
    '''
    Function that check if credentials exists with that email and return a Boolean
    '''
    return Credentials.credentials_exist(email)

def display_credentials():
    '''
    Function that returns all saved credentials
    '''
    return Credentials.display_credentials()

def display_user():
    '''
    this class has power to display users
    '''
    return User.display_users()    

def main():
    print("Hello welcome to your credentials list. what is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like?")
    print('\n') 

    while True:
        print("Use thes short codes : cc - create a new_user account with a user_defined password, dc - display credential and user, can -create a new_user account with" 
              "auto-generated password, ex -exit ")  
        short_code = input().lower()

        if short_code == "cc":
            print("user_name")
            print("-" * 10)
            print("What account would like to create credentials for?")
            site = input()
            print("->->->")
                            
            print("First name ....")
            fname = input()

            print("Last name ...")
            lname = input()

            print("Enter username ...")
            user_name = input()

            print("Email Address ...")
            email = input()

            print("Enter a password")
            password = input()

            save_user(create_user(user_name, email, password))
            save_credentials(create_credentials(fname, lname, user_name, password, email))
            print("\n")
            print(f"A new {site} account by {fname} has successfully been created")
            print(f"The username is {user_name} and the password is {password} ")
            print("\n")

        elif short_code == "dc":
            if display_credentials():
               print("Here is a list of all your user credentials accounts")
               print("/n")

               for credentials in display_credentials():
                   print(f"{credentials.first_name} {credentials.last_name} {credentials.user_name} has credentials for this {site}")
               print("\n")
            else:
                print("\n")
                print("It looks like no account credentials exist at the moment. Consider creating one or more ")
                print("\n")

        elif short_code == "can":
            print("New user")
            print("-" * 10)
            print("Which account would you like to create?")
            site = input()
            print("->->->")

            print("First name ....")
            fname = input()

            print("Last name ...")
            lname = input()

            print("Enter username ...program will generate a password for you")
            user_name = input()

            print("Email Address ...")
            email = input()

            password_generator = "12345678910!@#$%^&*()+-?><abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            password = "".join(random.sample(password_generator, 8))
            print("Password")

            save_user(create_user(user_name, email, password))
            save_credentials(create_credentials(fname, lname, user_name, email, password))
            print("\n")
            print(f"the username is {user_name} and the password is {password}")
            print("\n")


        elif short_code == "ex":                
            print("Bye ....")
            break
        else:
            print("Invalid command")

if __name__ == '__main__':
    main()
