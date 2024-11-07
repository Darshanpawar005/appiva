# Class for Items
class Item():
  # Constractor for class
  def __init__(self, weight, value):
    self.weight = weight
    self.value = value

# Function for calculating maximum profit
def knapsack_problem(n, items, capacity):

  items.sort(key=lambda x: x.value / x.weight, reverse=True)

  Total_profit = 0

  for item in items:
    if capacity >= item.weight:
      capacity -= item.weight
      Total_profit += item.value
    else:
      fractional = capacity / item.weight
      Total_profit += item.value * fractional
      break

  return Total_profit

# User input
Items = []
n = int(input("Enter number of items : "))
for i in range(n):
  print(f"For item {i+1} :")
  weight = int(input("Enter weight of item : "))
  value = int(input("Enter value of item : "))
  item = Item(weight,value)
  Items.append(item)
Capacity = int(input("Enter capacity of bag : "))

print(f"Maximum profit possible is {knapsack_problem(n, Items, Capacity)}")