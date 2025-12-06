from core.cpu import CPU
from core.memory import Memory
from iod.io_manager import IOManager
from persistence.program_loader import ProgramLoader
from ui.pygame_window import PygameWindow

def main():
    """Función principal que inicializa y ejecuta el simulador."""
    
    # 1. Crear componentes centrales
    memory = Memory()
    io_manager = IOManager()
    
    # 2. Cargar el programa
    # El archivo 'programa.txt' debe estar en la carpeta 'programas'
    program_loader = ProgramLoader("programas/ejemplos/mensaje_hola.txt", memory)
    program_loader.load_into_memory()

    # 3. Crear la CPU
    cpu = CPU(memory, io_manager)

    # 4. Crear la ventana de la interfaz gráfica
    pygame_window = PygameWindow(cpu, memory, io_manager, program_loader)

    # 5. Iniciar el bucle principal de la aplicación
    pygame_window.main_loop()

if __name__ == "__main__":
    main()
