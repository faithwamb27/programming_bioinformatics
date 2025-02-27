#!/usr/bin/env python3

#################################################
# Programming assignment #4
#
# Name: Faith Wambui
# username: Wanjiku
# Section: 010
#
##################################################
import random

###################################################

#### your program starts here.
#Question 1
stringA = "GGGCCGTTGGT"
stringB = "GGACCGTTGAC"
# Set the Hamming distance to 0
distance = 0
# Iterate through each character position in the strings
for i in range(len(stringA)):
    if stringA[i] != stringB[i]:
        distance += 1     #Increment the distance if the bases are different
# Print the calculated Hamming distance
print(distance)


#Question 2
with open(r'C:\Users\ADMIN\Desktop\Academia\programming_for_bioinformatics\binf690_wanjiku\hw4\input_fastq.txt', 'r') as fq, open(
        r'C:\Users\ADMIN\Desktop\Academia\programming_for_bioinformatics\binf690_wanjiku\hw4\output_fasta', 'w') as fa:
    while True:
        # Read header line
        header = fq.readline()
        if not header:
            break  # Stop if we reach the end of the file

        # Only process entries where the header starts with '@'
        if header.startswith('@'):
            sequence = fq.readline()  # Read sequence line
            plus_line = fq.readline()  # Ignore '+' line
            qs_line = fq.readline()  # Ignore quality score line

            # Writing the FASTA formatted header and sequence
            fasta_header = f'>{header[1:-1]}'  # Convert FASTQ header to FASTA header
            fasta_sequence = sequence.strip()  # Remove any trailing newline from sequence

            fa.write(f'{fasta_header}\n{fasta_sequence}\n')  # Write to FASTA file


#Question 3
S = ('TGTCAGCTACCTTGATGGATTGAGTTTGTTTCGGTCGATGCTCCATCGGGAGAGAGTCTG'
     'CGTCCTGGTCCGAGCAAGTCCCACCAAGTGGCACTTGGCGGCGCCATGTCCTATCTAGTG'
     'CCACCATGTCCGAGGACTTTGATGGCACATGGTGGCACTTGATTTGCCCAAGTCCCACCT'
     'GCTCCGACGTGGACCGACTTCGTGGCACATCGCTATCACCCACTCTACCGTTGAAAAGCC'
     'GAAGTCAAGCGCCGAAAGCTGATCGATTTGCGGTGTGATACGTTGCCAGTGATTCGTTCC'
     'GTGGTTTATGCTTGGCGCACCTACCGCGTCCCCGACGCATCGACTCCGCCGCCATTGCGC'
     'GGCACAAAACGGCCTTCGATCCTTCCGTACGGAGGGGTACTGCAGGGCTCACTGTTCATG'
     'CCGGAAATTGCACCGGCTTTTTTTTCAATCAAATCAAGTGGACCGTGTCGGATAGTGAGG'
     'ACACCGGACACCGCGATACCAAGCCGATTGGCGGTCTGTTTGTGAAAATAGACCGTAGTG'
     'CGGACAATTCCGAAGCCGGACACCGGACAGGTGCTCTGTGGAAATTCCGCGTATGCCCGA'
     'CACCCTTACAGCCGCGTGGCTGGGTGCGGATCACGAAGCCCAAAACACTGCGGCGGGGAT'
     'GATCTGACTTTGGGGTGGGGAGCTGCTTTGCGTGCCGAATGACGGCGAACGCAGGCTTCT'
     'GAGCAAATATCGATCCGGGGGGCGCCACCGGTACCAGAACGGCGCAACAGGTAATCACCC'
     'ATCACGGCAAGGGCCGCAGGCGTGTGGACGCAATCCACGCGAAGGCAGGCTCGCATCCAG'
     'AGATGCACCGGATAGGGTGGCCGCGCAAGCGGTGCGTGAGGCGAGAGCCTTGCATGTTCG'
     'CGAAGCGGACGGTCACGACGCATTGCTTCCATGCTCAGGGCCGATCGGTTTGGCATCGCT'
     'AAAGGACCGGAAGAGTGGTTGTAGGACCGGCAGGGTGGGCCGGCAAGCTGGGGGTGGTAC'
     'CCCGGTGCACCAAGCGGGCAGGGCCAATTCGGGGTTGGCGCCGCCGAGAATTGGGTTGCG'
     'CAGATTTGCGCGGCCGGCGGGATGCGCTTAGCGCGAATAGGAATCCGTC')

M = ('GGACACCGGACA', 'TCCGT', 'CGCGAA', 'CGGCGGG', 'CCGT')

motif_locations = {}  # Dictionary to store the results

# Loop over each motif in M
for motif in M:
    locations = []  # List to store start positions for current motif
    start = 0  # Starting position for search

    # Find occurrences of the motif in S
    while True:
        pos = S.find(motif, start)
        if pos == -1:  # Break the loop if motif not found
            break
        locations.append(pos)
        start = pos + 1  #Move to the next character after the found motif

    motif_locations[motif] = locations  #Store the locations for the motif

# Print the results using the 'motif_locations' dictionary directly)
print(motif_locations)

#Question 4
# Get input from the user
user_input = input("Enter a string: ")

# Process the input and check if it's a palindrome
s = user_input.replace(" ", "").lower()
is_palindrome = s == s[::-1]  # Compare the string to its reverse

# Print the result
if is_palindrome:
    print(f"'{user_input}' is a palindrome!")
else:
    print(f"'{user_input}' is not a palindrome.")

# Question 5
# import random
# Generate a random number between 1 and 9 (inclusive)
secret_number = random.randint(1, 9)

# Get the user's guess
guess = int(input("Guess a number between 1 and 9: "))

# Check the guess
if guess < secret_number:
    print("Too low!")
elif guess > secret_number:
    print("Too high!")
else:
    print("Exactly right!")

#Question 6
rna_codon_table = {
    "UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
    "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
    "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
    "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
    "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
    "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
    "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
    "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
    "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
    "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
    "UAA": "*", "CAA": "Q", "AAA": "K", "GAA": "E",
    "UAG": "*", "CAG": "Q", "AAG": "K", "GAG": "E",
    "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
    "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
    "UGA": "*", "CGA": "R", "AGA": "R", "GGA": "G",
    "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
}

# Get RNA string from the user
rna_string = (input("Enter an RNA string: ")).upper()

# Creating an empty string to store the protein sequence
protein_sequence = ""

for i in range(0, len(rna_string), 3):
    codon = rna_string[i:i + 3]
    if codon in rna_codon_table:
        amino_acid = rna_codon_table[codon]
        protein_sequence += amino_acid  # Add amino acid (including stop codon)
        if amino_acid == "*":  # Check for stop codon
            break  # Immediately exit the loop after adding the stop codon
    else:
        break  # Stop if an invalid codon is encountered

print(protein_sequence)  # Output
