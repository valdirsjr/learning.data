def possible_numbers(matrix, x, y):
    numbers = {1,2,3,4,5,6,7,8,9}
    i = j = 0
    pn = []
    #check row
    while i < 9:
        if matrix[x][i] != 0:
            pn.append(matrix[x][i])
        i = i + 1   
    #check column
    while j < 9:
        if matrix[j][y] != 0:
            pn.append(matrix[j][y])
        j = j + 1   
    return list(numbers.difference(set(pn)))

sudoku = [[0,1,0,0,0,9,0,0,8],
          [2,0,7,0,3,0,0,0,0],
          [0,0,4,6,0,2,0,3,0],
          [3,7,8,4,0,0,0,0,9],
          [4,2,9,0,0,0,0,8,1],
          [0,6,1,9,2,8,4,0,0],
          [0,0,6,0,8,4,3,0,7],
          [0,4,0,0,9,0,0,1,0],
          [8,3,0,0,0,0,6,0,4]
         ]

linha = 0
while linha < 9:
    coluna = 0
    while coluna < 9:
        if sudoku[linha][coluna] == 0:
            pn = possible_numbers(sudoku,linha,coluna)
            if len(pn) == 1:
                sudoku[linha][coluna] = pn[0]
        coluna = coluna + 1
    linha = linha + 1

print(sudoku)





print(possible_numbers(sudoku,3,3))

print(sudoku)