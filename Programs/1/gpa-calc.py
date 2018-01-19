# define the grade: value pairings
grade = {"A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7, "C+": 2.3, "C": 2.0, "C-": 1.7, "D+": 1.3, "D": 1.0, "F": 0.0}

n = int(input("Enter the number of courses you are taking: ")) # prompt the user for number of courses
print()

# initialize the total grade and credit values
gtot = 0
ctot = 0

# prompt for input of each course, add the info to the totals
for i in range(n):
    g = grade[input("Enter grade for course " + str(i + 1) + ": ").upper()]
    c = int(input("Enter credits for course " + str(i + 1) + ": "))
    print() # add newline to output, breaking up inputs
    gtot += g * c
    ctot += c

print("Your GPA is %.2f" % (gtot / ctot))
