# Program 2: Three Card Cribbage

## Logistics

* Due Date: Friday, February 9th no later than 11:59 p.m.
* Partner Information: You may complete this assignment individually or with exactly one partner. If you work with a partner, you **must** both be enrolled in the same lab section or you will both lose 10 points.
* Submission Instructions: Upload your solution, renamed to **YourFirstName-YourLastName-PartnerFirstName-PartnerLastName-Program2.py** to the BrightSpace **Program 2** Dropbox. If you work with a partner, only one person should submit the solution. To make the recording of grades easier, write both names in the BrightSpace Dropbox comment box.
* Deadline Reminder: Once the submission deadline passes, BrightSpace will no longer accept your Python submission and you will no longer be able to earn credit. Thus, if you are not able to fully complete the assignment, submit whatever you have before the deadline so that partial credit can be earned.

## Learning Outcomes

* To solve this problem, you need to understand the following new Python concept: lists.

## Simplified Three Card Cribbage Scoring

* A hand consists of three different cards. Each card contains a numeric value that ranges from 1 to 10 and a suit where the possible values are "clubs", "diamonds", "hearts" or "spades".
* If all three cards contain the same numeric value, that is a called a **three of a kind** and is worth 6 points.
* If two of the three cards contain the same numeric value (but the third card contains a different value), that is called a **pair** and is worth 2 points.
* If the three cards contain three consecutive numeric values (in any order), that is called a **sequence** and is worth 3 points.
* For each unique combination of cards that adds up to 15, that is called a **fifteen** and is worth 2 points for each fifteen.
* The value of a hand is the sum of anything that scores points. For example, a hand consisting of the 4 of hearts, 6 of diamonds and 5 of hearts is worth 5 points (3 for the sequence, 2 for the fifteen).

## Assignment
* Download cribbage.py and modify it so that when it is run on [this input file](https://www.cs.montana.edu/paxton/classes/csci127/programs/program2/cribbage.txt), it produces [this output file](https://www.cs.montana.edu/paxton/classes/csci127/programs/program2/output.txt). Note: the input file (cribbage.txt) should be located in the same directory as the python program.

## Input File Information

* We will study files later this semester.
* The input file contains an unknown number of cribbage hands. Each line contains a three card cribbage hand in this format: **Card 1 Value, Card 1 Suit, Card 2 Value, Card 2 Suit, Card 3 Value, Card 3 Suit**.
* All cribbage hands are valid.
* Note: Your program might be tested on a different set of cribbage hands so it is important to make your solution as general as possible.

## Grading - 100 points
* 10 points - Every **three of a kind** is identified correctly. (All or nothing.)
* 15 points - Every **pair** is identified correctly. (5 points for each incorrect answer up to 15 points.)
* 15 points - Every **sequence** is identified correctly. (5 points for each incorrect answer up to 15 points.)
* 15 points - Every **fifteen** is identified correctly. (5 points for each incorrect answer up to 15 points.)
* 10 point - Every hand that scores in multiple ways (e.g. a hand that scores both a fifteen and three of a kind) is scored correctly. (5 points for each incorrect answer up to 10 points.)
* 10 points - A separate function is used to determine each different type of scoring (e.g. **three of a kind**). (3 points for each missing function up to 10 points.)
* 10 points - The format of your output matches the format of the sample output exactly. (2 points for each type of difference up to 10 points.)
* 15 points - The Python solution is properly commented, easy to understand and does not contain unnecessary code. (3 points for each type of improvement up to 15 points.)
