from math import floor

class Food:
    def __init__(self, name, price, quantity, recipe):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.recipe = recipe
        self.total_batches = self.quantity // self.recipe
        self.batch_cost = self.price / self.total_batches


class Recipe:
    def __init__(self, items):
        self.ingredients = items
        self.cost = 0

        for i in self.ingredients:
            self.cost += i.batch_cost

    def __str__(self):
        output = f"{'----------Recipe----------':^39}" + "\n"
        for item in self.ingredients:
            output += f"{item.name:<12}: {str(item.total_batches) + ' batches':>15}  @  ${item.batch_cost:<10,.2f}" + "\n"
        output += "\n"
        output += f"{'Possible batches:':<17}  {self.find_smallest_batches()} batches" + "\n"
        output += f"{'Cost per batch:':<17} ${self.cost:<15,.2f}"
        return output

    def find_smallest_batches(self):
        smallest_batch = self.ingredients[0].total_batches
        for item in self.ingredients:
            if item.total_batches < smallest_batch:
                smallest_batch = item.total_batches
        return floor(smallest_batch)