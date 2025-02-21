import random

# FUNCIÓN PARA MOSTRAR EL TABLERO EN CONSOLA
def generar_tablero():
    """Muestra el tablero actual en la consola junto con el puntaje."""
    print()
    print('  12345678  ')
    print(' +--------+ ')
    for i in range(1, 9):
        print(f"{i}|{''.join(cuadro[i-1])}|{i}")
    print(' +--------+ ')
    print('  12345678  ')
    print(f'Puntaje --> {jugador_1}: {cantidad_jugadas_j1} {jugador_2}: {cantidad_jugadas_j2}')


# FUNCIÓN QUE DETERMINA SI LA JUGADA ES CORRECTA
def entrada_correcta(entrada):
    """Verifica si una entrada es válida.

    Args:
        entrada (str): La entrada ingresada por el usuario.

    Returns:
        bool: True si la entrada es válida, False en caso contrario.
    """
    if entrada in ('P', 'T', 'A'):
        return True
    if ',' in entrada:
        entrada = entrada.split(',')
        try:
            if len(entrada) != 2:
                return False
            entrada[0] = int(entrada[0]) - 1
            entrada[1] = int(entrada[1]) - 1

            if 0 <= entrada[0] <= 7 and 0 <= entrada[1] <= 7:
                return cuadro[entrada[0]][entrada[1]] == ' '
            return False
        except ValueError:
            return False
    return False


# FUNCIÓN PARA BUSCAR COORDENADAS DISPONIBLES
def buscar_disponibles():
    """Busca las coordenadas disponibles en el tablero.

    Returns:
        list: Lista de tuplas con coordenadas disponibles.
    """
    return [(i, j) for i in range(8) for j in range(8) if cuadro[i][j] == ' ']


# FUNCIÓN PARA REALIZAR VOLTERETAS
def realizar_volteretas(ultima_jugada):
    """Realiza las volteretas en el tablero.

    Args:
        ultima_jugada (tuple): Coordenadas de la última jugada realizada.
    """
    direcciones = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    fichas_a_voltear = []
    fila, columna = ultima_jugada

    for dx, dy in direcciones:
        x, y = columna + dx, fila + dy
        fichas_temporales = []

        while 0 <= x <= 7 and 0 <= y <= 7 and cuadro[y][x] == ficha[jugador_oponente]:
            fichas_temporales.append((y + 1, x + 1))
            x += dx
            y += dy

        if 0 <= x <= 7 and 0 <= y <= 7 and cuadro[y][x] == ficha[jugador_turno]:
            fichas_a_voltear.extend(fichas_temporales)

    if fichas_a_voltear:
        input(f'\nVoltereta en {fichas_a_voltear}, pulsa [ENTER] para asignar jugada al tablero')
        print()

        global cantidad_jugadas_j1, cantidad_jugadas_j2
        if jugador_turno == jugador_1:
            cantidad_jugadas_j1 += len(fichas_a_voltear)
            cantidad_jugadas_j2 -= len(fichas_a_voltear)
        else:
            cantidad_jugadas_j2 += len(fichas_a_voltear)
            cantidad_jugadas_j1 -= len(fichas_a_voltear)

        for fila_temp, columna_temp in fichas_a_voltear:
            cuadro[fila_temp - 1][columna_temp - 1] = ficha[jugador_turno]

        generar_tablero()


# Inicialización del tablero y diccionario de fichas
cuadro = [[' ' for _ in range(8)] for _ in range(8)]
ficha = {}

# CARGAR JUEGO SIN TERMINAR
with open("jugadas.txt", "a+") as f:
    f.seek(0)
    jugadas = f.readlines()

decision_archivo = ''
while jugadas:
    decision_archivo = input(
        'Se detectó un juego sin terminar, ¿desea continuar con él? Y/N: '
    ).upper().strip()
    if decision_archivo in ('Y', 'N'):
        break

if decision_archivo == 'Y':
    i = 0
    cantidad_jugadas_j1 = 0
    cantidad_jugadas_j2 = 0
    for linea in jugadas:
        if i == 8:
            linea = linea.split(',')
            jugador_1 = linea[0]
            jugador_2 = linea[1]
            ficha[jugador_1] = linea[2]
            ficha[jugador_2] = linea[3]
            jugador_turno = linea[4]
            jugador_oponente = jugador_1 if jugador_turno == jugador_2 else jugador_2
        else:
            linea = linea.replace('\n', '')
            cantidad_jugadas_j1 += linea.count('X')
            cantidad_jugadas_j2 += linea.count('O')
            fila = linea.split(',')
            if linea:
                cuadro[i] = fila
            i += 1
    cantidad_jugadas = cantidad_jugadas_j1 + cantidad_jugadas_j2

else:
    cuadro[3][3] = 'X'
    cuadro[4][4] = 'X'
    cuadro[3][4] = 'O'
    cuadro[4][3] = 'O'

    # Configuración del juego
    jugador_1 = input('Por favor indique nombre de participante #1: ')
    jugador_2 = input('Por favor indique nombre de participante #2: ')

    print(f'Lanzando una moneda al aire para decidir si empieza {jugador_1} o {jugador_2}...')
    if random.random() >= 0.5:
        jugador_turno = jugador_1
        jugador_oponente = jugador_2
    else:
        jugador_turno = jugador_2
        jugador_oponente = jugador_1
    print(f'Empieza {jugador_turno}')

    while True:
        ficha_primer_jugador = input(
            f'{jugador_turno} indica con qué ficha vas a jugar [X]/[O]: '
        ).upper().strip()
        if ficha_primer_jugador in ('X', 'O'):
            break

    ficha[jugador_turno] = ficha_primer_jugador
    ficha[jugador_1 if jugador_turno == jugador_2 else jugador_2] = (
        'X' if ficha_primer_jugador == 'O' else 'O'
    )

    print(f'{jugador_1} jugará con ficha [{ficha[jugador_1]}]')
    print(f'{jugador_2} jugará con ficha [{ficha[jugador_2]}]')

    cantidad_jugadas = 4
    cantidad_jugadas_j1 = 2
    cantidad_jugadas_j2 = 2

print('\nCargando el tablero del juego...')
generar_tablero()

# Bucle principal del juego
while cantidad_jugadas < 64:
    while True:
        print(
            f'\n{jugador_turno} [{ficha[jugador_turno]}] indica jugada <fila>,<columna>, '
            '[P] para pasar el turno, [T] para terminar el juego o [A] para jugada al azar: ',
            end=''
        )
        decision = input().upper().strip()
        if entrada_correcta(decision):
            break

    if decision == 'P':
        pass
    elif decision == 'T':
        break
    elif decision == 'A':
        coordenadas_disponibles = buscar_disponibles()
        decision = random.choice(coordenadas_disponibles)
        cuadro[decision[0]][decision[1]] = ficha[jugador_turno]
        if jugador_1 == jugador_turno:
            cantidad_jugadas_j1 += 1
        else:
            cantidad_jugadas_j2 += 1
        generar_tablero()
        realizar_volteretas(decision)
    else:
        decision = tuple(map(lambda x: int(x) - 1, decision.split(',')))
        cuadro[decision[0]][decision[1]] = ficha[jugador_turno]
        if jugador_1 == jugador_turno:
            cantidad_jugadas_j1 += 1
        else:
            cantidad_jugadas_j2 += 1
        generar_tablero()
        realizar_volteretas(decision)

    if jugador_turno == jugador_2:
        jugador_turno = jugador_1
        jugador_oponente = jugador_2
    else:
        jugador_turno = jugador_2
        jugador_oponente = jugador_1

    cantidad_jugadas = cantidad_jugadas_j1 + cantidad_jugadas_j2

    with open('jugadas.txt', 'w') as f:
        for i in range(9):
            if i == 8:
                f.write(
                    f'{jugador_1},{jugador_2},{ficha[jugador_1]},{ficha[jugador_2]},{jugador_turno}'
                )
            else:
                f.write(','.join(cuadro[i]))
                f.write('\n')

# Borrar contenido (finalización del juego)
with open('jugadas.txt', 'w') as f:
    pass

# Finalización del juego
if decision == 'T':
    print(f'\nEl jugador {jugador_turno} ha abandonado la partida, el juego finaliza')
    print(f'¡¡¡ Ganó {jugador_1 if jugador_turno == jugador_2 else jugador_2} !!!')
else:
    print('No hay coordenadas libres, el juego debe terminar')
    print(f'Puntaje --> {jugador_1}: {cantidad_jugadas_j1} {jugador_2}: {cantidad_jugadas_j2}')
    if cantidad_jugadas_j1 == cantidad_jugadas_j2:
        print('¡¡¡ Empate !!!')
    else:
        print(f'¡¡¡ Ganó {jugador_1 if cantidad_jugadas_j1 > cantidad_jugadas_j2 else jugador_2} !!!')
