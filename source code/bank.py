from loan import Loan
from typing import List

class BankAccount():
    
    # initialize the balance to 0
    def __init__(self, initial_balance = 0):
        self.balance = initial_balance
        self.interest_rate = 0
        self.loans: List[Loan] = [] # each loan is an instance of the Loan Class
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

        if self.loan_balance > 0 and amount > 0:
            amount_half = amount * 0.5
            self.loan_balance -= amount_half
            self.balance += amount_half
            return f"only ${amount_half} has been put to your loan. We have deposited ${amount_half}"
        elif amount > 0:
            self.balance += amount
            return f"${amount} has been deposited to your account"

    def get_balance(self):
        # return current balance of bank account
        return f"your current balance is {self.balance}"
    
    def take_loan(self, principal, interest_rate):
        # take out a loan with specified principal, interest and adds the loan to the balance.
        # start accruing interest
        loan = Loan(principal, interest_rate)
        self.loans.append(loan) # add to list of loans
        self.loan_balance += principal # increase total loans owed
        loan.start_interest_accrual()
        return f"${self.loan_balance} has been borrowed."

    def get_loans(self):
        # returns a list of all loans associated with this account
        return  [loan.get_loan_balance() for loan in self.loans]
    
    def get_loan_by_index(self, index):
        return self.loans[index] if 0 <= index < len(self.loans) else None
    
    # add a way for the user to make a payment on their account
    def make_loan_payment(self, loan_index, amount):
        if 0 <= loan_index < len(self.loans):
            # make a payment to that specific loan in the list of loans
            # 500 - amount
            # if the amount paying is greater than the loan, then its an error.
            # do not pay more than you can afford
            loan = self.get_loan_by_index(loan_index) 
            if amount <= self.balance:
                # you pay the loan so your balance and loan balance is depleted 
                self.balance -= amount
                self.loan_balance -= amount
                # make payment to loan
                loan.make_payment(amount)
                return f"You have paid ${amount} to your {loan_index + 1}th/nd loan. You have ${self.loan_balance} left."
            else:
                return "You have insufficient funds to pay this loan."
        else:
            return f"ERROR: No such loan exists."

    def get_loan_balance(self):
        return f"You owe: ${self.loan_balance}"
   
    
    

    
