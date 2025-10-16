from the_treasure_maze.constants import ROOMS, ITEMS, PUZZLES
from the_treasure_maze.utils import print_room_description, print_inventory


def move(player, direction):
    current = player["location"]
    if direction in ROOMS[current]["exits"]:
        player["location"] = ROOMS[current]["exits"][direction]
        print_room_description(player["location"], ROOMS)
        return True
    print("Нельзя идти в этом направлении.")
    return False


def look(player):
    print_room_description(player["location"], ROOMS)


def inventory(player):
    print_inventory(player["inventory"])


def take(player, item_name):
    for item, data in ITEMS.items():
        if item == item_name and data["location"] == player["location"]:
            player["inventory"].append(item)
            data["location"] = "player"
            print(f"Вы подняли {item}.")
            return True
    print(f"{item_name} здесь нет.")
    return False


def use(player, item_name):
    if item_name in player["inventory"]:
        print(f"Вы используете {item_name}.")
        # Простейший пример использования ключа для сокровищ
        if item_name == "key" and player["location"] == "treasure_room":
            player["has_key"] = True
            print("Вы открыли сундук с сокровищами!")
        return True
    print(f"У вас нет {item_name}.")
    return False


def solve(player):
    room = player["location"]
    if room in PUZZLES:
        answer = input(PUZZLES[room]["question"] + " ")
        if answer.strip() == PUZZLES[room]["answer"]:
            player["puzzle_solved"] = True
            print("Загадка решена! Вы можете забрать сокровище.")
            return True
        print("Неверный ответ.")
        return False
    print("В этой комнате нет загадки.")
    return False


def game_loop():
    """Основной цикл игры."""
    player = {
        "location": "hall",
        "inventory": [],
        "has_key": False,
        "puzzle_solved": False,
        "game_over": False
    }

    print_room_description(player["location"], ROOMS)

    while not player["game_over"]:
        command = input(
            "\nКоманда (look/move/inventory/take/use/solve/quit): "
        ).strip().lower()

        if command == "quit":
            print("Вы вышли из игры.")
            player["game_over"] = True
        elif command == "look":
            look(player)
        elif command == "inventory":
            inventory(player)
        elif command.startswith("move"):
            parts = command.split(maxsplit=1)
            if len(parts) == 2:
                _, direction = parts
                move(player, direction)
            else:
                print("Укажите направление: move north/south/east/west")
        elif command.startswith("take"):
            parts = command.split(maxsplit=1)
            if len(parts) == 2:
                _, item = parts
                take(player, item)
            else:
                print("Укажите предмет, который хотите взять: take <item>")
        elif command.startswith("use"):
            parts = command.split(maxsplit=1)
            if len(parts) == 2:
                _, item = parts
                use(player, item)
            else:
                print("Укажите предмет, который хотите использовать: use <item>")
        elif command == "solve":
            solve(player)
        else:
            print("Неизвестная команда.")

        # Проверка победы
        if (
                player["location"] == "treasure_room" and
                player["has_key"] and
                player["puzzle_solved"]
        ):
            print("\nПоздравляем! Вы нашли сокровище и победили!")
            player["game_over"] = True
# python -m the_treasure_maze.main