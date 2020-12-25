class BasePizza:
    """
    Базовый класс для создания пиццы.
    Имеет список базовых ингридиентов в виде рецепта с граммовкой.
    Так же имеет возможность задавать размер пиццы с контролем значения задаваемого параметра.
    Имеет вывод словаря ингредиентов через метод dict()
    """

    _size = None

    def __init__(self, size="L"):
        self.size = size
        self._ingredients = {"tomato sauce": 100, "mozzarella": 150}

    @property
    def size(self) -> str:
        return self._size

    @size.setter
    def size(self, val: str) -> None:
        if val in ("L", "XL"):
            self._size = val
        else:
            raise ValueError("Pizza size must be 'L' or 'XL'")

    def get_params(self) -> tuple:
        return self._size, self._ingredients

    def dict(self) -> dict:
        return self._ingredients

    def __hash__(self) -> int:
        return hash(self.get_params())

    def __eq__(self, other) -> bool:
        if isinstance(other, BasePizza):
            return self.get_params() == other.get_params()
        raise TypeError("Неверный тип второго значения")

    def __repr__(self) -> str:
        return self.__class__.__name__


class EmojiMixin:
    """
    Миксин для добавления эмодзи к названию пиццы
    """

    def __repr__(self):
        repr_str = super().__repr__()
        repr2emoji = {"Margherita": " 🧀", "Pepperoni": " 🍕", "Hawaiian": " 🍍"}
        return repr_str + repr2emoji.get(repr_str, "")


class Margherita(EmojiMixin, BasePizza):
    """Класс пиццы Маргарита"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._ingredients.update({"tomatoes": 300})


class Pepperoni(EmojiMixin, BasePizza):
    """Класс пиццы Пепперони"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._ingredients.update({"pepperoni": 250})


class Hawaiian(EmojiMixin, BasePizza):
    """Класс пиццы Гавайской"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._ingredients.update({"chicken": 200, "pineapples": 150})
