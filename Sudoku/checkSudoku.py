from checkCuadrado import checkCuadrado
from checkNumerosValidos import checkNumerosValidos
from checkFilas import checkFilas
from checkColumnas import checkColumnas
import casosTest


def check_sudoku(sudoku):
    return checkCuadrado(sudoku) and checkNumerosValidos(sudoku) and checkFilas(sudoku) and checkColumnas(sudoku)

if __name__ == '__main__':
    for attr in sorted(casosTest.__dict__):
        if attr.startswith('__'):
            pass
        else:
            print(attr, " => ", check_sudoku(casosTest.__dict__[attr]))