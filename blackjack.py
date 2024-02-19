from game_functions import *

def main():
    player_balance = 25
    while player_balance != 0:
        player_balance = play_round(player_balance)
        clear_console()
        
        play_again = get_play_again(player_balance)

        if not play_again:
            exit()
            
if __name__ == '__main__':
    main()
