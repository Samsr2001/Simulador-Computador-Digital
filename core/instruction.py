from utils.enums import Opcode

class Instruction:
    """Representa una instrucción decodificada."""

    def __init__(self, raw_value: int):
        """
        Inicializa una instrucción a partir de su valor crudo de 16 bits.
        Args:
            raw_value (int): El valor de 16 bits de la instrucción.
        """
        self.raw_value = raw_value
        self.opcode: Opcode = self._extract_opcode(raw_value)
        self.operand: int = self._extract_operand(raw_value)

    def _extract_opcode(self, value: int) -> Opcode:
        """Extrae el opcode (4 bits más significativos)."""
        opcode_value = (value >> 12) & 0xF
        try:
            return Opcode(opcode_value)
        except ValueError:
            # Si el opcode no es válido, se podría tratar como HALT o una NOP (no operation)
            # Por ahora, para robustez, lo tratamos como HALT.
            return Opcode.HALT

    def _extract_operand(self, value: int) -> int:
        """Extrae el operando (12 bits menos significativos)."""
        return value & 0xFFF

    def __str__(self) -> str:
        """Representación en texto de la instrucción."""
        return f"Opcode: {self.opcode.name}, Operando: {self.operand:03X}"
