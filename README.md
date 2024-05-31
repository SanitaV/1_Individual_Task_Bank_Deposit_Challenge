# Bank Deposit Challenge
## Easy Level
**Description:**
Create a program where the user can input deposits into a bank account. The program should use `if-else` statements, `input()`, `int()` and while True loop to keep track of deposits.

**Instructions:**
1. Welcome the user to the bank
2. Initiate balance = 0
3. Ask the user to input the amount of money they want to deposit.
4. Add the deposit amount to the total balance
5. Ask the user if they want to make another deposit or exit the bank. 
6. If they choose to make another deposit, repeat the process (while True).
7. If not, print the total amount deposited and exit the bank.


### “*In case code part doesn`t open or show properly - I will copy it here also:*“
```py
print("Welcome to the bank!")
print()

balance = 0
while True:
          deposit_amount = float(input("Please input the amount of money you want to deposit: "))
          balance += deposit_amount
          total = round(balance, 2)
          print(f"Your current balance is: {total}")

          question = input("Do you want to make another deposit or EXIT the bank? ")
          print()

          if question.lower() in ["exit", "e"]:
              print(f"You have deposited {total} EUR")
              print("Exiting the bank.")
              break
```
