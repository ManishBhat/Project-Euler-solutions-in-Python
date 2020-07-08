# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 09:02:21 2020

@author: Manish
"""
from sudoku import Board


def main():
    input_file = 'p096_sudoku.txt'
    output_file = 'output_files.txt'
    
    input_fhand = open(input_file, 'r')
    output_fhand = open(output_file, 'w')
    
    lines = input_fhand.readlines()
    lines = [line.strip('\n') for line in lines if line[:4]!= 'Grid']
    
    ind = 0
    grid_num = 1
    project_euler_output = 0
    while True:
        if ind >= len(lines):
            break
        sudoku_puzzle = lines[ind: ind + 9]
        #print(sudoku_puzzle[1][1], end = ' ')
        board = Board()
        for c in range(9):
            for r in range(9):
                board.board[c][r].number = int(sudoku_puzzle[c][r]) 
        board.solve()
        output_fhand.write("Grid " + "{:02d}".format(grid_num) + "\n")
        output_fhand.write(str(board))
        proj_euler_list = [board.board[0][0].number, board.board[0][1].number,\
                           board.board[0][2].number]
        project_euler_output += int(''.join(str(e) for e in proj_euler_list))
        
        grid_num += 1
        ind += 9
    print(project_euler_output)
if __name__ == '__main__':
    import time
    start_time = time.time()
    main()
    print("Program run time(in s): ", (time.time() - start_time))  
    