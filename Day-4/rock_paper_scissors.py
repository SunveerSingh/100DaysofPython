import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_input = int(input("Type 0 for rock, 1 for paper and 2 for scissors: "))

symbol = [rock, paper, scissors]
if user_input == 0:
  print(f"Your choice: \n {symbol[0]}")
elif user_input == 1:
  print(f"Your choice: \n {symbol[1]}")
else: print(f"Your choice: \n {symbol[2]}")

random_symbol = random.randint(0,2)
if random_symbol == 0:
  print(f"Computer Choose: \n {symbol[0]}")
elif random_symbol == 1:
  print(f"Computer Choose: \n {symbol[1]}")
else: print(f"Computer Choose: \n {symbol[2]}")

if user_input == 0 and random_symbol == 1:
  print(" Computer Wins")
elif user_input == 1 and random_symbol == 0:
  print("You Win")
elif user_input == 0 and random_symbol == 2:
  print("You Win")
elif user_input == 2 and random_symbol == 0:
  print("Computer Win")
elif user_input == 2 and random_symbol == 1:
  print("You Win")
elif user_input == 1 and random_symbol == 2:
  print("Computer  Win")
else: print("It's a Draw")