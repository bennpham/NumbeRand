NumbeRand
=========

A number guessing game I created in Python. The numbers are 0-999,999. There are 21 levels.



How to Run
-----------
To run the application, double click numberand.py or run it a Python IDE. 


How to Play
------------
First select a level/scenario to play by inputting the name of the level or the associated number.
If you need a description of what type of algorithms are used for each level, input '?' instead.
  - If you input '?' type the name of the number associated with the level for descriptions.
  - If you do not want to see any level description, just input anything at this stage.
  
After you select a level, input a number from 0-999,999 (including 0 or 999,999).
If you need any help about the rules, you can input '?' instead.

The first number you pick will always be correct, but the first number is random.
You will see a respond that tells you "EXACT","VERY HOT", "HOT", "WARMER", "WARM" "OK"
  - "EXACT"     you got the exact number
  - "VERY HOT"  1% in range of correct number
  - "HOT"       5% in range of correct number
  - "WARMER"    10% in range of correct number
  - "WARM"      25% in range of correct number
  - "OK"        in range of correct number (but not out of range and not better than 25%)
  
The responses can help you guess how close you are to the correct number, but the number will change each round as it
goes through an algorithm. You can try to use these feedbacks to help you guess the algorithm.

The range of how close you must be to the number each round will also be cut in half each round. Round 1 does not start
until you pick the first number. Round 1 start at 500,000 range, while round 2 is 250,000 range. If your number is
greater or lesser by the exact number plus or minus the range, you lose the game.


Versions
----------
0.04 - first release alpha
