#!/usr/bin/env python3

#################################################
# Programming project #2
#
# Name: Faith Wambui
# username: Wanjiku
# Section: 010
#
##################################################

import os

###################################################

#### your program starts here.

#Main Program
# main.py
import os
from fasta_module import FASTA
from fastq_module import FASTQ

# Utility Functions
def detect_file_type(filename):
    """
    Detect the file type (FASTA or FASTQ) and sequence type (nucleotide or peptide).

    :param filename: str, input file path
    :return: tuple, (file_type, sequence_type)
    """
    with open(filename, 'r') as file:
        first_line = file.readline().strip()
        second_line = file.readline().strip()

    if first_line.startswith('@'):
        return ('FASTQ', 'nucleotide')

    if first_line.startswith('>'):
        if all(char in 'ARNDCEQGHILKMFPSTWYV*' for char in second_line):
            return ('FASTA', 'peptide')
        elif all(char in 'ACTGN' for char in second_line):
            return ('FASTA', 'nucleotide')

    raise ValueError("Unsupported file format or content.")

def calculate_gc_content(sequence):
    """
    Calculate GC content of a nucleotide sequence.

    :param sequence: str, nucleotide sequence
    :return: float, GC content as a percentage
    """
    gc_count = sequence.count('G') + sequence.count('C')
    return (gc_count / len(sequence)) * 100 if sequence else 0

# Main Program
def main():
    print("Welcome to the Sequence Analyzer!")

    input_file = input("Please provide the input file path: ").strip()

    if not os.path.exists(input_file):
        print("Error: File not found.")
        return

    try:
        file_type, sequence_type = detect_file_type(input_file)
        print(f"Detected file type: {file_type}, Sequence type: {sequence_type}")

        if file_type == 'FASTA':
            handler = FASTA()
        elif file_type == 'FASTQ':
            handler = FASTQ()
        else:
            print("Unsupported file type.")
            return

        handler.read(input_file)

        # Metrics
        total_sequences = handler.count()
        avg_length = handler.avg_length()
        min_length = min(seq.length for seq in handler.sequences)
        max_length = max(seq.length for seq in handler.sequences)

        print("\nBasic Metrics:")
        print(f"Total number of sequences: {total_sequences}")
        print(f"Average sequence length: {avg_length:.2f}")
        print(f"Minimum sequence length: {min_length}")
        print(f"Maximum sequence length: {max_length}")

        if sequence_type == 'nucleotide':
            avg_gc_content = sum(calculate_gc_content(seq.sequence) for seq in handler.sequences) / total_sequences
            print(f"Average GC content: {avg_gc_content:.2f}%")

        # User interaction
        while True:
            print("\nOptions:")
            print("1. Convert FASTQ to FASTA (if applicable)")
            print("2. Filter sequences by minimum length")
            print("3. Filter sequences by minimum average quality (FASTQ only)")
            print("4. Exit")

            choice = input("Select an option: ").strip()

            if choice == '1':
                if file_type == 'FASTQ':
                    output_file = input("Enter the output FASTA file name: ").strip()
                    with open(output_file, 'w') as fasta_file:
                        for seq in handler.sequences:
                            fasta_file.write(f">{seq.sequence_id} {seq.description}\n{seq.sequence}\n")
                    print(f"Converted FASTQ to FASTA and saved to {output_file}")
                else:
                    print("Conversion is only applicable for FASTQ files.")

            elif choice == '2':
                min_length = int(input("Enter minimum sequence length: ").strip())
                filtered_sequences = [seq for seq in handler.sequences if seq.length >= min_length]

                output_file = input("Enter the output file name: ").strip()
                with open(output_file, 'w') as file:
                    for seq in filtered_sequences:
                        if file_type == 'FASTA':
                            file.write(f">{seq.sequence_id} {seq.description}\n{seq.sequence}\n")
                        elif file_type == 'FASTQ':
                            quality = ''.join(chr(q + 33) for q in seq.quality_scores)
                            file.write(f"@{seq.sequence_id} {seq.description}\n{seq.sequence}\n+\n{quality}\n")
                print(f"Filtered sequences saved to {output_file}")

            elif choice == '3':
                if file_type != 'FASTQ':
                    print("This option is only applicable for FASTQ files.")
                else:
                    min_quality = float(input("Enter minimum average quality: ").strip())
                    filtered_sequences = [seq for seq in handler.sequences
                                          if sum(seq.quality_scores) / len(seq.quality_scores) >= min_quality]

                    output_file = input("Enter the output file name: ").strip()
                    with open(output_file, 'w') as file:
                        for seq in filtered_sequences:
                            quality = ''.join(chr(q + 33) for q in seq.quality_scores)
                            file.write(f"@{seq.sequence_id} {seq.description}\n{seq.sequence}\n+\n{quality}\n")
                    print(f"Filtered sequences saved to {output_file}")

            elif choice == '4':
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()