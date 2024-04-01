# Miner
import random


class Cell:
    def __init__(self, has_mine=False):
        self.has_mine = has_mine
        self.is_revealed = False

    def __str__(self):
        if self.is_revealed:
            if self.has_mine:
                return '*'
            else:
                return ' '
        else:
            return 'X'


class Game:
    def __init__(self, width, height, num_mines):
        self.width = width
        self.height = height
        self.num_mines = num_mines
        self.board = [[Cell() for _ in range(width)] for _ in range(height)]
        self.plant_mines()

    def plant_mines(self):
        mines_planted = 0
        while mines_planted < self.num_mines:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if not self.board[y][x].has_mine:
                self.board[y][x].has_mine = True
                mines_planted += 1

    def reveal_cell(self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            print("Invalid cell coordinates")
            return
        cell = self.board[y][x]
        if cell.is_revealed:
            print("Cell already revealed")
            return
        cell.is_revealed = True
        if cell.has_mine:
            print("Game over! You hit a mine.")
        else:
            print("No mine here. Keep going.")

    def print_board(self):
        for row in self.board:
            print(' '.join(str(cell) for cell in row))


# Пример использования:

game = Game(5, 5, 5)  # Создаем игру с размером поля 5x5 и 5 минами
game.print_board()  # Выводим начальное состояние поля
game.reveal_cell(2, 2)  # Раскрываем клетку в координатах (2, 2)
game.print_board()  # Выводим обновленное состояние поля


def count_mines_around(self, x, y):
    count = 0
    for i in range(max(0, x - 1), min(self.width, x + 2)):
        for j in range(max(0, y - 1), min(self.height, y + 2)):
            if self.board[i][j].has_mine:
                count += 1
    return count


def print_board_with_mines_count(self):
    for i in range(self.width):
        for j in range(self.height):
            if self.board[i][j].is_revealed:
                if self.board[i][j].has_mine:
                    print("*", end=" ")
                else:
                    mines_around = self.count_mines_around(i, j)
                    print(mines_around, end=" ")
            else:
                print("-", end=" ")
        print()