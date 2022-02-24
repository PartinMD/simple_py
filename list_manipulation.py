inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

# Inventory Amount
inventory_len = len(inventory);
print(inventory_len)

# First and Last Items in Inventory
first = inventory[0]
print(first)
last = inventory[-1]
print(last)

# Make a list Index 2 - 5
inventory_2_6 = inventory[2:6]
print(inventory_2_6)

# Make a list 0 - 2
first_3 = inventory[0:3]
print(first_3)

# How many twin beds in stock
twin_beds = inventory.count("twin bed")
print(twin_beds)

# Remove index 4
removed_item = inventory.pop(4)
print(removed_item)

# Insert new item at index 10
inventory.insert(10, "19th Century Bed Frame")
print(inventory)

# Adding lines in terminal
print(".")
print(".")
print(".")
# The sorting hat
inv_sorted = sorted(inventory)
print("This inventory is Sorted(): " + str(inv_sorted))

inventory.sort() 
print("The .sort() method also works: " + str(inventory))
