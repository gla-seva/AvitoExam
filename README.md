# Avito Exam

Для просмотра меню введите `python cli.py menu`
Для заказа пиццы Маргарита введите `python cli.py order margherita --delivery` используйте ключ `--delivery` для доставки на дом. Для самовывоза не указывайте ключ.

Для выполнения тестов и замера покрытия выполните `python -m pytest --cov .`

Текущее покрытие тестами

```
---------- coverage: platform darwin, python 3.7.7-final-0 -----------
Name            Stmts   Miss  Cover
-----------------------------------
cli.py             31      1    97%
decorators.py       9      0   100%
pizza.py           42      1    98%
test_cli.py        30      0   100%
test_pizza.py      17      0   100%
-----------------------------------
TOTAL             129      2    98%

```