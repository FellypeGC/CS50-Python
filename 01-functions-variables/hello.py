# Ask user for their name, remove whitespace from str and capitalize first letter
name = input("What's your name? ").strip().title()


# Say hello to user
print(f"hello, {name}", end="")