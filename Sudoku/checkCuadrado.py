import casosTest

def checkCuadrado(sudoku):
    numeroFilas = len(sudoku)
    for fila in sudoku:
        if len(fila) != numeroFilas:
            return False
    return True

if __name__ == '__main__':
    for attr in sorted(casosTest.__dict__):
        if attr.startswith('__'):
            pass
        else:
            print(attr, "=>", checkCuadrado(casosTest.__dict__[attr]))