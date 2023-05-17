import pytest

from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient_name_1 = str("tomate")
    ingredient_name_2 = str("queijo parmesão")
    ingredient_name_3 = str("queijo parmesão")
    ingredient_1 = Ingredient(ingredient_name_1)
    ingredient_2 = Ingredient(ingredient_name_2)
    ingredient_3 = Ingredient(ingredient_name_3)
    ingredient_1_expected_restrictions = set()
    ingredient_2_expected_restrictions = set(
        {Restriction.LACTOSE, Restriction.ANIMAL_DERIVED}
    )

    expected_result_repr_1 = str("Ingredient('tomate')")
    expected_result_repr_2 = str("Ingredient('queijo parmesão')")
    expected_result_repr_3 = str("Ingredient('queijo parmesão')")

    # Verifica parâmetros no construtor
    with pytest.raises(TypeError, match="missing 1 required"):
        Ingredient()

    # Verifica se uma instância de Ingredient foi criada
    assert isinstance(ingredient_1, Ingredient)

    # Verifica se a instância foi criado com o nome correto
    assert ingredient_1.name == ingredient_name_1
    assert ingredient_2.name == ingredient_name_2

    # Verifica as restrições de cada ingrediente
    assert ingredient_1.restrictions == ingredient_1_expected_restrictions
    assert ingredient_2.restrictions == ingredient_2_expected_restrictions

    # Verifica se o método __repr__ retorna o resultado esperado
    assert str(repr(ingredient_1)) == expected_result_repr_1
    assert str(repr(ingredient_2)) == expected_result_repr_2
    assert str(repr(ingredient_3)) == expected_result_repr_3
    assert (repr(ingredient_2) == repr(ingredient_3)) is True
    assert (repr(ingredient_1) == repr(ingredient_2)) is False

    # Verifica se o método __eq__ retorna o resultado esperado
    assert (ingredient_1 == ingredient_2) is False
    assert (ingredient_2 == ingredient_3) is True
    assert (ingredient_1 != ingredient_2) is True
    assert (ingredient_2 != ingredient_3) is False

    # Verifica se o método __hash__ retorna o resultado esperado
    assert hash(ingredient_1) != hash(ingredient_2)
    assert hash(ingredient_2) == hash(ingredient_3)
