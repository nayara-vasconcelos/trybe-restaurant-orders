from csv import DictReader
from typing import Dict

from src.models.dish import Recipe
from src.models.ingredient import Ingredient

BASE_INVENTORY = "data/inventory_base_data.csv"

Inventory = Dict[Ingredient, int]


def read_csv_inventory(inventory_file_path=BASE_INVENTORY) -> Dict:
    inventory = dict()

    with open(inventory_file_path, encoding="utf-8") as file:
        for row in DictReader(file):
            ingredient = Ingredient(row["ingredient"])
            inventory[ingredient] = int(row["initial_amount"])

    return inventory


# def write_csv_inventory(inventory: Dict, inventory_file_path=BASE_INVENTORY):
#     with open(inventory_file_path, "w", encoding="utf-8") as file:
#         headers = ["ingredient", "initial_amount"]
#         writer = DictWriter(file, fieldnames=headers)
#         writer.writeheader()
#         for ingredient, amount in inventory.items():
#             row = {"ingredient": ingredient.name, "initial_amount": amount}
#             writer.writerow(row)


# Req 5
class InventoryMapping:
    def __init__(self, inventory_file_path=BASE_INVENTORY) -> None:
        self.inventory = read_csv_inventory(inventory_file_path)

    # Req 5.1
    def check_recipe_availability(self, recipe: Recipe):
        for ingredient, required_amount in recipe.items():
            is_available = (
                ingredient in self.inventory
                and self.inventory[ingredient] >= required_amount
            )
            if not is_available:
                return False

        return True

    # Req 5.2
    def consume_recipe(self, recipe: Recipe) -> None:
        if not self.check_recipe_availability(recipe):
            raise ValueError("Some ingredients are unavailable.")

        for ingredient, amount in recipe.items():
            self.inventory[ingredient] -= amount

        return None
