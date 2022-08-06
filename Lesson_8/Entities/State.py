from enum import Enum


class State(Enum):
    New = 0,
    Preority_1 = 1,
    Preority_2 = 2,
    Preority_3 = 3,
    Preority_4 = 4,
    Preority_5 = 5,
    Delete = 6,
    Wait = 7,
    Done = 8,
