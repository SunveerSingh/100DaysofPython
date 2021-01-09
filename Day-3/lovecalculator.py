
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

name_combined = f"{name1}{name2}"
print(name_combined)
count_t = name_combined.count('t')
count_r = name_combined.count('r')
count_u = name_combined.count('u')
count_e = name_combined.count('e')
count_l = name_combined.count('l')
count_o = name_combined.count('o')
count_v = name_combined.count('v')

true = count_t + count_r + count_u + count_e
love = count_l + count_o + count_v + count_e

print(f"Your Score is {true}{love}%")