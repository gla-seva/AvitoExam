import pytest
from pizza import Margherita, Pepperoni, Hawaiian, BasePizza


@pytest.mark.parametrize(
    "pizza_class, name",
    [
        (Margherita, "Margherita 🧀"),
        (Pepperoni, "Pepperoni 🍕"),
        (Hawaiian, "Hawaiian 🍍"),
    ],
)
def test_default_pizza(pizza_class, name: str):
    assert str(pizza_class()) == name
    assert pizza_class().size == "L"


def test_pizza_siz_comparison():
    assert Hawaiian(size="L") != Hawaiian(size="XL")
    assert Margherita() != Hawaiian()
    with pytest.raises(TypeError):
        Hawaiian() == 1


def test_ingredients_pizza():
    ingredients = {"tomato sauce": 100, "mozzarella": 150, "tomatoes": 300}
    assert Margherita().dict() == ingredients


def test_wrong_pizza_size():
    with pytest.raises(ValueError):
        Hawaiian(size="S")
