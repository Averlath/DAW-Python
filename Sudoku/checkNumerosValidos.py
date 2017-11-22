import casosTest

def sonNumerosEnteros(sudoku):
    for fila in sudoku:
        for numero in fila:
            if not isinstance(numero, int):
                return False
    return True

def numerosEnRango(sudoku):
    numerosValidos = range(1, len(sudoku) + 1)
    for fila in sudoku:
        for numero in fila:
            if numero not in numerosValidos:
                return False
    return True

def checkNumerosValidos(sudoku):
    return sonNumerosEnteros(sudoku) and numerosEnRango(sudoku)

if __name__ == '__main__':
    for attr in sorted(casosTest.__dict__):
        if attr.startswith('__'):
            pass
        else:
            print(attr, " => ", checkNumerosValidos(casosTest.__dict__[attr]))