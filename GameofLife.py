import os
import time

class GameOfLife:

    def __init__(self, x, y):
        self._grid = []
        self._x = x
        self._y = y
        for i in range(x):
            self._grid.append([])
            for j in range(y):
                self._grid[i].append("-")

    def toggle_pos(self, x, y):
        if self._grid[x][y] == "-":
            self._grid[x][y] = "O"
        elif self._grid[x][y] == "O":
            self._grid[x][y] = "-"

    def run_it(self):
        temp_grid = GameOfLife(self._x, self._y)
        for i in range(self._x):
            for j in range(self._y):
                temp_grid._grid[i][j] = self._grid[i][j]
                count = self.neighbor_count(i, j)
                if self._grid[i][j] == "O":
                    if count < 2:
                        temp_grid.toggle_pos(i, j)
                    elif count > 3:
                        temp_grid.toggle_pos(i, j)
                else:
                    if count == 3:
                        temp_grid.toggle_pos(i, j)
        self._grid = temp_grid._grid
        print (self)

    def neighbor_count(self, x, y):
        count = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if not (i == x and j == y):
                    if i < 0:
                        i = self._x - 1
                    elif i > self._x - 1:
                        i = 0
                    if j < 0:
                        j = self._y - 1
                    elif j > self._y - 1:
                        j = 0
                    if self._grid[i][j] == "O":
                        count += 1
        return count

    def __str__(self):
        grid = ""
        for i in range(len(self._grid)):
            for j in range(len(self._grid[i])):
                grid += self._grid[i][j] + " "
            grid += "\n"
        return grid

def main():
    file = open("p.txt")
    file = file.read().split("\n")
    grid = GameOfLife(int(file[0].split(",")[0]), int(file[0].split(",")[1]))
    for coordinate in file[1:]:
        if coordinate != "":
            coordinate = coordinate.split(",")
            grid.toggle_pos(int(coordinate[0]), int(coordinate[1]))
    num = int(input("How many times do you want to iterate: "))
    os.system("cls")
    print (grid)
    time.sleep(.1)
    os.system("cls")
    for i in range(num):
        grid.run_it()
        time.sleep(.1)
        os.system("cls")

main()
