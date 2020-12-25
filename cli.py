import click
from pizza import Margherita, Pepperoni, Hawaiian, BasePizza
from decorators import log

MENU = {"margherita": Margherita(), "pepperoni": Pepperoni(), "hawaiian": Hawaiian()}


@log("🍕‍Приготовили за {}с!")
def bake(pizza: "BasePizza"):
    """Готовим пиццу"""
    pass


@log("🛵 Доставили за {}с!")
def delivery(pizza: "BasePizza"):
    """Доставляем пиццу"""
    pass


@log("🏠 Забрали за {}с!")
def pickup(pizza: "BasePizza"):
    """Выдаем пиццу"""
    pass


@click.group()
def cli():
    pass


@cli.command()
@click.option("--delivery", "delivery_flag", default=False, is_flag=True)
@click.argument("pizza", nargs=1)
def order(pizza: str, delivery_flag: bool):
    """Готовит и доставляет пиццу"""
    if pizza not in MENU:
        print(
            "Такой пиццы пока нет в нашем меню. "
            "Выберите одну из возможных опций: "
            f'{", ".join(MENU)}'
        )
        return

    bake(MENU[pizza])
    if delivery_flag:
        delivery(MENU[pizza])
    else:
        pickup(MENU[pizza])


@cli.command()
def menu():
    """Выводит меню"""
    for pizza in MENU.values():
        print(f'- {pizza}: {", ".join(pizza.dict())}')


if __name__ == "__main__":
    cli()
