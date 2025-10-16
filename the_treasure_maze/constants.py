ROOMS = {
    "hall": {
        "description": "Большой зал с порталом",
        "exits": {"north": "treasure_room"}
    },
    "treasure_room": {
        "description": "Комната с сокровищами",
        "exits": {"south": "hall"}
    },
}

ITEMS = {
    "key": {
        "description": "Золотой ключ",
        "location": "hall"
    },
    "treasure": {
        "description": "Сундук с сокровищами",
        "location": "treasure_room"
    },
}

COMMANDS = ["look", "inventory", "move", "take", "use", "solve", "quit"]

PUZZLES = {
    "treasure_room": {
        "question": "Сколько будет 2+2?", "answer": "4"
    }
}