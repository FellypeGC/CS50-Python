# Ask user for their name, remove whitespace from str and capitalize first letter
# name = input("What's your name? ").strip().title()

# Split user's name into first and last name
# firstName, lastName = name.split()

# Say hello to user
# print(f"hello, {firstName}", end="")

# Say hello to user but in a function
# def hello(to):
#     print(f"hello, {firstName}", end="")

def hello(to="world"):
    print(f"hello, {to}")

hello()
name = input("What's your name? ")
hello(name)
