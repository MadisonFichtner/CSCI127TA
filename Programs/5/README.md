# Program 5: Eight Puzzle

## Logistics

* Due Date: Friday, April 13th no later than 11:59 p.m.
* Partner Information: You may complete this assignment individually or with exactly one partner. If you work with a partner, you **must** both be enrolled in the same lab section or you will both lose 10 points.
* Submission Instructions: Upload your solution, renamed to **YourFirstName-YourLastName-PartnerFirstName-PartnerLastName-Program5.py** to the BrightSpace **Program 5** Dropbox. If you work with a partner, only one person should submit the solution.
* Deadline Reminder: Once the submission deadline passes, BrightSpace will no longer accept your Python submission and you will no longer be able to earn credit. Thus, if you are not able to fully complete the assignment, submit whatever you have before the deadline so that partial credit can be earned.

## Learning Outcomes

* Utilize NumPy arrays to solve a problem.
* Utilize object-oriented programming to solve a problem.

## Eight Puzzle Overview

The [8-puzzle problem][1] is a puzzle invented and popularized by Noyes Palmer Chapman in the 1870s. It is played on a 3-by-3 grid with 8 square blocks labeled 1 through 8 and a blank square. Your goal is to rearrange the blocks so that they are in order. You are permitted to slide the blank square horizontally or vertically. The following shows a sequence of legal moves from an initial board position (left) to the goal position (right).




>
>         1  3        1     3        1  2  3        1  2  3        1  2  3
>      4  2  5   =>   4  2  5   =>   4     5   =>   4  5      =>   4  5  6
>      7  8  6        7  8  6        7  8  6        7  8  6        7  8
>     
>      initial                                                      goal
>     




## Assignment

* Using [program5.py][2] as a starting point, supply the missing functions such that interaction with a user could produce this [transcript][3].
* When the user is asked for input, the legal responses are _left_, _right_, _up_ and _down_ (using any combination of uppercase and lowercase letters).
* The user commands indicate how the blank space such be moved. For example, if the user enters _left_, the blank space should be exchanged with the number that is located to its left. Note: if the blank space is on the far left of the board, it can not be moved to the left.

## Grading - 100 points
* 25 points. The method _is_puzzle_solved_ works correctly (all or nothing).
* 10 points. The method _move_blank_ works correctly when the user enters a legal _left_ move (all or nothing).
* 10 points. The method _move_blank_ works correctly when the user enters a legal _right_ move (all or nothing).
* 10 points. The method _move_blank_ works correctly when the user enters a legal _up_ move (all or nothing).
* 10 points. The method _move_blank_ works correctly when the user enters a legal _down_ move (all or nothing).
* 10 points. The method _move_blank_ works correctly when the user enters an illegal command (all or nothing).
* 10 points. The output format shown in the sample transcript is matched exactly. (5 points for each type of difference up to 10 points.)
* 15 points - The methods you write are properly commented, easy to understand and do not contain unnecessary code. (3 points for each type of improvement up to 15 points.)

[1]: http://en.wikipedia.org/wiki/Fifteen_puzzle
[2]: https://www.cs.montana.edu/paxton/classes/csci127/programs/program5/program5.py
[3]: https://www.cs.montana.edu/paxton/classes/csci127/programs/program5/output.txt
