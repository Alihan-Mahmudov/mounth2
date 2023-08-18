from random import randint

def check_win():
    winning_slot = randint(1, 30)
    chosen_slot = int(input("Выберите слот (1-30): "))

    if chosen_slot == winning_slot:
        return True, 2 * chosen_slot
    else:
        return False, 0