# CSCI 127, In-Lab 6

## Logistics

* Due: Thursday, February 22nd no later than 11:59 p.m.
* Partner Information: Complete this assignment individually.
* Submission Instructions: Upload your solution, renamed to **YourFirstName-YourLastName-Lab6.py** to the BrightSpace **Lab 6** Dropbox.
* Deadline Reminder: Once this deadline passes, BrightSpace will no longer accept your Python submission and you will no longer be able to earn credit. Thus, if you are not able to fully complete the assignment, submit whatever you have before the deadline so that partial credit can be earned.

## Learning Outcomes

* Gain experience with files.

## Assignment

* Download the file [broadway.csv][1]. This input file is describe in detail [here][2].
* Download [lab6.py][3] into the same directory where the broadway.csv file is located and rename it according to the instructions in the Logistics section.
* Add the two missing functions so that when the user enters the name of a play (using any combination of uppercase and lowercase letters), the total attendance and total revenue for the play are calculated correctly.

## Sample Run 1


    Please enter the name of a play: hamilton
    Total attendance is 608,917
    Total revenue is $98,459,890


## Sample Run 2


    Please enter the name of a play: HaMILton
    Total attendance is 608,917
    Total revenue is $98,459,890


## Sample Run 3


    Please enter the name of a play: Dr. Zhivago
    Total attendance is 0
    Total revenue is $0


## Grading - 10 points
* 2 points - The calculate_attendance function is correct when the user enters the name of a play using only lowercase letters.
* 2 points - The calculate_attendance function is correct when the user enters the name of a play using any mix of lowercase and uppercase letters.
* 1 point - The calculate_attendance function is of high quality.
* 2 points - The calculate_revenue function is correct when the user enters the name of a play using only lowercase letters.
* 2 points - The calculate_revenue function is correct when the user enters the name of a play using any mix of lowercase and uppercase letters.
* 1 point - The calculate_revenue function is of high quality.

[1]: https://www.cs.montana.edu/paxton/classes/csci127/inlabs/lab6/broadway.csv
[2]: https://think.cs.vt.edu/corgis/csv/broadway/broadway.html
[3]: https://www.cs.montana.edu/paxton/classes/csci127/inlabs/lab6/lab6.py
