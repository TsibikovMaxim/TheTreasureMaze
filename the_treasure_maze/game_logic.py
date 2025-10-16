import random


def random_event(player):
    """Случайные события с шансом 20%."""
    chance = random.randint(1, 100)
    if chance <= 20:
        print("\nСлучайное событие! Падающий потолок!")
        # Пример: игрок теряет случайный предмет
        if player["inventory"]:
            lost_item = random.choice(player["inventory"])
            player["inventory"].remove(lost_item)
            print(f"Вы случайно уронили {lost_item}!")


def trap_event(player):
    """Ловушки с шансом 10%."""
    chance = random.randint(1, 100)
    if chance <= 10:
        print("\nВы попали в ловушку! Игра окончена.")
        player["game_over"] = True
