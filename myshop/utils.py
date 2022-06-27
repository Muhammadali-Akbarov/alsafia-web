
from re import I, M


def getCategoryid(mystr: str) -> int:
    id = ""
    for item in mystr:
        if item.isdigit():
            id += item
    
    return id