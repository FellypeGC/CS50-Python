# Ask user for their name, remove whitespace from str and capitalize first letter
name = input("What's your name? ").strip().title()

# Split user's name into first and last name
firstName, lastName = name.split()

# Say hello to user
print(f"hello, {firstName}", end="")