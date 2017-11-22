import casosTest

def checkFilas(sudoku):
    for fila in sudoku:
        posicionNumero = 0
        for numero in fila:
            if numero in fila[posicionNumero + 1:]:
                return False
            else:
                posicionNumero += 1
    return True

if __name__ == '__main__':
    for attr in sorted(casosTest.__dict__):
        if attr.startswith('__'):
            pass
        else:
            print(attr, "=>", checkFilas(casosTest.__dict__[attr]))