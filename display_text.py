def call_help() -> None:
    print("------------------------------------------------------------------",
          "                    How to play NumbeRand",
          "------------------------------------------------------------------",
          "Basically, pick a number between 0 and 999,999.",
          "This include 0 and 999,999",
          "The first pick is always right.", 
          "Your first pick is always a random number as well",
          "The round doesn't officially start until you pick a number.",
          "Your first pick starting bound is basically 1,000,000.",
          "Your second pick is level 1 and bound is now 500,000",
          "As you continuously progress, the bound decrease by half.",
          "There are 21 levels total.",
          "The bound is pretty much there to tell you the following:",
          "    - For the exact number you must pick, add and subtract the bound from that \
number. You will get two numbers.",
          "    - If you pick a number that is between those two numbers, you proceed \
to the next round.",
"You will also get a message every time you input a valid number.",
"The following below are the messages and what they mean:",
"    - EXACT :   You pick exact number",
"    - VERY HOT: You are 1% away from exact number",
"    - HOT:      You are 5% away from exact number",
"    - WARMER:   You are 10% away from exact number",
"    - WARM:     You are 25% away from exact number",
"    - OK:       You are 26%-99% away from exact number",
"This is how the game works: ",
"    - In the beginning, a random number and algorithm are chosen",
"    - As the game progress, the number will continuously go through the algorithm",
"    - The only thing random between in picking the number is what algorithm is being used",
"    - Depending on the difficulty you pick, you may get easier or harder algorithms",
"    - Basically, there is a pattern in the number that it goes through, although finding \
the pattern is the hard part as it continuously cycle through the algorithm and change.",
"    - Using the messages mentioned above might help you follow the pattern if you \
happen to keep notes of the changes on a notepad.",
"------------------------------------------------------------------",
"", sep='\n')
    
    
def display_level_list():
    print("Please select the following level scenario from the list below to play.",
          "To get a description of what type of algorithms are in each level scenario, input '?'.", 
            "    - 1: add_mult_easy", 
            "BONUS",
            "    - easy_test", sep='\n')
    
    
def display_level_description(level: str):
    ''' Depending on the parameter, prints description for level description '''
    if level in ('1', "add_mult_easy", "level_add_mult_easy"):
        print("2 possible algorithms where x is the number going through the algorithms", 
              "    - x + y", "        - y is [-5,5]",
              "    - x * y", "        - y is [0,5]",sep='\n')
    elif level in ('easy_test', 'levelb_easy_test', 'level_easy_test'):
        print("2 possible algorithms where x is the number going through the algorithms",
              "     - x*0 + y", "             - y is [0,1]",
              "     - x/y", "             - y is [2,4]", sep='\n')
    else:
        print("INVALID LEVEL SCENARIO. Exiting description...")
