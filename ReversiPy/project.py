import random

# FUNCIÓN PARA MOSTRAR EL TABLERO EN CONSOLA
def generar_tablero(jugadas_j1, jugadas_j2):
    # i controla las filas del tablero
    for i in range(12):
        # j controla las columnas del tablero
        for j in range(12):
            # Imprimir números en la parte izquierda e derecha
            if (j == 0 or j == 11) and (2 <= i <= 9):
                print(i - 1, end='')

            # Imprimir números en la parte superior y inferior
            if (i == 0 or i == 11) and 2 <= j <= 9:
                print(j - 1, end='')

            # Imprimir '+' en las esquinas
            if (i == 1 and j == 1) or (i == 1 and j == 10) or (i == 10 and j == 1) or (i == 10 and j == 10):
                print('+', end='')

            # Imprimir margen superior e inferior
            if (i == 1 or i == 10) and (2 <= j <= 9):
                print('-', end='')

            # Imprimir margen izquierdo y derecho
            if (2 <= i <= 9) and (j == 1 or j == 10):
                print('|', end='')

            # Imprimir esquinas de la margen
            if ((i == 0 or i == 11) and ((j == 0 or j == 1) or (j == 10 or j == 11))) or ((i == 1 or i == 10) and (j == 0 or j == 11)):
                print(' ', end='')

            # Acceder al tablero donde van las fichas
            if ((2 <= i <= 9) and 2 <= j <= 9):
                # Verificar si hay una ficha en la posición actual
                coordenada_actual = f'{i - 1},{j - 1}'
                if (coordenada_actual in jugadas_j1) or (coordenada_actual in jugadas_j2):
                    ficha_poner = ficha[jugador_1] if coordenada_actual in jugadas_j1 else ficha[jugador_2]
                    print(ficha_poner, end='')
                else:
                    print(' ', end='')
        print()


# FUNCIÓN QUE DETERMINA SI LA JUGADA ES CORRECTA
def entrada_correcta(entrada):
    # Verificar si la entrada es 'P', 'T' o 'A'
    if entrada == 'P' or entrada == 'T' or entrada == 'A':
        return True

    # Verificar si la entrada es una coordenada válida
    # 1,8
    # a,b
    # 1,2,3,4,5,6
    if ',' in entrada:
        entrada = entrada.split(',')  # Separar la entrada en fila y columna
        # ['1', '8']
        try:
            if len(entrada) != 2:  # Verificar que haya exactamente dos valores
                return False
            entrada[0] = int(entrada[0])  # Convertir fila a entero
            entrada[1] = int(entrada[1])  # Convertir columna a entero
            # [1, 8]
            if 1 <= entrada[0] <= 8 and 1 <= entrada[1] <= 8:  # Verificar rango

                coordenada = f'{entrada[0]},{entrada[1]}'
                if coordenada in posicion_fichas_j1 or coordenada in posicion_fichas_j2:
                    return False
                else:
                    return True
            else:
                return False
        except ValueError:  # Manejar errores de conversión
            return False
    else:
        return False


# FUNCIÓN PARA BUSCAR COORDENADAS DISPONIBLES
def buscar_disponibles(jugadas_j1, jugadas_j2):
    # Lista que va a almacenar coordenadas disponibles
    disponibles = []
    for i in range(1, 9):
        for j in range(1, 9):
            # creamos un string con el formato de las coordenadas de las fichas para comparar y verificar si la posicion ya está ocupada
            coordenada_actual = f'{i},{j}'  # Formato de coordenada
            if not (coordenada_actual in jugadas_j1) and not (coordenada_actual in jugadas_j2):
                disponibles.append(coordenada_actual)
    return disponibles


def realizar_volteretas(ultima_jugada, jugadas_j1, jugadas_j2):
    # Direcciones posibles: arriba, abajo, izquierda, derecha y las cuatro diagonales
    direcciones = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1),  (1, 0), (1, 1)]

    fichas_a_voltear = []
    ultima_jugada = ultima_jugada.split(',')
    fila = int(ultima_jugada[0])
    columna = int(ultima_jugada[1])

    for direccion in direcciones:
        dx, dy = direccion
        x, y = columna + dx, fila + dy
        fichas_temporales = []

        # Verificar si hay fichas del oponente en la dirección actual
        while 1 <= x <= 8 and 1 <= y <= 8 and f'{y},{x}' in (posicion_fichas_j1 if jugador_turno == jugador_2 else posicion_fichas_j2):
            fichas_temporales.append(f'{y},{x}')
            x += dx
            y += dy

        # Si encontramos una ficha del jugador actual al final de la dirección, volteamos las fichas temporales
        if 1 <= x < 8 and 1 <= y < 8 and f'{y},{x}' in (posicion_fichas_j2 if jugador_turno == jugador_2 else posicion_fichas_j1):
            fichas_a_voltear.extend(fichas_temporales)

        
    if len(fichas_a_voltear)>0:
        input(f'\nVoltereta en {fichas_a_voltear}, pulsa [ENTER] para asignar jugada al tablero')
        print()
        global cantidad_jugadas_j1, cantidad_jugadas_j2
        if jugador_turno == jugador_1:
            cantidad_jugadas_j1 += len(fichas_a_voltear)
            cantidad_jugadas_j2 -= len(fichas_a_voltear)
            posicion_fichas_j1.extend(fichas_a_voltear)

        else:
            cantidad_jugadas_j2 += len(fichas_a_voltear)
            cantidad_jugadas_j1 -= len(fichas_a_voltear)
            posicion_fichas_j2.extend(fichas_a_voltear)

        for ficha in fichas_a_voltear:
            if ficha in posicion_fichas_j2 if jugador_turno == jugador_1 else posicion_fichas_j1:
                posicion_fichas_j2 if jugador_turno == jugador_1 else posicion_fichas_j1.remove(ficha)
        
        generar_tablero(posicion_fichas_j1, posicion_fichas_j2)

    return len(fichas_a_voltear) > 0




# CONFIGURACIÓN DEL JUEGO
jugador_1 = input('Por favor indique nombre de participante #1: ')
jugador_2 = input('Por favor indique nombre de participante #2: ')

print(f'Lanzando una moneda al aire para decidir si empieza {jugador_1} o {jugador_2}...')
# utilizamos sintaxis de condicional comprimida para elegir aleatoriamente el jugador que empieza
# sintaxis: <resultado_si> if <condicional> else <resultado_sino>
jugador_turno = jugador_1 if random.random() >= 0.5 else jugador_2
print(f'Empieza {jugador_turno}')

# con este ciclo verificamos que la entrada sea valida para la eleccion de la ficha
ficha_primer_jugador = ''
while ficha_primer_jugador != 'X' and ficha_primer_jugador != 'O':
    ficha_primer_jugador = input(f'{jugador_turno} indica con qué ficha vas a jugar [X]/[O]: ').upper()

# Creamos un diccionario donde la clave es el nombre del jugador y el valor es la ficha del jugador
ficha = {jugador_turno : ficha_primer_jugador}
ficha[jugador_1 if jugador_turno == jugador_2 else jugador_2] = 'X' if ficha_primer_jugador == 'O' else 'O'

print(f'{jugador_1} jugará con ficha [{ficha[jugador_1]}]')
print(f'{jugador_2} jugará con ficha [{ficha[jugador_2]}]')


# INICIO DEL JUEGO
posicion_fichas_j1 = []
posicion_fichas_j2 = []

if ficha[jugador_1] == 'X':
    posicion_fichas_j1.append('4,4')
    posicion_fichas_j1.append('5,5')

    posicion_fichas_j2.append('4,5')
    posicion_fichas_j2.append('5,4')
else:
    posicion_fichas_j1.append('4,5')
    posicion_fichas_j1.append('5,4')

    posicion_fichas_j2.append('4,4')
    posicion_fichas_j2.append('5,5')

print('\nCargando el tablero del juego...')
generar_tablero(posicion_fichas_j1, posicion_fichas_j2)
cantidad_jugadas = 4
cantidad_jugadas_j1 = 2
cantidad_jugadas_j2 = 2


# BUCLE PRINCIPAL DEL JUEGO
while cantidad_jugadas < 64:
    # Imprime el puntaje de cada jugador respectivamente
    print(f'Puntaje --> {jugador_1}: {cantidad_jugadas_j1} {jugador_2}: {cantidad_jugadas_j2}')

    # Se hace un llamado a la funcion entrada_correcta para verificar si la entrada es valida
    decision = ''
    while not entrada_correcta(decision):
        print(f'\n{jugador_turno} [{ficha[jugador_turno]}] indica jugada <fila>,<columna>, [P] para pasar el turno, [T] para terminar el juego o [A] para jugada al azar: ', end='')
        decision = input().upper() # Se pone en mayusculas para el manejo de errores

    # Condicional para pasar el turno
    if decision == 'P':
        pass

    # Condicional para terminar la partida
    elif decision == 'T':
        break


    # Condicional para realizar la seleccion aleatoria de unas coordenadas
    elif decision == 'A':
        # se crea la lista coordenadas_disponibles con la funcion buscar_disponibles(), esta lista contiene todas las coordenadas disponibles en el tablero
        coordenadas_disponibles = buscar_disponibles(posicion_fichas_j1, posicion_fichas_j2)
        decision = random.choice(coordenadas_disponibles)

        # Verifica de quien es la jugada y le asigna la jugada a la lista de fichas del jugador
        if jugador_turno == jugador_1:
            posicion_fichas_j1.append(decision)
            cantidad_jugadas_j1 += 1
        else:
            posicion_fichas_j2.append(decision)
            cantidad_jugadas_j2 += 1

        # cede el turno al otro jugador
        

    else:
        if jugador_turno == jugador_1:
            posicion_fichas_j1.append(decision)
            cantidad_jugadas_j1 += 1
        else:
            posicion_fichas_j2.append(decision)
            cantidad_jugadas_j2 += 1

    

    # re genera el tablero para mostrar las nuevas jugadas
    generar_tablero(posicion_fichas_j1, posicion_fichas_j2)
    if  not (decision in 'PT'):
        realizar_volteretas(decision, posicion_fichas_j1, posicion_fichas_j2)

    jugador_turno = jugador_1 if jugador_turno == jugador_2 else jugador_2
    cantidad_jugadas = cantidad_jugadas_j1 + cantidad_jugadas_j2

# FINALIZACIÓN DEL JUEGO
# Mensaje especial para cuando se finaliza la partida manualmente
if decision == 'T':
    print(f'\nEl jugador {jugador_turno} ha abandonado la partida, el juego finaliza')
    print(f'¡¡¡ Ganó {jugador_1 if jugador_turno == jugador_2 else jugador_2} !!!')
# Mensaje de finalizacion
else:
    print(f'No hay coordenadas libres, el juego debe terminar')
    print(f'Puntaje --> {jugador_1}: {cantidad_jugadas_j1} {jugador_2}: {cantidad_jugadas_j2}')
    if cantidad_jugadas_j1 == cantidad_jugadas_j2:
        print(f'¡¡¡ Empate !!!')
    else:
        print(f'¡¡¡ Ganó {jugador_1 if cantidad_jugadas_j1 > cantidad_jugadas_j2 else jugador_2} !!!')