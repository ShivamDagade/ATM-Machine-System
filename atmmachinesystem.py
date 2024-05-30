class Customer:
    
    bank='SBI Bank'
    
    def __init__(self,accno,balance=0.0):
        self.accno=accno
        self.balance=balance
    
    def deposit(self,amount):
        self.balance=self.balance+amount
        print('Deposit Transaction Successfully Completed')
    
    def withdraw(self,amount):
        if amount>self.balance:
            print('Insufficent Balance')
        elif (amount>(self.balance-500)):
            print('Please Maintain Minimun Balance of 500')    
        elif(amount%100==0 or amount%500==0):
            self.balance=self.balance-amount
            print('Withdraw Transaction Successfully Completed')
        else:
            print('Please Enter Amount In Multiple Of 100 or 500')
    def inquiry(self):
        print('Your Balance : ',self.balance)
        
print('** Welcome To',Customer.bank,'**')
accno=input('Enter Your Account Number : ')
c=Customer(accno)
while 1:
    print('d-Deposit \nw-Withdraw \ni-Inquiry \ne-Exit')
    option=input('Enter The Option You Want To Perfrom Operation : ').lower()
    if option=='d':
        amount=float(input('Enter Amount You Want To Deposit : '))
        c.deposit(amount)
    elif option=='w':
        amount=float(input('Enter Amount You Want To Withdraw : '))
        c.withdraw(amount)
    elif option=='i':
        c.inquiry()
    elif option=='e':
        print('Thanks For Banking With Us')
        break
    else:
        print('Please Choose Valid Option')