class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1  # começa com uma sentinela

        for nucleotide in gene.upper():
            self.bit_string <<= 2  # desloca dois bits para a esquerda

            match nucleotide:
                case "A":
                    self.bit_string |= 0b00
                case "C":
                    self.bit_string |= 0b01
                case "G":
                    self.bit_string |= 0b10
                case "T":
                    self.bit_string |= 0b11
                case _:
                    raise ValueError("Invalid Nucleotide:{}".format(nucleotide))

    def _decompress(self) -> str:
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() -1, 2): # - 1 para excluir a sentinela
            bits: int = self.bit_string >> i & 0b11

            match bits:
                case 0b00:
                    gene += "A"
                case 0b01:
                    gene += "C"
                case 0b10:
                    gene += "G"
                case 0b11:
                    gene += "T"
                case _:
                    raise ValueError(f"Invalid bits:{bits}")
        return gene[::-1] #inverte a string usando fatiamento com inversão

    def __str__(self) -> str:
        return self._decompress()


from sys import getsizeof
original: str = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100
print(f"original is {getsizeof(original)} bytes")
compressed: CompressedGene = CompressedGene(original)

print(f"compressed is {getsizeof(compressed.bit_string)} bytes")

print(f"Original: {original}" )
print(f"Compressed: {compressed}")
print(f"Decompressed: {compressed._decompress()}")

print(f"original and decompressed are the same {original == compressed._decompress()}")

