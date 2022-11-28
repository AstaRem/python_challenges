# ask user name, then shout ir letter by letter as a cheerleaders do

name = input("Enter your name: ")

for letter in name:
    print(letter + "!")

print("What does it spell?")

print(f'{name.upper()}!')

