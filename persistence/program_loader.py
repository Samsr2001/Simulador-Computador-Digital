from core.memory import Memory
from utils.enums import Opcode

class ProgramLoader:
    """Carga un programa desde un archivo de texto a la memoria."""

    def __init__(self, file_path: str, memory: Memory):
        """
        Inicializa el cargador de programas.
        Args:
            file_path (str): La ruta al archivo del programa.
            memory (Memory): La instancia de la memoria donde se cargará el programa.
        """
        self.file_path = file_path
        self.memory = memory

    def load_into_memory(self):
        """
        Lee el archivo de programa, lo compila a 16 bits y lo carga en la RAM.
        """
        self.memory.reset() # Limpia la memoria antes de cargar
        address = 0
        try:
            with open(self.file_path, 'r') as f:
                for line in f:
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
                            # Es un caracter, como 'A'. Usar slicing es más seguro.
                            char_literal = operand_str[1:-1]
                            if char_literal:
                                # Maneja casos como ' ' (espacio)
                                operand = ord(char_literal)
                            else:
                                # Caso '' (caracter vacío)
                                operand = 0
                        else:
                            # Es un número (decimal por defecto)
                            try:
                                operand = int(operand_str)
                            except ValueError:
                                print(f"Error: Operando inválido '{operand_str}' en línea: {line}")
                                continue

                    # Construir la instrucción de 16 bits
                    # 4 bits para opcode, 12 para operando
                    instruction_value = (opcode << 12) | (operand & 0xFFF)
                    
                    self.memory.write(address, instruction_value)
                    address += 1
        
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo del programa en '{self.file_path}'")
        except Exception as e:
            print(f"Error inesperado al cargar el programa: {e}")

