# ReversiPy

**ReversiPy** es una implementación en Python del clásico juego de estrategia **Reversi** (también conocido como **Othello**). Este proyecto permite a dos jugadores competir en un tablero de 8x8, donde el objetivo es colocar fichas propias y voltear las fichas del oponente para dominar el mayor número de casillas posibles al finalizar la partida.

El juego se ejecuta en la consola y cuenta con las siguientes características principales:

## Características Principales

1. **Tablero Dinámico**:
   - El tablero se genera y actualiza en tiempo real en la consola.
   - Las fichas de los jugadores se representan con los símbolos `X` y `O`.
   - El tablero muestra números en los bordes para facilitar la selección de coordenadas.

2. **Turnos Alternados**:
   - Los jugadores ingresan sus nombres al inicio del juego.
   - Se decide aleatoriamente quién comienza la partida.
   - Cada jugador elige su ficha (`X` o `O`) al inicio.

3. **Mecánica de Juego**:
   - Los jugadores ingresan coordenadas en formato `fila,columna` para colocar sus fichas.
   - Si una jugada es válida, el juego voltea las fichas del oponente que quedan atrapadas entre la nueva ficha y las fichas propias.
   - Los jugadores pueden pasar su turno (`P`), terminar la partida (`T`) o solicitar una jugada aleatoria (`A`).

4. **Reglas del Reversi**:
   - El juego termina cuando no quedan movimientos válidos o cuando el tablero está completo.
   - Gana el jugador con más fichas propias en el tablero al finalizar la partida.

5. **Interacción en Consola**:
   - El juego es interactivo y guía a los jugadores durante la partida.
   - Al finalizar, se muestra el puntaje de ambos jugadores y el ganador.

6. **Funcionalidades Adicionales**:
   - **Jugada Aleatoria**: Los jugadores pueden solicitar que el sistema elija una jugada válida al azar.
   - **Volteo de Fichas**: El sistema detecta automáticamente las fichas que deben voltearse en todas las direcciones (horizontal, vertical y diagonal).
   - **Puntaje en Tiempo Real**: Muestra el número de fichas de cada jugador durante la partida.

---

## Cómo Funciona el Código

- **Generación del Tablero**: La función `generar_tablero` dibuja el tablero en la consola, mostrando las fichas de ambos jugadores y los bordes numerados.
- **Validación de Jugadas**: La función `entrada_correcta` verifica si las coordenadas ingresadas son válidas y si la casilla está disponible.
- **Volteo de Fichas**: La función `realizar_volteretas` detecta y voltea las fichas del oponente en todas las direcciones posibles.
- **Jugadas Aleatorias**: La función `buscar_disponibles` encuentra todas las casillas libres en el tablero para permitir jugadas aleatorias.
- **Lógica del Juego**: El bucle principal controla los turnos, actualiza el tablero y verifica si el juego ha terminado.

---

## Requisitos para Ejecutar

- Python 3.x instalado.
- Ejecutar el script en una terminal o consola.

---

## Ejemplo de Flujo de Juego

1. Los jugadores ingresan sus nombres.
2. El sistema decide aleatoriamente quién comienza.
3. Los jugadores eligen sus fichas (`X` o `O`).
4. El tablero inicial se muestra con las fichas centrales colocadas.
5. Los jugadores alternan turnos para colocar fichas o pasar.
6. El juego termina cuando no hay más movimientos válidos.
7. Se muestra el puntaje final y el ganador.

---
