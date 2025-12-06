def to_binary(value, bits):
    """Convierte un valor a su representación binaria con un número de bits."""
    return format(value, f'0{bits}b')

def to_hex(value, bits):
    """Convierte un valor a su representación hexadecimal."""
    return format(value, f'0{bits//4}X')
