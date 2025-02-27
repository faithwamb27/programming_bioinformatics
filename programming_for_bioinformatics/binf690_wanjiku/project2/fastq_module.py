# fastq.py
from sequence_module import Sequence

class FASTQ:
    """
    A class to handle FASTQ file operations, inheriting from the Sequence module.
    """

    def __init__(self):
        """
        Initialize a FASTQ object with storage for sequences.
        """
        self.sequences = []

    def read(self, filename):
        """
        Read a FASTQ file and populate Sequence instances.

        :param filename: str, path to the FASTQ file
        """
        with open(filename, 'r') as file:
            while True:
                header = file.readline().strip()
                if not header:
                    break  # End of file

                sequence = file.readline().strip()
                plus_line = file.readline().strip()  # '+' line (ignored here)
                quality = file.readline().strip()

                sequence_id = header[1:].split()[0]  # Remove '@' and take the first part as ID
                description = " ".join(header[1:].split()[1:])  # Everything after the first part as description
                quality_scores = [ord(char) - 33 for char in quality]  # Convert Phred quality to numerical scores

                self.sequences.append(
                    Sequence(sequence_id=sequence_id,
                             description=description,
                             sequence=sequence,
                             quality_scores=quality_scores)
                )

    def write(self, filename=None):
        """
        Write sequences to a file or display them in FASTQ format.

        :param filename: str or None, output file path or None to print to screen
        """
        output = []
        for seq in self.sequences:
            quality = ''.join(chr(score + 33) for score in seq.quality_scores)
            output.append(f"@{seq.sequence_id} {seq.description}\n{seq.sequence}\n+\n{quality}")

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
    fastq = FASTQ()
    fastq.read("C:/Users/ADMIN/Desktop/Academia/programming_for_bioinformatics/binf690_wanjiku/project2/small_sample.fastq")  # Replace with your FASTQ file path
    fastq.write()
    print("Total sequences:", fastq.count())
    print("Average length:", fastq.avg_length())

