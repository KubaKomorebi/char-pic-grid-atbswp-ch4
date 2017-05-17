grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def characterPicGrid(grid):
    index = 0
    new_string = grid[index][0]
    while index < 8:
        new_string = new_string + grid[index + 1][0]
        index = index + 1
        if index == 8:
            print(new_string)
            continue
    index1 = 0
    new_string1 = grid[index1][1]
    while index1 < 8:
        new_string1 = new_string1 + grid[index1+1][1]
        index1 = index1 + 1
        if index1 == 8:
            print(new_string1)
            continue
    index2 = 0
    new_string2 = grid[index2][2]
    while index2 < 8:
        new_string2 = new_string2 + grid[index2+1][2]
        index2 = index2 + 1
        if index2 == 8:
            print(new_string2)
            continue
    index3 = 0
    new_string3 = grid[index3][1]
    while index3 < 8:
        new_string3 = new_string3 + grid[index3+1][3]
        index3 = index3 + 1
        if index3 == 8:
            print(new_string3)
            continue
    index4 = 0
    new_string4 = grid[index4][1]
    while index4 < 8:
        new_string4 = new_string4 + grid[index4+1][4]
        index4 = index4 + 1
        if index4 == 8:
            print(new_string4)
            continue
    index5 = 0
    new_string5 = grid[index5][1]
    while index5 < 8:
        new_string5 = new_string5 + grid[index5+1][5]
        index5 = index5 + 1
        if index5 == 8:
            print(new_string5)

characterPicGrid(grid)
