from numbers import Real
import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction


# Req 2
def test_dish():
    # Verifica parâmetros no construtor
    with pytest.raises(TypeError, match="missing 2 required"):
        Dish()
    with pytest.raises(TypeError, match="missing 1 required"):
        Dish(3)
    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("invalid_dish", "30,00")
    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("invalid_dish", 0)

    dish_1 = {
        "name": "lasanha berinjela",
        "price": 27.00,
        "ingredients": {
            Ingredient("queijo mussarela"),
            Ingredient("tomate"),
            Ingredient("farinha"),
            Ingredient("sal"),
            Ingredient("agua"),
            Ingredient("berinjela"),
        },
        "recipe": [
            ("queijo mussarela", 15),
            ("tomate", 10),
            ("farinha", 10),
            ("sal", 5),
            ("agua", 10),
            ("berinjela", 1),
        ],
        "restrictions": {
            Restriction.ANIMAL_DERIVED,
            Restriction.LACTOSE,
            Restriction.GLUTEN,
        },
    }

    dish_2 = {
        "name": "arroz com brócolis",
        "price": 15.00,
        "ingredients": {"arroz", "sal", "azeite", "brócolis"},
        "restrictions": {},
    }

    instance_dish_1 = Dish(dish_1["name"], dish_1["price"])
    instance_dish_2 = Dish(dish_2["name"], dish_2["price"])
    instance_dish_3 = Dish(dish_1["name"], dish_1["price"])

    expected_repr_1_and_3 = str("Dish('lasanha berinjela', R$27.00)")
    expected_repr_2 = str("Dish('arroz com brócolis', R$15.00)")

    # Verifica se o médodo __repr__ retorna o resultado esperado
    assert str(repr(instance_dish_1)) == expected_repr_1_and_3
    assert str(repr(instance_dish_2)) == expected_repr_2
    assert str(repr(instance_dish_3)) == expected_repr_1_and_3
    assert str(repr(instance_dish_1)) == str(repr(instance_dish_3))
    assert str(repr(instance_dish_1)) != str(repr(instance_dish_2))

    # Verifica se o método __eq__ retorna o resultado esperado
    assert (instance_dish_1 == instance_dish_2) is False
    assert (instance_dish_1 == instance_dish_3) is True
    assert (instance_dish_2 != instance_dish_3) is True

    # Verifica se o método __hash__ retorna o resultado esperado
    assert hash(instance_dish_1) == hash(instance_dish_3)
    assert hash(instance_dish_1) != hash(instance_dish_2)

    # Verifica se o atributo "name" da instância é o esperado
    assert instance_dish_1.name == dish_1["name"]
    assert instance_dish_2.name == dish_2["name"]

    # Verifica o atributo "price" da instância é o esperado
    assert isinstance(instance_dish_1.price, Real) is True
    assert instance_dish_1.price == dish_1["price"]
    assert instance_dish_2.price == dish_2["price"]

    # Verifica o comportamento dos métodos add_ingredient_dependency
    # e get_ingredients
    for ingredient, amount in dish_1["recipe"]:
        instance_dish_1.add_ingredient_dependency(
            Ingredient(ingredient), amount
        )
    assert len(instance_dish_1.get_ingredients()) == len(dish_1["ingredients"])
    assert instance_dish_1.get_ingredients() == dish_1["ingredients"]

    # Verifica o comportamento do método get_restrictions
    assert instance_dish_1.get_restrictions() == dish_1["restrictions"]
