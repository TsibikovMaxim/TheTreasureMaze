from the_treasure_maze.constants import COMMANDS


def get_player_input():
    """Запрашивает команду игрока и проверяет её."""
    command = input("\nВведите команду: ").strip().lower()
    if command in COMMANDS:
        return command
    print("Неизвестная команда. Попробуйте ещё раз.")
    return None


def print_room_description(room, ROOMS):
    """Выводит описание комнаты и доступные выходы."""
    print(f"\nВы находитесь в комнате: {room}")
    print(ROOMS[room]["description"])
    exits = ', '.join(ROOMS[room]["exits"].keys())
    print(f"Доступные выходы: {exits}")


def print_inventory(inventory):
    """Выводит предметы в инвентаре игрока."""
    if not inventory:
        print("Ваш инвентарь пуст.")
    else:
        print("Инвентарь:", ', '.join(inventory))
