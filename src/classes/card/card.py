from src.classes.enums.type import Type
from src.classes.entity import Entity
from src.classes.item import Item


class Card:
    def __init__(self, title: str, card_type: Type, entity: Entity = None, item: Item = None):
        self.title = title
        self.type = card_type
        self.entity = entity
        self.item = item

    @property
    def item(self):
        return self.item

    @item.setter
    def item(self, value):
        self.item = value

    @property
    def title(self):
        return self.title

    @title.setter
    def title(self, value):
        self.title = value

    @property
    def type(self):
        return self.type

    @type.setter
    def type(self, value):
        self.type = value

    @property
    def entity(self):
        return self.entity

    @entity.setter
    def entity(self, value):
        self.entity = value
