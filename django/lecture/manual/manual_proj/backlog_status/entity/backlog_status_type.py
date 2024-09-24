from enum import Enum

class BacklogStatusType(Enum):
    BACKLOG = 1
    SPRINT_TERM = 2
    IN_PROGRESS = 3
    REVIEW = 4
    COMPLETED = 5
    ADDITIONAL_WORK = 6
    ARCHIVED = 7

    @classmethod
    def choices(cls):
        return [(key.value, key.name.lower()) for key in cls]
