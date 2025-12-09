# Simulador de Computador Digital con Arquitectura von Neumann

Este proyecto es un simulador funcional de un computador digital simple, desarrollado en Python con la librería Pygame. El simulador implementa la arquitectura de von Neumann, donde tanto las instrucciones del programa como los datos se almacenan en la misma memoria.

El objetivo principal es educativo: visualizar de manera gráfica e interactiva el funcionamiento interno de una CPU, incluyendo el ciclo de instrucción (búsqueda, decodificación, ejecución), el acceso a memoria y la interacción con dispositivos de entrada/salida.

## 🌟 Características Principales

-   **Simulación de CPU:** Incluye registros fundamentales como el Contador de Programa (PC), Registro de Instrucción (IR), Acumulador (AC) y un flag de Cero (FLAG_Z).
-   **Memoria RAM Interactiva:** Una visualización gráfica de la memoria de 256 celdas, donde se resalta en tiempo real la celda que está siendo accedida por la CPU.
-   **Interfaz Gráfica Completa:** Desarrollada con Pygame, la interfaz muestra paneles para la CPU, la Memoria, la Pantalla de salida y los Controles de la simulación.
-   **Conjunto de Instrucciones (ISA):** Implementa un ISA simple de 16 bits con instrucciones para carga/almacenamiento, operaciones aritméticas, saltos y entrada/salida.
-   **Controles de Ejecución:** Permite ejecutar programas de forma continua (`Run`), ciclo a ciclo (`Step`) o reiniciar la simulación (`Reset`).
-   **Cargador de Programas:** Los programas se escriben en un lenguaje ensamblador simple en archivos `.txt` y son cargados en memoria por el simulador.

## 📁 Estructura del Proyecto

El proyecto está organizado en módulos para separar las responsabilidades:

-   `core/`: Contiene la lógica central del computador (CPU, ALU, Unidad de Control, Memoria).
-   `iod/`: Gestiona los dispositivos de Entrada/Salida (Teclado y Pantalla simulada).
-   `persistence/`: Incluye el `ProgramLoader`, responsable de leer los archivos de programa y cargarlos en la memoria.
-   `ui/`: Contiene toda la lógica de la interfaz gráfica desarrollada con Pygame, incluyendo los diferentes paneles.
-   `utils/`: Módulo de utilidades con constantes, enumeraciones y funciones de ayuda.
-   `programas/`: Contiene los programas de ejemplo en lenguaje ensamblador para ser ejecutados por el simulador.

## 🛠️ Requisitos

Para ejecutar el simulador, necesitas tener instalado lo siguiente:

-   Python 3.x
-   La librería `pygame`

## 🚀 Instalación y Ejecución

Sigue estos pasos para poner en marcha el simulador:

1.  **Clona el repositorio:**
    ```bash
    git clone https://github.com/tu-usuario/Simulador-Computador-Digital.git
    cd Simulador-Computador-Digital
    ```

2.  **Crea y activa un entorno virtual** (recomendado):
    ```bash
    # En Linux/macOS
    python3 -m venv venv
    source venv/bin/activate

    # En Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Instala las dependencias:**
    El único requisito es `pygame`, que está listado en `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecuta el simulador:**
    ```bash
    python main.py
    ```
    Esto abrirá la ventana de Pygame con la interfaz del simulador.

## 📖 Cómo Usar el Simulador

-   **Panel de Control:** Usa los botones `Run`, `Step` y `Reset` para controlar la ejecución.
    -   `Run`: Ejecuta el programa de forma continua hasta encontrar una instrucción `HALT`.
    -   `Step`: Ejecuta una única instrucción del ciclo Fetch-Decode-Execute.
    -   `Reset`: Reinicia la CPU y la memoria a su estado inicial, recargando el programa desde `programa.txt`.
-   **Cargar Programas:** Para ejecutar un programa diferente, puedes editar el archivo `programas/programa.txt` o copiar el contenido de uno de los ejemplos de la carpeta `programas/ejemplos/` en él. Después, presiona `Reset` en el simulador para cargarlo en memoria.
-   **Entrada de Datos:** Cuando la CPU ejecuta la instrucción `IN`, el simulador esperará que presiones una tecla. El código ASCII de la tecla se cargará en el registro Acumulador (AC).

## 🖥️ Conjunto de Instrucciones (ISA)

Las instrucciones son de 16 bits: 4 bits para el código de operación (opcode) y 12 bits para el operando (dirección o valor).

| Opcode (hex) | Mnemónico  | Descripción                                          |
| ------------ | ---------- | ---------------------------------------------------- |
| `0x1`        | `LOAD`     | Carga el valor de `RAM[addr]` en el registro `AC`.    |
| `0x2`        | `STORE`    | Almacena el valor de `AC` en `RAM[addr]`.              |
| `0x3`        | `ADD`      | `AC = AC + RAM[addr]`. Actualiza `FLAG_Z`.           |
| `0x4`        | `SUB`      | `AC = AC - RAM[addr]`. Actualiza `FLAG_Z`.           |
| `0x5`        | `JUMP`     | `PC = addr`. Salta a la dirección especificada.      |
| `0x6`        | `JZ`       | Si `FLAG_Z == 1`, entonces `PC = addr`.              |
| `0x7`        | `IN`       | Espera una tecla y carga su valor ASCII en `AC`.     |
| `0x8`        | `OUT`      | Imprime el valor de `AC` como un caracter ASCII en la pantalla. |
| `0x9`        | `LOADI`    | Carga un valor inmediato (`val`) en `AC`.            |
| `0xA`        | `OUTNUM`   | Imprime el valor numérico de `AC` en la pantalla.      |
| `0xF`        | `HALT`     | Detiene la ejecución del programa.                   |

---

