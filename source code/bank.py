
class bank():
    
    # initialize the balance to 0
    def __init__(balance, self, initial_balance = 0):
        self.balance = initial_balance
        self.interest_rate = 0
        self.loan_balance = 0 

    def withdraw(self, amount):
        # if the amount is greater than the balance, then send an error message
        if amount > self.balance:
            return f"The amount to withdraw exceeds the balance"
        else:
            newBalance = self.balance - amount
            return f"Your balance has been updated to ${newBalance}"
        
    def deposit(self, amount):
        # if loan, then take off 50% of the deposit to paying the loan.
        #     return only ${} has been put to your loan. We have deposited ${amount - amount*0.5}
        # else
        #     self.balance + amount
        #     f"${amount} has been deposited to your account
        pass

    def get_balance(self):
        # return current balance of bank account
        return f"your current balance is {self.balance}"
    
    def take_loan(self, principal, interest_rate, term)
        # take out a loan with specified principal, interest, term, and adds the loan to the balance.
        pass

    def get_loans(self):
        # returns the lost of all loans associated with this account
        pass
    
    
    
    

    
