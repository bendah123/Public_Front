from dataclasses import dataclass
from typing import List
from dataclasses_json import dataclass_json, LetterCase


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class OrderItem():
    inventory_id: int
    count : int

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Order():
    order_id: str
    items : List[OrderItem]