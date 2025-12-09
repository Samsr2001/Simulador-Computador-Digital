from core.memory import Memory
from core.instruction import Instruction
from utils.enums import Opcode

class ControlUnit:
    """Unidad de Control (CU)."""

    def __init__(self, memory: Memory):
        """
        Inicializa la Unidad de Control.
        Args:
            memory (Memory): La memoria principal del sistema.
        """
        self.memory = memory
        self.instruction: Instruction = None

    def fetch(self, pc: int) -> int:
        """
        Fase de búsqueda: obtiene la siguiente instrucción de la memoria.
        Args:
            pc (int): El Program Counter, apuntando a la instrucción actual.
        Returns:
            int: El valor crudo (16 bits) de la instrucción.
        """
        return self.memory.read(pc)

    def decode(self, raw_instruction: int) -> Instruction:
        """
        Fase de decodificación: interpreta el valor crudo de la instrucción.
        Args:
            raw_instruction (int): El valor de 16 bits de la instrucción.
        Returns:
            Instruction: Un objeto Instruction con opcode y operando.
        """
        self.instruction = Instruction(raw_instruction)
        return self.instruction

    def execute(self, cpu):
        """
        Fase de ejecución: realiza la operación indicada por el opcode.
        Este método modifica el estado de la CPU (registros, flags, pc).
        Args:
            cpu: La instancia de la CPU que se está ejecutando.
        """
        opcode = self.instruction.opcode
        operand = self.instruction.operand

        # Variable para rastrear si el PC ya fue modificado
        pc_modified = False

        if opcode == Opcode.LOAD:
            cpu.ac = self.memory.read(operand)
        elif opcode == Opcode.STORE:
            self.memory.write(operand, cpu.ac)
        elif opcode == Opcode.ADD:
            value_from_mem = self.memory.read(operand)
            cpu.ac = cpu.alu.add(cpu.ac, value_from_mem)
            cpu.flag_z = 1 if cpu.ac == 0 else 0
        elif opcode == Opcode.SUB:
            value_from_mem = self.memory.read(operand)
            cpu.ac = cpu.alu.sub(cpu.ac, value_from_mem)
            cpu.flag_z = 1 if cpu.ac == 0 else 0
        elif opcode == Opcode.JUMP:
            cpu.pc = operand
            pc_modified = True
        elif opcode == Opcode.JZ:
            if cpu.flag_z == 1:
                cpu.pc = operand
                pc_modified = True
        elif opcode == Opcode.IN:
            cpu.waiting_for_input = True
            pc_modified = True  # El PC se manejará después de la entrada
        elif opcode == Opcode.OUT:
            cpu.io_manager.write_char(cpu.ac)
        elif opcode == Opcode.OUTNUM:
            cpu.io_manager.write_value(cpu.ac)
        elif opcode == Opcode.LOADI:
            cpu.ac = operand
        elif opcode == Opcode.HALT:
            cpu.halted = True
            pc_modified = True

        # Si el PC no fue modificado por un salto o una espera, avanzamos
        if not pc_modified:
            cpu.pc += 1
