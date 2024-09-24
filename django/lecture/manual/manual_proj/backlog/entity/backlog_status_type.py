from enum import Enum

class BacklogStatusType(Enum):
    OPEN = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    ARCHIVED = 4

    @classmethod
    def choices(cls):
        return [(key.value, key.name.lower()) for key in cls]
