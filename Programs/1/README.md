# CSCI 127, Program 1

## Logistics

* Due Date: Friday, January 26th no later than 11:59 p.m.
* Partner Information: You may complete this assignment individually or with exactly one partner. If you work with a partner, you **must** both be enrolled in the same lab section or you will both lose 10 points.
* Submission Instructions: Upload your solution, entitled **YourFirstName-YourLastName-PartnerFirstName-PartnerLastName-Program1.py** to the BrightSpace **Program 1** Dropbox. If you work with a partner, only one person should submit the solution. However, to make the recording of grades easier, write both names in the BrightSpace Dropbox comment box.
* Deadline Reminder: Once the submission deadline passes, BrightSpace will no longer accept your Python submission and you will no longer be able to earn credit. Thus, if you are not able to fully complete the assignment, submit whatever you have before the deadline so that partial credit can be earned.

## Learning Outcomes

* To solve this problem, you need to understand the following Python concepts: data types, functions, selection statements and iteration.

## Background Information

* At Montana State University, the following grades have the following values: A (4.0), A- (3.7), B+ (3.3), B (3.0), B- (2.7), C+ (2.3), C (2.0), C- (1.7), D+ (1.3), D (1.0) and F (0.0).
* Example GPA Calculation: If a student earns an A in a 3 credit course and a B- in a 2 credit course, that student's GPA can be calculated as (4.0 * 3 + 2.7 * 2) / (3 + 2).

## Assignment

* Write a Python program that prompts the user for the number of classes taken and then for each class, the letter grade received (e.g. B+) and the number of credits (e.g. 3). Once this information is known, the program should calculate and display the GPA.
* Here is a [sample transcript][1]. Your solution should match the output format exactly.

## Assumptions

* The user will take at least one and no more than seven courses.
* Each course has a credit value between one and five (inclusive).
* A grade can be entered in uppercase or lowercase. For example, either A- or a-.
* All user inputs will be valid.

## Grading - 100 points
* 35 points - The GPA calculation is correct.
* 15 points - The user is prompted to enter the number of courses (5 points), the letter grade for each course (5 points) and the credits for each course (5 points).
* 10 points - With the exception of the GPA, the output format matches the output format of the transcript exactly (2 points for each type of difference up to 10 points).
* 5 points - The GPA is displayed with two digits to the right of the decimal.
* 10 points - A function named **translate** is defined that takes a letter grade (e.g. b- or B-) and correctly returns its value (e.g. 2.7).
* 10 points - A function named **main** is defined (5 points). The only python statement that does not appear in this function or the translate function is the call to the main function, e.g. **main()** (5 points).
* 10 points - The Python solution is easy to understand and does not contain unnecessary code (2 points for each type of improvement up to 10 points).
* 5 points - An appropriate Python comment appears at the top of the submission. See below for the type of information that should appear.

## Sample Python Header Comment


    # ---------------------------------------
    # CSCI 127, Joy and Beauty of Data
    # Program 1: GPA Calculator
    # Your Name(, Your Partner's Name)
    # Last Modified: January ??, 2018
    # ---------------------------------------
    # A brief overview of the program.
    # ---------------------------------------


## Helpful Hint

* To learn more about formatted output, take a look at [this page][2]. Use Python's new style for formatted output.

[1]: https://www.cs.montana.edu/transcript.out
[2]: https://pyformat.info/
