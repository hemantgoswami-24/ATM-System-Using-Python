class Atm:
    def __init__(self,name):
        self.name = name
        self.__balance = 0
        self.__pin = self.create_pin()

    def check_balance(self):
        if self.check_pin():
            print(f"Your Balance is : Rs.{self.__balance}/-")

    def deposit(self):
        if self.check_pin():
            amount = int(input("Enter the amount: "))
            if amount<=0:
                print("Please Enter a Valid Amount!")
            else:
                self.__balance+=amount
                print(f"Rs.{amount}/- has been depositted successfully!")

    def withdraw(self):
        if self.check_pin():
            amount = int(input("Enter the amount: "))
            if amount<=0:
                print("Please Enter a Valid Amount!")
            elif amount>self.__balance:
                print("Insufficient Funds!")
            else:
                self.__balance-=amount
                print(f"Rs.{amount}/- has been withdrawn successfully!")
    
    def create_pin(self):
        pin = input("Enter your pin: ")
        
        while True:
            if len(pin.strip()) == 4:
                break
            else:
                print("Your Pin Should Be Of 4-Digit Only!")
                pin = input("Enter your pin: ")
    
        pin_2 = input("Re-Enter your pin: ")
        
        if pin == pin_2:
            print("Your Pin is created successfully!")
            return int(pin)
        else:
            print("Your Pins Don't Match! Please Try Again!")

    def check_pin(self):
        user_pin = int(input("Enter Your Pin: "))
        count=2
        while count>0:
            if self.__pin == user_pin:
                return True
            else:
                print("\nYour Pins Don't Match! Please Try Again!")
                print(f"You have only {count} attempts left.")
                user_pin = int(input("\nEnter Your Pin: "))
                count-=1
        else:
            if self.__pin == user_pin:
                return True
            else:
                print("\nYour Pins Don't Match!")
                print("Your Card is Blocked!")
om = Atm("Om")
om.check_balance()
om.deposit()
om.withdraw()
