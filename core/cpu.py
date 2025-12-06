from core.alu import ALU
from core.control_unit import ControlUnit
from core.memory import Memory
from iod.io_manager import IOManager

class CPU:
    """Unidad Central de Procesamiento (CPU)."""

    def __init__(self, memory: Memory, io_manager: IOManager):
        """
        Inicializa la CPU.
        Args:
            memory (Memory): El sistema de memoria.
            io_manager (IOManager): El gestor de entrada/salida.
        """
        self.memory = memory
        self.io_manager = io_manager

        # Componentes internos
        self.alu = ALU()
        self.control_unit = ControlUnit(self.memory)

        # Registros
        self.pc = 0  # Program Counter
        self.ir = 0  # Instruction Register
        self.ac = 0  # Accumulator
        self.flag_z = 0  # Zero Flag

        # Estado
        self.halted = False
        self.running = False

    def step(self):
        """Ejecuta un único ciclo de instrucción (fetch-decode-execute)."""
        if self.halted:
            return

        # 1. Fetch
        pc_before_fetch = self.pc
        self.ir = self.control_unit.fetch(self.pc)
        self.pc += 1

        # 2. Decode
        instruction = self.control_unit.decode(self.ir)

        # 3. Execute
        # Si la instrucción es un salto, la CU modificará el PC directamente.
        # Si no, el PC ya se ha incrementado para la siguiente instrucción.
        self.control_unit.execute(self)
        
        # Si el PC no fue modificado por un salto, y la instrucción no fue un salto condicional no cumplido
        # if self.pc == pc_before_fetch + 1:
        #     pass # El PC ya está bien

    def run_cycle(self):
        """Wrapper para ejecutar un ciclo si la CPU está en modo 'running'."""
        if self.running and not self.halted:
            self.step()

    def run(self):
        """Inicia la ejecución continua."""
        self.running = True

    def stop(self):
        """Detiene la ejecución continua."""
        self.running = False
        
    def reset(self):
        """Reinicia la CPU y la memoria a su estado inicial."""
        self.pc = 0
        self.ir = 0
        self.ac = 0
        self.flag_z = 0
        self.halted = False
        self.running = False
        self.memory.reset()
        self.io_manager.reset()

