class User:
    name = "Ashliegh"
    email = "ashlieghdawn@icloud.com"
    password = "abc234"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")

class Employee(User):
    base_pay = 11.00
    department = "General"
    pin_number = "3980"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_pin = input("Enter your pin: ")
        if (entry_email == self.email and entry_pin == self.pin):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")
            
class Supplier(User):
    base_pay = 13.00
    entry_phonenumber = "5416869199"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_phonenumber = input("Enter your phone number: ")
        entry_password = input("Enter your password: ")
        if (entry_phonenumber == self.phonenumber and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or phone number is incorrect.")
        
    

customer = User()
customer.getLoginInfo()

manager = Employee()
manager.getLoginInfo()
        
