class ALU:
    """Unidad Aritmético-Lógica (ALU)."""

    def add(self, a: int, b: int) -> int:
        """
        Suma dos números de 16 bits.
        Args:
            a (int): El primer operando (acumulador).
            b (int): El segundo operando (valor de memoria).
        Returns:
            int: El resultado de la suma, truncado a 16 bits.
        """
        return (a + b) & 0xFFFF

    def sub(self, a: int, b: int) -> int:
        """
        Resta dos números de 16 bits.
        Args:
            a (int): El primer operando (acumulador).
            b (int): El segundo operando (valor de memoria).
        Returns:
            int: El resultado de la resta, truncado a 16 bits.
        """
        return (a - b) & 0xFFFF
