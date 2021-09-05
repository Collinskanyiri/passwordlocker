#!/usr/bin/env python3.8

from math import log
from credentials import Credentials
from user import User
import random

"""
Run module
"""


def create_user(user_name, password):
    '''
    Function that creates new user
    '''
    new_user = User(user_name, password)
    return new_user


def save_user_details(user):
    '''
    saves user details
    '''
    user.save_user_details()


def check_existing_users(name):
    '''
    Function that checks if a user account name exists
    '''

    return User.user_exist(name)


def display_user():
    '''
    display users
    '''
    return User.display_users()


def user_log_in(user_name, password):
    '''
    Function to allow user to log-in to their credentials account
    '''
    log_in = User.log_in(user_name, password)
    if log_in != False:
        return User.log_in(user_name, password)


def create_credentails(credentials_user_name, email, credentials_site, credentials_password):
    '''
    Function to create new credentials
    '''

    new_credentails = Credentials(
        credentials_user_name, email, credentials_site, credentials_password)

    return new_credentails


def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()


def check_existing_credentials(credentials_user_name):
    '''
    Function that checks if a user credentials_site exists
    '''
    return Credentials.credentials_exists(credentials_user_name)


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


def find_credentials(credentials_site):
    """
    function to find credentials based on credentials_site 
    """
    return Credentials.find_credentials(credentials_site)


def del_credentials(credentials):
    '''
    Function to delete credentials
    '''
    credentials.delete_credentials()


def main():
    print("Hello Welcome to PASSWORDLOCKER")

    while True:

        print("""Short codes:
        nw - Create a new passwordlocker account \n
        lg - Log-in to your already existing account on passwordlocker \n
        ex - Exit the passwordlocker account """)
        short_code = input().lower()

        if short_code == "nw":
            """
            short_code to create new account on passwordlocker
            """
            print("\n")
            print(" New password locker account")
            print("-*-"*10)

            print("User name ...")
            user_name = input()

            print("password ...")
            user_password = input()

            save_user_details(create_user(user_name, user_password))

            print("\n")
            print(
                "Welcome {user_name} Your account has been created successfully!\n")
              
        elif short_code == "lg":
            """
            short_code to allow user to Log-in to already existing account on passwordlocker 
            """
            print("\n")
            print("*"*10)
            print("Log-in to your Passwordlocker Account")
            print("Enter the user name")
            user_name = input()

            print("Enter the password")
            user_password = input()

            if user_log_in(user_name, user_password) == None:
                print("\n")
                print("Invalid user name or password, try again or Create a New Account")
                print("\n")

            else:

                user_log_in(user_name, user_password)
                print("\n")
                print("Welcome {user_name} You have successfully logged into your Account")
                print("\n")
                print("*Use the following codes to navigate*")
                print("\n")

                
                while True:
                    print("""Use these short codes:
                    cc - create a new credentials_user account with a user_defined password,\n
                    can -create a new_credentials_user account with auto-generated password,\n
                    sv - add credentials to an already exiting account,\n
                    dc - display credentials\n
                    del - delete an existing credentials account\n
                    log - log-out """)
                    short_code = input().lower()

                    if short_code == "cc":
                        print("new credentials_user_name with a user_defined password")
                        print("-*-" * 10)
                        
                        print("credentials name ...")
                        credentials_name = input()

                        print("First name ....")
                        fname = input()

                        print("Last name ...")
                        lname = input()

                        print("Enter username ...")
                        credentials_user_name = input()

                        print("""What account would like to create credentials for?\n
                               eg; Facebook""")
                        credentials_site = input()

                        print("Email Address ...")
                        email = input()

                        print("Enter a password")
                        credentials_password = input()

                        save_credentials (create_credentails(credentials_name, credentials_user_name, fname, lname, email, credentials_password, credentials_site))
            
                        print("\n")
                        print("A new {credentials_site} account by {fname} has successfully been created")
                        print("The username is {credentials_user_name} and the password is {credentials_password} ")
                        print("\n")

                    elif short_code == "can":
                       print("new credentials_user_name with auto-generated password")
                       print("-*-"*10)

                       print("credentials name ...")
                       credentials_name = input()

                       print("First name ....")
                       fname = input()

                       print("Last name ...")
                       lname = input()

                       print("Enter username ...program will generate a password for you")
                       credentials_user_name = input() 

                       print("""What account would like to create credentials for?\n
                               eg; Facebook""")
                       credentials_site = input()

                       print("Email Address ...")
                       email = input()

                       password_generator = "12345678910!@#$%^&*()+-?><abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
                       credentials_password = "".join(random.sample(password_generator, 8))
                       print("Password")

                       save_credentials (create_credentails(credentials_name, credentials_user_name, fname, lname, email, credentials_password, credentials_site))
                       print("\n")
                       print("The username is {credentials_user_name} and the password is {credentials_password} ")
                       print("\n")

                    elif short_code == "sv":
                        print("\n")
                        print("add credentials to an already exiting account")
                        print("-*-"*10)

                        print("credentials name ...")
                        credentials_name = input()

                        print("user name ...")
                        credentials_user_name = input()

                        print("Email Address ...")
                        email = input()

                        print("Password...")
                        credentials_password = input()

                        print("""What account would like to create credentials for?\n
                               eg; Facebook""")
                        credentials_site = input()

                        save_credentials(create_credentails(credentials_name, credentials_user_name, email, credentials_password, credentials_site))

                        print("\n")
                        print(
                            "Credentials for {credentials_site} have been successfully saved !\n")
                        print("\n")
                    
                    elif short_code == "dc":
                        print("\n")
                        print("display credentials")
                        print("-*-"*10)
                       
                        if display_credentials(credentials_user_name):
                            print("display credentials for ...")
                            credentials_name = input()
                            
                            print("\n")
                            print("{credentials_user_name}\'s credentials")
                            print("*"*10)

                            for Credentials in display_credentials(credentials_name):
                                print("Site ..... {credentials.credentials_site}")
                                print("UserName .... {credentials.credentials_user_name}")
                                print("Email .... {credentials.email}")
                                print("Password .... {credentials.credentials_password}")
                                print("*"*10)
                        else:
                            print("\n")
                            print("Sorry, there is no account maching your details.")
                            print("\n")

                    elif short_code == "del":
                        
                        print("Enter name of credentials you want to delete")
                        credentials_name = input()

                        if check_existing_credentials(credentials_name):
                            delete_credentials_name = find_credentials(
                                credentials_name)
                            # print(f" {delete_credentials_name}")
                            print("Your stored credentials for: {credentials_name} has been deleted Successfully \n")
                        else:
                            print(" The Credentials does not Exist ⚠️ ")

                    elif short_code == "log":
                        print("logging out")
                        break

                    else:
                        print("invalid command")

        elif short_code == "ex":
                     print("Bye ....")
        break
    else:
        print("Invalid command")

if __name__ == '__main__':
    main()
