#!/usr/bin/env python3

#################################################
# Programming project #1
#
# Name: Faith Wambui
# username: Wanjiku
# Section: 010
#
##################################################

import sys
import pprint
import math
import re

###################################################

#### your program starts here.

# Goal 1

file_path = r"C:\Users\ADMIN\Desktop\Academia\programming_for_bioinformatics\binf690_wanjiku\project1\stop_receiving.fastq"
# Open the input file
with open(file_path, 'r') as f:
# Read the first line
    first_line = f.readline().strip()  # Remove any leading/trailing whitespace

# Check the first character of the first line
if first_line.startswith('>'):
    print("Input file is in FASTA format")
    file_type = "FASTA"
elif first_line.startswith('@'):
    print("Input file is in FASTQ format")
    file_type = "FASTQ"
else:
    print("Unknown file format")
    file_type = None

# Goal 2
# Specify the input file path
file_path = r"C:\Users\ADMIN\Desktop\Academia\programming_for_bioinformatics\binf690_wanjiku\project1\stop_receiving.fastq"

# Initialize variables for statistics
total_sequences = 0
total_length = 0
base_counts = {'A': 0, 'C': 0, 'T': 0, 'G': 0, 'N': 0}
most_ns_count = 0  # Initialize most_ns_count
sequence_with_most_ns = ""  # Initialize sequence_with_most_ns

# Open the FASTQ file for reading
with open(file_path, 'r') as f:
    while True:
        header = f.readline().strip()  # Read the sequence header
        if not header:  # End of file
            break

        sequence = f.readline().strip()  # Read the sequence line
        f.readline()  # Read and ignore the "+" line
        quality = f.readline().strip()  # Read the quality line

        # Calculate sequence and base statistics
        total_sequences += 1
        seq_length = len(sequence)
        total_length += seq_length
        base_counts['A'] += sequence.count('A')
        base_counts['C'] += sequence.count('C')
        base_counts['T'] += sequence.count('T')
        base_counts['G'] += sequence.count('G')
        base_counts['N'] += sequence.count('N')

        n_count = sequence.count('N')
        if n_count > most_ns_count:
            most_ns_count = n_count
            sequence_with_most_ns = sequence

# Calculate percentage of each base across the library (excluding 'N')
total_bases = sum(base_counts[base] for base in ['A', 'C', 'T', 'G'])
percentages = {base: (count / total_bases) * 100 for base, count in base_counts.items() if base in ['A', 'C', 'T', 'G']}

# Output results
print(f"Total number of sequences: {total_sequences}")
print(f"Average sequence length: {total_length / total_sequences if total_sequences else 0:.2f}")
print(f"Sequence with the most 'N's: {sequence_with_most_ns}")
print(f"Number of 'N's: {most_ns_count}")
print("Percentage of bases (A, C, T, G):")
for base, perc in percentages.items():
    print(f"  {base}: {perc:.2f}%")


# Goal 3
# Specify the input and output file paths
input_file_path = r"C:\Users\ADMIN\Desktop\Academia\programming_for_bioinformatics\binf690_wanjiku\project1\stop_receiving.fastq"
output_file_path = r"C:\Users\ADMIN\Desktop\Academia\programming_for_bioinformatics\binf690_wanjiku\project1\stop_receiving_trimmed_sequences.fastq"

# Define quality threshold and minimum length
quality_threshold = 30  # input for minimum per-base quality.
min_length = 50         # input for minimum sequence length

# Open the input FASTQ file and the output file
with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
    while True:
        header = infile.readline().strip()
        if not header:  # Break if the end of the file is reached
            break
        seq = infile.readline().strip()  # Read the sequence
        plus_line = infile.readline().strip()  # Plus line '+'
        quality = infile.readline().strip()  # Quality scores

        # Convert quality scores to numerical values (Phred+33)
        quality_scores = [ord(char) - 33 for char in quality]

        # Trim the sequence based on quality
        start_index = 0
        end_index = len(seq)

        # Trim from the start (left side)
        while start_index < len(seq) and quality_scores[start_index] < quality_threshold:
            start_index += 1

        # Trim from the end (right side)
        while end_index > start_index and quality_scores[end_index - 1] < quality_threshold:
            end_index -= 1

        # Get the trimmed sequence
        trimmed_seq = seq[start_index:end_index]

        # Check if the trimmed sequence meets the minimum length requirement
        if len(trimmed_seq) >= min_length:
            # Write the trimmed sequence to the output file
            outfile.write(f"{header}\n{trimmed_seq}\n{plus_line}\n{quality[start_index:end_index]}\n")

# Print a confirmation message
print(f"Trimmed sequences have been written to {output_file_path}.")

# Goal 4
# Specify the input and output file paths
input_file_path = r"C:\Users\ADMIN\Desktop\Academia\programming_for_bioinformatics\binf690_wanjiku\project1\stop_receiving.fastq"
output_file_high_quality = r"C:\Users\ADMIN\Desktop\Academia\programming_for_bioinformatics\binf690_wanjiku\project1\stop_receiving_high_quality_sequences.fastq"
output_file_low_quality = r"C:\Users\ADMIN\Desktop\Academia\programming_for_bioinformatics\binf690_wanjiku\project1\stop_receiving_low_quality_sequences.fastq"

# Define the average quality threshold
average_quality_threshold = 20  # Replace with your input for average sequence quality

# Open the input FASTQ file and the output files
with open(input_file_path, 'r') as infile, open(output_file_high_quality, 'w') as outfile_high, open(output_file_low_quality, 'w') as outfile_low:
    while True:
        header = infile.readline().strip()
        if not header:  # Break if the end of the file is reached
            break
        seq = infile.readline().strip()  # Read the sequence
        plus_line = infile.readline().strip()  # Plus line '+'
        quality = infile.readline().strip()  # Quality scores

        # Convert quality scores to numerical values (Phred+33)
        quality_scores = [ord(char) - 33 for char in quality]

        # Calculate the average quality score
        average_quality = sum(quality_scores) / len(quality_scores) if quality_scores else 0

        # Write the sequence to the output file based on average quality
        if average_quality >= average_quality_threshold:
            outfile_high.write(f"{header}\n{seq}\n{plus_line}\n{quality}\n")
        else:
            outfile_low.write(f"{header}\n{seq}\n{plus_line}\n{quality}\n")

# Print confirmation messages
print(f"High-quality sequences have been written to {output_file_high_quality}.")
print(f"Low-quality sequences have been written to {output_file_low_quality}.")

