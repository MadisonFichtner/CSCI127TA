# Lab 5: Program 2 Enhancement

## Logistics

* Due: Thursday, February 15th no later than 11:59 p.m.
* Partner Information: Complete this assignment individually.
* Submission Instructions: Upload your solution, named **YourFirstName-YourLastName-Lab5.py** to the BrightSpace **Lab 5** Dropbox.
* Deadline Reminder: Once this deadline passes, BrightSpace will no longer accept your Python submission and you will no longer be able to earn credit. Thus, if you are not able to fully complete the assignment, submit whatever you have before the deadline so that partial credit can be earned.

## Learning Outcomes

* To practice understanding and modifying code that someone else wrote.
* A computer scientist is often asked to modify an existing solution. For this lab, you will modify a sample Program 2 solution to work with cribbage hands that contain four cards.

## Assignment

* Download this Program 2 [sample solution][1] and rename it according to the instructions above. Before proceeding, make sure you fully understand the solution.
* **Fifteens** and **sequences** no longer matter. Delete these functions from the sample solution.
* When all four cards have the same suit, this is called a **flush** and scores 4 points. Add the necessary function.
* Modify the **pairs** function to work with four cards.
* Test your program on this [cribbage.txt][2] input file.

## Grading - 10 points
* 2 points - The **flush** function works on all inputs. (All or nothing.)
* 6 points - The **pairs** function works for any number of pairs when the hand contains four cards. (1 point for each incorrect answer up to 5 points.)
* 2 points - The **pairs** function is general. Thus, it could work on a hand with any number of cards. For example, the hand could have five cards, ten cards, one card, or even 100 cards! (All or nothing.)

[1]: https://www.cs.montana.edu/paxton/classes/csci127/inlabs/lab5/cribbage.py
[2]: https://www.cs.montana.edu/paxton/classes/csci127/inlabs/lab5/cribbage.txt
