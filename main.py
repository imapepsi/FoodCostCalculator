from cooking import *

def is_evaluable(text):
    try:
        eval(text)
        return True
    except NameError as e:
        return False

# Get Recipe
filename = input("Enter recipe csv file: ")
csv = open(filename, 'r')
lines = csv.readlines()
lines = lines[1:]
items = []
for line in lines:
    data = line.strip("\n")
    data = data.split(",")
    for i in range(len(data)):
        if is_evaluable(data[i]):
            data[i] = eval(data[i])

    items.append(Food(data[0], data[1], data[2], data[3]))


my_recipe = Recipe(items)

store_cost = float(input("Enter cost of food if bought at the store: $"))

print("\n")
print(my_recipe)
print(f"{'Cost @ Store:':<17} ${store_cost:<10,.2f}")

difference = store_cost - my_recipe.cost
if store_cost > my_recipe.cost:
    print(f"{'Savings:':<17} ${abs(difference):,.2f}")
elif store_cost < my_recipe.cost:
    print(f"{'Expense:':<17} ${abs(difference):,.2f}")
else:
    print("No cost difference")
