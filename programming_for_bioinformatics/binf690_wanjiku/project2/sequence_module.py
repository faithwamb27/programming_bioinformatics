# sequence.py
class Sequence:
    """
    A class to represent a biological sequence and associated information.
    """

    def __init__(self, sequence_id, description, sequence, quality_scores=None):
        """
        Initialize a Sequence object.

        :param sequence_id: str, unique identifier or name of the sequence
        :param description: str, annotation or additional information about the sequence
        :param sequence: str, the sequence itself (e.g., nucleotide or protein sequence)
        :param quality_scores: list of int or float, per-base quality scores
        """
        self.sequence_id = sequence_id
        self.description = description
        self.sequence = sequence
        self.quality_scores = quality_scores or []

    @property
    def gc_count(self):
        """
        Compute and return the GC count of the sequence.

        :return: int, number of G and C bases in the sequence
        """
        return self.sequence.upper().count('G') + self.sequence.upper().count('C')

    @property
    def length(self):
        """
        Return the length of the sequence.

        :return: int, length of the sequence
        """
        return len(self.sequence)

    def __repr__(self):
        """
        Return a string representation of the Sequence object.

        :return: str, representation of the sequence object
        """
        return (f"Sequence(ID: {self.sequence_id}, Length: {self.length}, "
                f"GC Count: {self.gc_count}, Description: {self.description})")
