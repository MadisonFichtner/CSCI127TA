# In-Lab 3: Strings, Iteration and Recursion

## Logistics

* Due: Thursday, February 1st no later than 11:59 p.m.
* Partner Information: Complete this assignment individually.
* Submission Instructions: Upload your solution, renamed to **YourFirstName-YourLastName-Lab3.py** to the BrightSpace **Lab 3** Dropbox.
* Deadline Reminder: Once this deadline passes, BrightSpace will no longer accept your Python submission and you will no longer be able to earn credit. Thus, if you are not able to fully complete the assignment, submit whatever you have before the deadline so that partial credit can be earned.

## Learning Outcomes

* Gain experience manipulating strings.
* Gain experience solving a problem using iteration.
* Gain experience solving a problem using recursion.

## Assignment

* Download [lab3.py][1]
* Rewrite the body of the **remove_builtin** function such that it removes all white space from the original sentence using the built-in [replace][2] method. For example, if the sentence is " Hi There ", the function should return "HiThere".
* Rewrite the body of the **remove_iterative** function such that it removes all white space from the original sentence using a loop. (Do not use the built-in replace method.)
* Rewrite the body of the **remove_recursive** function such that it removes all white space from the original sentence using recursion. (Do not use the built-in replace method.)

## Grading - 10 points
* 3 points - The remove_builtin function is implemented correctly.
* 3 points - The remove_iterative function is implemented correctly.
* 4 points - The base case (2 points) and two general cases (1 point each) of the remove_recursive function are implemented correctly.

[1]: https://www.cs.montana.edu/paxton/classes/csci127/inlabs/lab3/
[2]: https://docs.python.org/3/library/stdtypes.html?highlight=isdigit#str.replace
