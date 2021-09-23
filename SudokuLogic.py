class Sudoku:
    def __init__(self):
        self.board = self.CreateBoard()
        self.count = 0
        pass

    @staticmethod
    def CreateBoard():
        li = []
        li.append([3, 9, 0, 0, 5, 0, 0, 0, 0])
        li.append([0, 0, 0, 2, 0, 0, 0, 0, 5])
        li.append([0, 0, 0, 7, 1, 9, 0, 8, 0])
        li.append([0, 5, 0, 0, 6, 8, 0, 0, 0])
        li.append([2, 0, 6, 0, 0, 3, 0, 0, 0])
        li.append([0, 0, 0, 0, 0, 0, 0, 0, 4])
        li.append([5, 0, 0, 0, 0, 0, 0, 0, 0])
        li.append([6, 7, 0, 1, 0, 5, 0, 4, 0])
        li.append([1, 0, 9, 0, 0, 0, 2, 0, 0])
        return li

    def Find_next_Empty(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return row, col

        return None, None

    def PrintBoard(self):
        print("|-------|-------|-------|")
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if j % 3 == 0:
                    print("| ", end="")
                if self.board[i][j] == 0:
                    print(f". ", end="")
                else:
                    print(f"{self.board[i][j]} ", end="")
            print("|")
            if (i+1) % 3 == 0:
                print("|-------|-------|-------|")
        pass

    def isSafe(self, i, j, num):
        if num > 9:
            return False
        # Check if the number is present in row;
        if num in self.board[i]:
            return False
        # Check if number is present in column;
        li = [self.board[t][j] for t in range(0, 9)]
        if num in li:
            return False
        # Check if the number is present in the box.
        i = i//3
        j = j//3
        for t in range(i*3, (i+1)*3):
            li = [self.board[t][k] for k in range(j*3, (j+1)*3)]
            if num in li:
                return False

        return True

    def SolvePuzzle(self):
        self.PrintBoard()
        row, col = self.Find_next_Empty()
        if row is None:
            return True

        for num in range(1, 10):
            if self.isSafe(row, col, num):
                self.board[row][col] = num
                if self.SolvePuzzle():
                    return True
                self.board[row][col] = 0
        return False
