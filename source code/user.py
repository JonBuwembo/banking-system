from bank import BankAccount
from loan import Loan

my_account = BankAccount()


# PART 1: USER TAKES OUT A LOAN AND MAKES A DEPOSIT
# suppose this person enjoys taking so many loans.
print(my_account.deposit(100))
print(my_account.take_loan(5000, 5))
print(my_account.take_loan(1200, 5))
print(my_account.take_loan(600, 5))
for loan in my_account.get_loans():
    print(loan)
print(my_account.deposit(30))
print(my_account.get_balance())
print(my_account.get_loan_balance()) 

# PART 2: USER MAKES A PAYMENT TO THE LOAN
print(my_account.make_loan_payment(0, 100))
print(my_account.get_loans()) # print all loans in a list
print(my_account.get_loan_balance())