#===============================================================================
# NumbeRand
# Created on Aug 30, 2014
# 
# @author: Ben Pham
#===============================================================================
from game_logic import GameLogic
import display_text


def select_level() -> str:
    ''' Ask user to select level scenario '''
    display_text.display_level_list()
    diff = str(input("Please select a level scenario to play: "))
    
    if diff == '?':
        desc = str(input("Please select a level scenario to acquire descriptions from: "))
        display_text.display_level_description(desc)
        return select_level()
    elif diff in ('1', "add_mult_easy", "level_add_mult_easy"):
        from level_add_mult_easy import return_algorithm
        return return_algorithm()
    elif diff in ('easy_test', 'levelb_easy_test', 'level_easy_test'):
        from levelb_easy_test import return_algorithm
        return return_algorithm()
    else:
        print("\nSorry, this level scenario doesn't exist. Please try again.\n")
        return select_level()



def user_interface() -> None:
    ''' Calls other functions '''
    Main_Game = GameLogic(select_level())
    print("--------------------------------------------------------------------------")
    print("Whenever you need help, input '?' when you are asked for your input.")
    print("--------------------------------------------------------------------------")
    
    while True:
        user_input = input("Pick a number between 0 - 999,999 including 0 and \
999,999 : ")
        
        try:
            if int(user_input) < Main_Game.MIN or int(user_input) > Main_Game.MAX:
                print("INVALID NUMBER!! MUST BE BETWEEN 0 & 999,999!!\n")
            elif Main_Game.check_bound(int(user_input)) == 'LOSE':
                print("The numbers were {}.".format(Main_Game.return_history_as_str()))
                print("You are on level {}.".format(Main_Game.return_level()))
                print("Your bounds are {}".format(Main_Game.return_bound()))
                print("GAME OVER!!")
                break
            elif Main_Game.victory(int(user_input)):
                print("The numbers are {}.".format(Main_Game.return_history_as_str()))
                print("You are on level {}.".format(Main_Game.return_level()))
                print("Your bounds are {}".format(Main_Game.return_bound()))
                print("YOU ARE VICTORIOUS!!")
                break
            else:
                print("{}\n".format(Main_Game.check_bound(int(user_input))))
                Main_Game.next_level()
                print("Level {}. Bound {}.".format(str(int(Main_Game.return_level())), str(int((Main_Game.return_bound())))))
        
        except:
            if user_input == '?':
                display_text.call_help()
            else: 
                print("INVALID COMMAND!\n")
        



if __name__ == '__main__':
    user_interface()
