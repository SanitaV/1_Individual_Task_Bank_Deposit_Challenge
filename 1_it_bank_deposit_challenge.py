Automatically generated by Colab.
Original file is located at
    https://colab.research.google.com/drive/1gJXOVIWVj2-mS5W74s07Qf-67oG-u51C

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
