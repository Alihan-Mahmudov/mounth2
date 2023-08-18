from logic import check_win


def play_game():

    from  decouple import config
    initial_money = int(config('MY_MONEY', default=1000))


    while initial_money > 0:
        print(f"Ваш текущий капитал: {initial_money}")
        bet = int(input("Сделайте ставку: "))

        if bet > initial_money:
            print("Вы не можете поставить больше, чем у вас есть.")
            continue

        result, winnings = check_win()
        if result:
            print(f"Поздравляем! Вы выиграли {winnings}$!")
            initial_money += winnings
        else:
            print(f"К сожалению, вы проиграли {bet}$.")
            initial_money -= bet

        choice = input("Хотите сыграть еще? (да/нет): ")
        if choice.lower() != "да":
            break

    print("Игра окончена. Ваш итоговый капитал:", initial_money)


if __name__ == "__main__":
    play_game()