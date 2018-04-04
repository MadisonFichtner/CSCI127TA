import numpy as np

class EightPuzzle:

    def __init__(self):
        self.solution = np.array([1,2,3,4,5,6,7,8," "])
        self.solution = self.solution.reshape(3,3)

    def __str__(self):
        separator = "+-+-+-+\n"
        answer = separator
        for row in range(3):
            for col in range(3):
                answer += "|" + str(self.puzzle[row][col])
            answer += "|\n"
            answer += separator
        return answer

    def puzzle_1(self):
        self.puzzle = np.array([1,2,3,4,5,6,7,8," "])
        self.puzzle = self.puzzle.reshape(3,3)
        self.blank_x = 2
        self.blank_y = 2

    def puzzle_2(self):
        self.puzzle = np.array([4,1,3,7,2,5,8," ", 6])
        self.puzzle = self.puzzle.reshape(3,3)
        self.blank_x = 2
        self.blank_y = 1

    def swap_positions(self, x1, y1, x2, y2):
        self.puzzle[x1][y1], self.puzzle[x2][y2] = self.puzzle[x2][y2], self.puzzle[x1][y1]

    def move_blank(self):
        """ move_blank asks the user where to move the blank """
        new_x, new_y = self.get_valid_choice()
        self.swap_positions(self.blank_x, self.blank_y, new_x, new_y)
        self.blank_x, self.blank_y = new_x, new_y

    def get_valid_choice(self):
        """ get_valid_choice prompt the user for a valid direction to move the blank """
        new_x, new_y = self.blank_x, self.blank_y
        valid = False

        while not valid:
            dir = input("Enter choice [up, down, left, right]: ").lower()
            if dir == "right":
                new_y = self.blank_y + 1
            elif dir == "up":
                new_x = self.blank_x - 1
            elif dir == "down":
                new_x = self.blank_x + 1
            elif dir == "left":
                new_y = self.blank_y - 1
            else:
                print("Please enter a valid direction.")
                continue
            valid = True

            if new_x < 0 or new_x > 2 or new_y < 0 or new_y > 2:
                print("That move is invalid.  Please try again.")
                valid = False
        return (new_x, new_y)

    def is_puzzle_solved(self):
        return np.array_equal(self.solution, self.puzzle)

def solve(puzzle):
    steps = 0
    print("Puzzle:\n")
    print(puzzle)
    while not puzzle.is_puzzle_solved():
        puzzle.move_blank()
        print(puzzle)
        steps += 1
    print("Congratulations - you solved the puzzle in", steps, "steps!\n")


def main():
    puzzle = EightPuzzle()
    puzzle.puzzle_1()
    solve(puzzle)
    puzzle.puzzle_2()
    solve(puzzle)

main()
