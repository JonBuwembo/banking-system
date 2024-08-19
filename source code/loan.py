import time
import threading

class Loan:

    def __init__(self, principle, interest_rate):
        self.principle = principle
        self.interest_rate = interest_rate
        self.loan_balance = principle
        # loan functionality activated
        self.running = True
    
    
    # calculate_interest():     separate function to calculate interest
    # apply_interest():         separate function to apply interest (apply_interest()) --> utilizes calculate_interest()
    # start_interest_accrual(): overtime increase the interest
    # make_payment():           make a payment to the loan
    # stop_interest_accrual():  stop the interest increasing
    # get_loan():               get my loan balance


    def calculate_interest(self):
        # balance *(1 + rate%)
        return self.loan_balance * self.interest / 100


    def apply_interest(self):
        interest = self.calculate_interest()
        self.loan_balance += interest # add interest
        return f"Interest of {interest} has been applied. Current balance is now {self.balance}"
        

    def start_interest_accrual(self):
        # threading
        def accrue_interest():
            while self.running:
                time.sleep(300) # 5 minutes, every five minutes interest rate increases.
                print(self.apply_interest()) 
        
        thread = threading.Thread(target=accrue_interest, daemon=True)
        thread.start()


    def stop_interest_accrual(self):
        # stops the interest accrual for all loans.
        self.running = False

    def make_payment(self, amount):
        # if the payment exceeds the loan balance ...
        # if the payment does not cover all the loan balance ...
        # if the payment is not a valid input, less than 0 ...

        if self.loan_balance >= amount and amount > 0:
            self.loan_balance -= amount
            return f"payment of ${amount} sucessfully processed. There still remains ${self.loan_balance} in loans."
        elif self.loan_balance < amount:
            return "ERROR: You are repaying more than the outstanding loan balance."
        else:
            return "ERROR: Invalid Input" 
        

    def get_loan_balance(self):
        return f"You owe ${self.loan_balance} in loans."
        
