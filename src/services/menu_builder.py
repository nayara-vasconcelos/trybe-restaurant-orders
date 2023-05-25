import pandas as pd

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str):
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 4
    def _format_menu(self, dish):
        return {
            "dish_name": dish.name,
            "ingredients": dish.get_ingredients(),
            "price": dish.price,
            "restrictions": dish.get_restrictions(),
        }

    def _check_dish_restrictions(self, restriction, dish_restrictions):
        if restriction is None:
            return False

        for dish_restriction in dish_restrictions:
            if dish_restriction == restriction:
                return True

        return False

    def get_main_menu(self, restriction=None) -> pd.DataFrame:
        menu = []
        for dish in self.menu_data.dishes:
            if self.inventory.check_recipe_availability(
                dish.recipe
            ) and not self._check_dish_restrictions(
                restriction, dish.get_restrictions()
            ):
                menu.append(self._format_menu(dish))

        return pd.DataFrame(menu)
