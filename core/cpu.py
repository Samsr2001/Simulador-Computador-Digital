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
        self.waiting_for_input = False

    def step(self):
        """Ejecuta un único ciclo de instrucción o maneja el estado de espera."""
        if self.halted:
            return

        # Si estamos esperando una entrada de teclado
        if self.waiting_for_input:
            key = self.io_manager.pop_key()
            if key is not None:
                self.ac = key
                self.io_manager.write_char(key)  # <-- ECHO a la pantalla
                self.waiting_for_input = False
                self.pc += 1  # La instrucción IN ha terminado, avanzamos al siguiente
            return # Si no hay tecla, no hacemos nada más en este ciclo

        # --- Ciclo normal Fetch-Decode-Execute ---
        
        # 1. Fetch
        self.ir = self.control_unit.fetch(self.pc)

        # 2. Decode
        instruction = self.control_unit.decode(self.ir)
        pc_before_execute = self.pc

        # 3. Execute
        # La ejecución de 'IN' ahora activará 'waiting_for_input'
        self.control_unit.execute(self)
        
        # 4. Avanzar PC (si no es un salto o una instrucción de espera)
        # Si la ejecución resultó en una espera, no avanzamos el PC.
        # El PC se avanzará cuando se reciba la tecla.
        if not self.waiting_for_input:
            # Si el PC no fue modificado por un JUMP, lo incrementamos.
            if self.pc == pc_before_execute:
                self.pc += 1

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
        self.waiting_for_input = False
        self.memory.reset()
        self.io_manager.reset()
