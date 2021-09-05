class Credentials:
    """Class that generates new instances of credentials"""

    credentials_list = [] # Empty credentials list
    # Init method up here
    def save_credentials(self):

        '''
        save_credentials method save credentials objects into credentials_list
        '''

        Credentials.credentials_list.append(self)

    def __init__(self,first_name,last_name,user_name,password,email):

      # docstring removed for simplicity 

        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name 
        self.password = password
        self.email = email

    def delete_credentials(self):

        '''
        delete_credentials method deletes a saved credentials from the credentials_list
        '''

        Credentials.credentials_list.remove(self)
    @classmethod
    def find_by_email(cls,email):
        '''
        Method that takes in a email and returns a credentials that matches that email.

        Args:
            email: email to search for
        Returns :
            Credentials of person that matches the email.
        '''

        for credentials in cls.credentials_list:
            if credentials.email == email:
                return credentials
    @classmethod
    def credentials_exist(cls,email):
        '''
        Method that checks if a credentials exists from the credentials list.
        Args:
            email: email to search if it exists
        Returns :
            Boolean: True or false depending if the credentials exists
        '''
        for credentials in cls.credentials_list:
            if credentials.email == email:
                    return True

        return False   
    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list 

