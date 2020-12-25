import pytest
from click.testing import CliRunner
import cli
from unittest.mock import patch
import decorators


@pytest.fixture(scope="module")
def runner():
    return CliRunner()


def test_menu_stdout(runner):
    result = runner.invoke(cli.cli, ["menu"])
    expected_out = (
        "- Margherita 🧀: tomato sauce, mozzarella, tomatoes\n"
        "- Pepperoni 🍕: tomato sauce, mozzarella, pepperoni\n"
        "- Hawaiian 🍍: tomato sauce, mozzarella, chicken, pineapples\n"
    )
    assert result.exit_code == 0
    assert result.output == expected_out


def test_order_delivary_stdout(runner):
    with patch.object(decorators, "randint", return_value=0):
        result = runner.invoke(cli.cli, ["order", "margherita", "--delivery"])
    expected_out = "🍕‍Приготовили за 0с!\n" "🛵 Доставили за 0с!\n"
    assert result.exit_code == 0
    assert result.output == expected_out


def test_order_pickup_stdout(runner):
    with patch.object(decorators, "randint", return_value=0):
        result = runner.invoke(cli.cli, ["order", "margherita"])
    expected_out = "🍕‍Приготовили за 0с!\n" "🏠 Забрали за 0с!\n"
    assert result.exit_code == 0
    assert result.output == expected_out


def test_order_wrong_pizza_stdout(runner):
    with patch.object(decorators, "randint", return_value=0):
        result = runner.invoke(cli.cli, ["order", "diablo"])
    expected_out = (
        "Такой пиццы пока нет в нашем меню. "
        "Выберите одну из возможных опций: margherita, pepperoni, hawaiian\n"
    )
    assert result.exit_code == 0
    assert result.output == expected_out
