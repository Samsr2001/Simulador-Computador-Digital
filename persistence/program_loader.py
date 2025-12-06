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

                    parts = line.split()
                    mnemonic = parts[0].upper()
                    
                    try:
                        opcode_enum = Opcode[mnemonic]
                        opcode = opcode_enum.value
                    except KeyError:
                        print(f"Error: Mnemónico desconocido '{mnemonic}' en línea: {line}")
                        continue

                    operand = 0
                    if len(parts) > 1:
                        operand_str = parts[1]
                        if operand_str.startswith("'") and operand_str.endswith("'"):
                            # Es un caracter, como 'A'
                            operand = ord(operand_str.strip("'"))
                        else:
                            # Es un número (decimal por defecto)
                            operand = int(operand_str)


                    # Construir la instrucción de 16 bits
                    # 4 bits para opcode, 12 para operando
                    instruction_value = (opcode << 12) | (operand & 0xFFF)
                    
                    self.memory.write(address, instruction_value)
                    address += 1
        
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo del programa en '{self.file_path}'")
        except Exception as e:
            print(f"Error inesperado al cargar el programa: {e}")

