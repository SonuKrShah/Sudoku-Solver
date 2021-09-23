from SudokuLogic import Sudoku

if __name__ == "__main__":
    Game = Sudoku()
    Game.PrintBoard()
    temp = Game.SolvePuzzle()

    if not temp:
        print("Not Solvable")
    print()
    print()
    Game.PrintBoard()
