# CSCI 127, In-Lab 7

## Logistics

* Due: Thursday, March 1st no later than 11:59 p.m..
* Partner Information: Complete this assignment individually.
* Submission Instructions: Upload your solution, renamed to **YourFirstName-YourLastName-Lab7.py** to the BrightSpace **Lab 7** Dropbox.
* Deadline Reminder: Once this deadline passes, BrightSpace will no longer accept your Python submission and you will no longer be able to earn credit. Thus, if you are not able to fully complete the assignment, submit whatever you have before the deadline so that partial credit can be earned.

## Learning Outcome

* Gain experience with dictionaries.

## Preliminaries

* Matrices can be used to represent and manipulate computer graphics objects. In this assignment, we will represent matrices using sparse dictionaries by recording only non-zero values.
* Learn how matrix subtraction works by reading [this information][1].
* Download input file [sparse-matrix.txt][2]. The first line in the file contains the number of rows and columns for two integer matrices. Until the word **stop** is encountered, the next lines provide information about non-zero entries in the first matrix. The first integer on the line is the row number, the second integer is the column number and the third integer is the contents of that matrix entry. Once information about the first matrix is known, information about the second matrix is provided using the same format.
* Download [lab7.py][3], rename it according to the instructions above, and make sure you understand it.

## Assignment

* Take the program above and modify it by adding the two missing functions. When the program is run on the output file above, it should produce [this output][4].

## Helpful Hint

## Grading - 10 points
* 4 points - Your program's output matches the output format of the transcript above (1 point for each type of difference up to 4 points).
* 1 point - The print_matrix function uses the print_header function correctly.
* 3 points - Matrix subtraction is performed correctly (all or nothing).
* 2 points - Zeros do not appear in matrix_3.

## If Time Remains

* Work on Program 3, seeking feedback as necessary.

[1]: http://stattrek.com/matrix-algebra/matrix-addition.aspx
[2]: https://www.cs.montana.edu/paxton/classes/csci127/inlabs/lab7/sparse-matrix.txt
[3]: https://www.cs.montana.edu/paxton/classes/csci127/inlabs/lab7/lab7.py
[4]: https://www.cs.montana.edu/paxton/classes/csci127/inlabs/lab7/output.txt
