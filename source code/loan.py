class loan:

    def __init__(self, principle, interest, term):
        self.principle = principle
        self.interest = interest
        self.term = term
        self.balance = principle
    
    
    # calculate_interest():     separate function to calculate interest
    # apply_interest():         separate function to apply interest (apply_interest()) --> utilizes calculate_interest()
    # start_interest_accrual(): overtime increase the interest
    # make_payment():           make a payment to the loan
    # stop_interest_accrual():  stop the interest increasing
    # get_loan():               get my loan balance


    def pass_interest_accrual():
        # simulates the passing of five minutes, applying interest or increasing interest rate
        pass

    def stop_all_loans_interest_accrual(self):
        # stops the interest accrual for all loans.
        pass

    def calculate_interest():
        pass

    def apply_interest():
        pass

    def start_interest_accrual(self):
        pass

    def stop_interest_accrual(self):
        pass

    def make_payment(self):
        pass

    def get_loan_balance(self):
        pass
