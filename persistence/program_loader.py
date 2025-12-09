from core.memory import Memory
from utils.enums import Opcode
from typing import List, Optional

class ProgramLoader:
    """Carga un programa en la memoria desde un archivo o una lista."""

    def __init__(self, memory: Memory, file_path: Optional[str] = None):
        """
        Inicializa el cargador de programas.
        Args:
            memory (Memory): La instancia de la memoria.
            file_path (str, optional): La ruta al archivo del programa. Defaults to None.
        """
        self.file_path = file_path
        self.memory = memory

    def load_from_list(self, program_lines: List[str]):
        """
        Compila un programa desde una lista de strings y lo carga en la RAM.
        Args:
            program_lines (List[str]): Las líneas del programa en ensamblador.
        """
        self.memory.reset()  # Limpia la memoria antes de cargar
        try:
            self._parse_lines(program_lines)
        except Exception as e:
            print(f"Error inesperado al cargar el programa desde la lista: {e}")

    def load_into_memory(self):
        """
        Lee el archivo de programa, lo compila a 16 bits y lo carga en la RAM.
        """
        if not self.file_path:
            print("Error: No se ha especificado un file_path para load_into_memory.")
            return
            
        self.memory.reset()  # Limpia la memoria antes de cargar
        try:
            with open(self.file_path, 'r') as f:
                lines = f.readlines()
                self._parse_lines(lines)
        
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo del programa en '{self.file_path}'")
        except Exception as e:
            print(f"Error inesperado al cargar el programa: {e}")

    def _parse_lines(self, lines: List[str]):
        """
        Parsea una lista de líneas de código y las carga en memoria.
        Args:
            lines (List[str]): Lista de líneas de código ensamblador.
        """
        address = 0
        for line in lines:
            line = line.strip()
            if not line or line.startswith('#'):  # Ignorar líneas vacías o comentarios
                continue

            # Separar mnemónico del resto de la línea
            parts = line.split(maxsplit=1)
            mnemonic = parts[0].upper()
            
            try:
                opcode_enum = Opcode[mnemonic]
                opcode = opcode_enum.value
            except KeyError:
                print(f"Error: Mnemónico desconocido '{mnemonic}' en línea: {line}")
                continue

            operand = 0
            if len(parts) > 1:
                operand_str = parts[1].strip()
                
                # Ignorar comentarios al final de la línea
                if '#' in operand_str:
                    operand_str = operand_str.split('#', 1)[0].strip()

                if not operand_str:
                    operand = 0
                elif operand_str.startswith("'") and operand_str.endswith("'"):
                    char_literal = operand_str[1:-1]
                    if char_literal:
                        operand = ord(char_literal)
                    else:
                        operand = 0
                else:
                    try:
                        operand = int(operand_str)
                    except ValueError:
                        print(f"Error: Operando inválido '{operand_str}' en línea: {line}")
                        continue

            # Construir la instrucción de 16 bits
            instruction_value = (opcode << 12) | (operand & 0xFFF)
            
            self.memory.write(address, instruction_value)
            address += 1


