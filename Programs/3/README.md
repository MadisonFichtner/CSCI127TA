# Program 3: Music Library

## Logistics

* Due Date: Thursday, March 2nd no later than 11:59 p.m.
* Partner Information: You may complete this assignment individually or with exactly one partner. If you work with a partner, you **must** both be enrolled in the same lab section or you will both lose 10 points.
* Submission Instructions: Upload your solution, renamed to **YourFirstName-YourLastName-PartnerFirstName-PartnerLastName-Program3.py** to the BrightSpace **Program 3** Dropbox. If you work with a partner, only one person should submit the solution.
* Deadline Reminder: Once the submission deadline passes, BrightSpace will no longer accept your Python submission and you will no longer be able to earn credit. Thus, if you are not able to fully complete the assignment, submit whatever you have before the deadline so that partial credit can be earned.

## Learning Outcomes

* To solve this problem, you need to understand the following Python concept: files.

## Background Information

## Assignment

* Using [music.py][1] (renamed according to the instructions above) as a starting point, supply the missing functions such that interaction with a user could produce this [sample transcript][2].
* The function **longest_song** should find the song with the longest _duration_ and print out its title and running time, rounded to the nearest second. Match the output format in the sample transcript.
* The function **songs_by_year** is passed a year (e.g. 2010) that the user supplies. The function identifies and prints the number of songs in the Music CSV Library that were produced in that _year_. Match the output format in the sample transcript.
* The function **all_songs_by_artist** is passed an artist (e.g. Nine Inch Nails) that the user supplies using any combination of uppercase and lowercase letters. The function finds and prints in sorted order each song in the Music CSV Library by the _artist.name_. Match the output format in the sample transcript.
* Study the Music CSV Library and develop a function of your own that corresponds to menu option 4. The function should be interesting, non-trivial and not a simple variation of one of the other 3 functions. Modify the **menu** and **main** functions as appropriate.

## Grading - 100 points
* 15 points. The function **longest_song** is correct. (All or nothing.)
* 15 points. The function **songs_by_year** is correct. (5 points for each failed test case up to 15 points.)
* 20 points. The function **all_songs_by_artist** is correct. (5 points for each failed test case up to 15 points. 5 points for printing the songs in alphabetical order.)
* 20 points. The function you choose is correct (5 points), non-trivial (5 points) and not a simple variation of one of the other three functions (10 points).
* 15 points. The output for the required three functions matches the output format of the sample transcript. The output for your function looks good and is easily understandable. (3 points for each type of improvement up to 15 points.)
* 15 points - The Python solution is properly commented, easy to understand and does not contain unnecessary code. (3 points for each type of improvement up to 15 points.)

[1]: https://www.cs.montana.edu/paxton/classes/csci127/programs/program3/music.py
[2]: https://www.cs.montana.edu/paxton/classes/csci127/programs/program3/transcript.txt
