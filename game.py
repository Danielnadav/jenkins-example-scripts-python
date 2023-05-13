def difficulty_game():
    while True:
        difficulty_game = input("Please choose a difficulty level to play between 1-5: ")
        try:
            game = int(difficulty_game)
            if game not in range(1, 6):
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 5.")
    
    if game == 1:
        print("Easy mode")
    elif game == 2:
        print("Medium mode")
    elif game == 3:
        print("Hard mode")
    elif game == 4:
        print("Expert mode")
    else:
        print("Master mode")

    difficulty_file = open("/var/tmp/games.txt", "w+")
    difficulty_file.write(str(game) + "\n")
    difficulty_file.close()


difficulty_game()
