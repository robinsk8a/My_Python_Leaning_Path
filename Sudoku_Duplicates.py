"""This is a CodeWars challenge which main objective is to find if a sudoku matrix is answered correctly or if there is any repeated number either in the rows or in 
the column. 
This exercise was broken on the page, labeling the board matrix as "Try again" answer, so I checked on it to verify if the code was wrong, after comparing with a 
know repeated matrix base on the original and even make a heat map for each, I'm pretty sure that the code is working well... but there is always gap for mistakes 
so if you found some error, please let me know.
 """


import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
def duplicate_row(arr):
    is_duplcate = True
    if type(arr) is not list:
        arr = arr.tolist()
    for row in arr:
        x= 0
        x = x + 1
        #print(row)
        
        #print(sorted(row))
        
        for num in row:
            #print(num)
            #print(row.count(num))
            if row.count(num) > 1:
                #print(False)
                is_duplcate = False

    return is_duplcate
    
def duplicate_colm(arr):
    #print("colms")
    colums = np.transpose(arr)
    return duplicate_row(colums)
        


def done_or_not(board): #board[i][j]
    #print(np.shape(board))
    if duplicate_row(board) is True and duplicate_colm(board) is True:
        return "Finished"
    else:
        return "Try again!"
    
    

board = [[1, 2, 3, 4, 5, 6, 7, 8, 9], 
         [2, 3, 4, 5, 6, 7, 8, 9, 1], 
         [3, 4, 5, 6, 7, 8, 9, 1, 2], 
         [4, 5, 6, 7, 8, 9, 1, 2, 3], 
         [5, 6, 7, 8, 9, 1, 2, 3, 4], 
         [6, 7, 8, 9, 1, 2, 3, 4, 5], 
         [7, 8, 9, 1, 2, 3, 4, 5, 6], 
         [8, 9, 1, 2, 3, 4, 5, 6, 7], 
         [9, 1, 2, 3, 4, 5, 6, 7, 8]]
board_rep = [[2, 1, 3, 4, 5, 6, 7, 8, 9], 
         [2, 3, 4, 5, 6, 7, 8, 9, 1], 
         [3, 4, 5, 6, 7, 8, 9, 1, 2], 
         [4, 5, 6, 7, 8, 9, 1, 2, 3], 
         [5, 6, 7, 8, 9, 1, 2, 3, 4], 
         [6, 7, 8, 9, 1, 2, 3, 4, 5], 
         [7, 8, 9, 1, 2, 3, 4, 5, 6], 
         [8, 9, 1, 2, 3, 4, 5, 6, 7], 
         [9, 1, 2, 3, 4, 5, 6, 7, 8]]

print(done_or_not(board))
print(done_or_not(board_rep))


fig, (ax1, ax2) =plt.subplots(1,2)

sns.heatmap(board, ax= ax1, annot=True,cmap='Blues', fmt='g')
sns.heatmap(board_rep, ax= ax2, annot=True,cmap='Blues', fmt='g')

plt.show()
