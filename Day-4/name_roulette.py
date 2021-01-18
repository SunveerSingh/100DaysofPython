import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

total_names = len(names)
random_name = random.randint(0, total_names-1)
name = names[random_name]
print(f"{name} will pay the bill")
