def accesoCasosTexttest(matrizCasosTest, rutaAccesoFichero):
    try:
        if not isinstance(rutaAccesoFichero, str):
            raise ValueError
        fichero = open(rutaAccesoFichero, 'r')
    except FileNotFoundError:
        print("Fichero no encontrado")
        return []
    except ValueError:
        print("El nombre del fichero ha de ser un string")
        return []
    else:
        matrizCasosTest = []
        numeroPropiedadesItem = 0
        for linea in fichero:
            if linea.find("day") != -1:
                casosTestDia = []
            elif linea == "\n":
                matrizCasosTest.append(casosTestDia)
                print(matrizCasosTest)
            elif linea.find("name") != -1:
               numeroPropiedadesItem = len(linea.split(','))
            else:
                item = linea.rstrip().rsplit(',', maxsplit=numeroPropiedadesItem - 1)
                for atributo in item:
                	try:
                		atributo = int(atributo)
                	except:
                 		pass
                casosTestDia.append(print((item)))
        fichero.close()
        return matrizCasosTest
 
def crearFicheroCasosTest(ficheroVolcadoCasosTest, matrizCasosTest):
    try:
        if not isinstance(ficheroVolcadoCasosTest, str):
            raise ValueError
        stdout = open(ficheroVolcadoCasosTest, 'w')
    except ValueError:
            print("La ruta de acceso al fichero ha de ser un string")
    else:
        for (offset, casosTestDia) in enumerate(matrizCasosTest):
            stdout.write('-' * 5 + " Dia %d: " % offset + '-' * 5 + '\n')
            for item in casosTestDia:
                stdout.write(','.join(item) + '\n')
        stdout.close()

def mostrarCasosTest(matrizCasosTest):
    for (offset, casosTestDia) in enumerate(matrizCasosTest):
        print('-' * 5 + " Dia %d: " % offset + '-' * 5)
        for item in casosTestDia:
            print(item)


if __name__ == "__main__":
    rutaAccesoFichero = "C:\\Users\\ivanp\\Desktop\\Ollivander\\casos_test.txt"
    matrizCasosTest = []
    matrizCasosTest = accesoCasosTexttest(matrizCasosTest, rutaAccesoFichero)
    mostrarCasosTest(matrizCasosTest)
    ficheroVolcadoCasosTest = "stdout.txt"
    crearFicheroCasosTest(ficheroVolcadoCasosTest, matrizCasosTest)