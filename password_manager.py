import re

#parent class
class BasePasswordManager:
    #defining old password functionality
    def old_passwords(self):
        old_password = ['01234567', '1234shukla', '2207shuklaji','1234']
        self.old_password = old_password[-1]
        return self.old_password

    # defining get password functionality
    def get_password(self):
        current_password = self.old_password
        self.current_password = current_password
        return "Current password is " + self.current_password

    # defining is password correct functionality
    def is_correct(self):
        password = input(' ****Please type in your password here****:-- > ')
        self.password = password
        print("New passsword is the same as the current password:", self.password == self.current_password)
        return self.password

#child class
class PasswordManager(BasePasswordManager):

    # defining level of password functionality
    def get_level(self):
        self.present_security_level = 0
        check_alphabet = False
        check_number = False
        if self.password.isdigit():
            self.present_security_level = 0
            print('Security level is', self.present_security_level, ' :WEAK Password')
            print('Password consists of Digits only')

        elif self.password.isalpha():
            self.present_security_level = 0  # For Level 0 of security
            print('Security level is', self.present_security_level, ' :WEAK Password')
            print('Password consists of Alphabets only')

        elif check_alphabet == False and check_number == False and (
                bool(re.match('^[a-zA-Z0-9]*$', self.password)) == True):
            for i in self.password:
                if i.isalpha():
                    check_alphabet = True
            for j in self.password:
                if j.isnumeric():
                    check_number = True
                if check_alphabet == True and check_number == True:
                    self.present_security_level = 1  # For Level 1 of Security
                    print('Security Level is-->', self.present_security_level, ': MODERATE')
                    print('**Password is alphanumeric & NO special characters are present**')
                    break

        elif check_alphabet == False and check_number == False:
            for i in self.password:
                if i.isalpha():
                    check_alphabet = True
            for j in self.password:
                if j.isnumeric():
                    check_number = True
            if check_alphabet == True and check_number == True and (
                    bool(re.match('^[a-zA-Z0-9]*$', self.password)) == False):
                self.present_security_level = 2  # For Security_Level 2
                print('Security level is', self.present_security_level, ':STRONG')
                print('Password is alphanumeric  alongwith special characters also present')
            else:
                self.present_security_level = 1

                print('Security level is', self.present_security_level, ': MODERATE')
                print('Password contains special characters with either numbers or alphabets only')

    # defining if password can be set functionality
    def set_password(self):
        if len(self.password) < 6:
            print("New Password must have 8 characters or More")
            print("Password Change : UNSUCCESSFUL")
        elif self.present_security_level < 2:
            print("New password must contain at least 1 special character with numbers and alphabets")
            print("Password Change : UNSUCCESSFUL")
        elif self.password == self.current_password:
            print("Password Change: No Changes Detected")
        else:
            print("Password Change:SUCCESSFUL")
            print("Congratulations")



#Here I am calling functions by making object of child class
customer = PasswordManager()
customer.old_passwords()
customer.get_password()
customer.is_correct()
customer.get_level()
customer.set_password()