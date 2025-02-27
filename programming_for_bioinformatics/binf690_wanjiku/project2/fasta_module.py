# fasta.py
from sequence_module import Sequence

class FASTA:
    """
    A class to handle FASTA file operations, inheriting from the Sequence module.
    """

    def __init__(self):
        """
        Initialize a FASTA object with storage for sequences.
        """
        self.sequences = []

    def read(self, filename):
        """
        Read a FASTA file and populate Sequence instances.

        :param filename: str, path to the FASTA file
        """
        with open(filename, 'r') as file:
            sequence_id = None
            description = None
            sequence_data = []

            for line in file:
                line = line.strip()
                if line.startswith('>'):
                    if sequence_id is not None:
                        self.sequences.append(
                            Sequence(sequence_id=sequence_id,
                                     description=description,
                                     sequence=''.join(sequence_data))
                        )
                    header = line[1:].split(maxsplit=1)
                    sequence_id = header[0]
                    description = header[1] if len(header) > 1 else ""
                    sequence_data = []
                else:
                    sequence_data.append(line)

            # Append the last sequence if file doesn't end with '>'
            if sequence_id is not None:
                self.sequences.append(
                    Sequence(sequence_id=sequence_id,
                             description=description,
                             sequence=''.join(sequence_data))
                )

    def write(self, filename=None):
        """
        Write sequences to a file or display them in FASTA format.

        :param filename: str or None, output file path or None to print to screen
        """
        output = []
        for seq in self.sequences:
            output.append(f">{seq.sequence_id} {seq.description}\n{seq.sequence}")

        if filename:
            with open(filename, 'w') as file:
                file.write('\n'.join(output))
        else:
            print('\n'.join(output))

    def count(self):
        """
        Return the total number of sequences.

        :return: int, count of sequences
        """
        return len(self.sequences)

    def avg_length(self):
        """
        Return the average length of all sequences.

        :return: float, average length of sequences
        """
        if not self.sequences:
            return 0.0
        total_length = sum(seq.length for seq in self.sequences)
        return total_length / len(self.sequences)

# Example usage
if __name__ == "__main__":
    fasta = FASTA()
    fasta.read("C:/Users/ADMIN/Desktop/Academia/programming_for_bioinformatics/binf690_wanjiku/project2/small_sample_mix_format.fasta") # Replace with your FASTA file path
    fasta.write()
    print("Total sequences:", fasta.count())
    print("Average length:", fasta.avg_length())
