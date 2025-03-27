# Define a tuple of colors
colors = ("red", "blue", "green", "yellow", "black", "white", "purple", "orange")

# Take color input from the user
colour_check = input("Enter the color you want to check: ")

# Take index input from the user
try:
    user_index = int(input(f"Enter the index (0 to {len(colors)-1}): "))
    
    # Check if the index is valid
    if 0 <= user_index < len(colors):
        if colors[user_index] == colour_check:
            print(f"Yes, {colour_check} is present at index {user_index}.")
        else:
            print(f"No, {colour_check} is not at index {user_index}. It is {colors[user_index]}.")
    else:
        print("Index out of range!")
except ValueError:
    print("Please enter a valid integer for index.")