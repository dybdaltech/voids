

from asyncio.format_helpers import _format_callback_source
from dataclasses import dataclass
from enum import Enum

class Forms(Enum):
    RECTANGLE = 0
    IMAGE = 1
    TEXT = 2

class FormColor(Enum):
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    GREEN = (0,255, 0)
    WHITE = (255, 255, 255)

@dataclass
class Form:
    FormType: Forms
    FormColor: FormColor


@dataclass
class Rectangle(Form):
    width: int
    height: int

    def area(self) -> int:
        return self.width * self.height

@dataclass
class TextForm(Form):
    text: str