import casosTest

def checkColumnas(sudoku):
    assert isinstance(
        sudoku, list), "la interfaz exige que sudoku debe ser una lista"
    numeroDeFilas = len(sudoku)
    indexFilaActual = 0
    for fila in sudoku:
        for numero in fila:
            indexFilaSiguiente = indexFilaActual + 1
            while indexFilaSiguiente < numeroDeFilas:
                try:
                    posicionNumeroFilaSiguiente = sudoku[indexFilaSiguiente].index(numero)
                except ValueError:
                    return False
                else:
                    if posicionNumeroFilaSiguiente == fila.index(numero):
                        return False
                    else:
                        indexFilaSiguiente += 1
        indexFilaActual += 1
    return True

if __name__ == '__main__':
    for attr in sorted(casosTest.__dict__):
        if attr.startswith('__'):
            pass
        else:
            print(attr, "=>", checkColumnas(casosTest.__dict__[attr]))