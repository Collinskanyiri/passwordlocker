class User:
    """
    class that generates new instances of users
    """

    user_list=[] # Empty user list

    def __init__(self,user_name,email,password):


 

        self.user_name = user_name
        self.email = email
        self.password = password

    def save_user_details(self):
        """
        save_contact method saves user objects into user_list
        """
        User.user_list.append(self)

    @classmethod
    def display_users(cls):
        """
        method that returns the class list
        """
        return cls.user_list

 