from loan import Loan

class bank():
    
    # initialize the balance to 0
    def __init__(self, initial_balance = 0):
        self.balance = initial_balance
        self.interest_rate = 0
        self.loans = []
        self.loan_balance = 0

    def withdraw(self, amount):
        # if the amount is greater than the balance, then send an error message
        if amount > self.balance:
            return f"The amount to withdraw exceeds the balance"
        else:
            self.balance -= amount
            return f"Your balance has been updated to ${self.balance}"
        
    def deposit(self, amount):
        # if loan, then take off 50% of the deposit to paying the loan.
        #     return "only ${} has been put to your loan. We have deposited ${amount - amount*0.5}
        # else
        #     self.balance + amount
        #     f"${amount} has been deposited to your account

        if self.loan_balance > 0:
            amount_half= amount * 0.5
            self.loan_balance -= amount_half
            self.balance += amount_half
            return f"only ${amount_half} has been put to your loan. We have deposited ${amount_half}"
        else:
            self.balance += amount
            return f"${amount} has been deposited to your account"

    def get_balance(self):
        # return current balance of bank account
        return f"your current balance is {self.balance}"
    
    def take_loan(self, principal, interest_rate):
        # take out a loan with specified principal, interest and adds the loan to the balance.
        # start accruing interest
        loan = Loan(principal, interest_rate)
        self.loan_balance += principal
        loan.start_interest_accrual()
        return f"${self.loan_balance} has been borrowed."

    def get_loans(self):
        # returns a list of all loans associated with this account
        return  [loan.get_loan_balance() for loan in self.loans]
    
    
    
    
    

    
