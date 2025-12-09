from core.cpu import CPU
from core.memory import Memory
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
from iod.io_manager import IOManager
from persistence.program_loader import ProgramLoader
from ui.pygame_window import PygameWindow
from programas.rom import CALCULATOR_PROGRAM

def main():
    """Función principal que inicializa y ejecuta el simulador."""
    
    # 1. Crear componentes centrales
    memory = Memory()
    io_manager = IOManager()
    
    # 2. Cargar el programa incorporado (calculadora)
    program_loader = ProgramLoader(memory)
    program_loader.load_from_list(CALCULATOR_PROGRAM)

    # 3. Crear la CPU
    cpu = CPU(memory, io_manager)

    # 4. Crear la ventana de la interfaz gráfica
    # Pasamos el programa incorporado para que la función de Reset funcione
    pygame_window = PygameWindow(cpu, memory, io_manager, program_loader, CALCULATOR_PROGRAM)

    # 5. Iniciar el bucle principal de la aplicación
    pygame_window.main_loop()

if __name__ == "__main__":
    main()
