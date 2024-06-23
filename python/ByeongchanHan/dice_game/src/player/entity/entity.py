import uuid
from dataclasses import dataclass, field


@dataclass
class Player:
    __id: uuid.UUID = field(init=False)
    nickname: str = "UnKnown"

    def __post_init__(self):
        self.__id = uuid.uuid4()

    @property
    def id(self):
        return self.__id
