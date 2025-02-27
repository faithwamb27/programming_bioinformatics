#!/usr/bin/env python3

#################################################
# Programming assignment #5
# Name: Faith Wambui
# username: Wanjiku
# Section: 010
#
##################################################


###################################################

#### your program starts here.

#Question 1
def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)

def print_fibonacci_sequence(n):
    sequence = [fibonacci(i) for i in range(n)]
    print(", ".join(map(str, sequence)))

# Example
n = 6
print_fibonacci_sequence(n)

#Question 2
def compress_dna(dna):
    compressed = []
    count = 1

    for i in range(1, len(dna)):
        if dna[i] == dna[i - 1]:
            count += 1
        else:
            compressed.append(f"{dna[i - 1]}{count}")
            count = 1

    compressed.append(f"{dna[-1]}{count}")  # Add the last nucleotide and its count
    return "".join(compressed)


def decompress_dna(compressed_dna):
    decompressed = []
    i = 0

    while i < len(compressed_dna):
        nucleotide = compressed_dna[i]
        count = ""
        i += 1

        # Gather all digits following the nucleotide
        while i < len(compressed_dna) and compressed_dna[i].isdigit():
            count += compressed_dna[i]
            i += 1

        decompressed.append(nucleotide * int(count))

    return "".join(decompressed)


# Example Input
dna = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCG"

# Compression
compressed_dna = compress_dna(dna)
print("Compressed DNA:", compressed_dna)

# Decompression
decompressed_dna = decompress_dna(compressed_dna)
print("Decompressed DNA:", decompressed_dna)

# Validation
assert decompressed_dna == dna, "Decompression failed!"

#Question 3
def pig_latin_encrypt(text):
    vowels = "aeiouAEIOU"
    words = text.split()
    encrypted_words = []

    for word in words:
        if word[0] in vowels:
            encrypted_words.append(word + "ay")
        else:
            encrypted_words.append(word[1:] + word[0] + "ay")

    return " ".join(encrypted_words)


def pig_latin_decrypt(encrypted_text):
    words = encrypted_text.split()
    decrypted_words = []

    for word in words:
        if word.endswith("ay"):
            stripped_word = word[:-2]  # Remove 'ay' from the end
            if stripped_word[0] in "aeiouAEIOU":  # Likely vowel-start rule
                decrypted_words.append(stripped_word)
            else:  # Likely consonant-start rule
                decrypted_words.append(stripped_word[-1] + stripped_word[:-1])  # Move last letter to front

    return " ".join(decrypted_words)


# Example
text = "hello apple world this is pig latin"

# Encryption
encrypted_text = pig_latin_encrypt(text)
print("Encrypted Text:", encrypted_text)

# Decryption
decrypted_text = pig_latin_decrypt(encrypted_text)
print("Decrypted Text:", decrypted_text)

#Question 4
def caesar_cipher_encrypt(plaintext, shift):
    encrypted_text = []

    for char in plaintext:
        if char.isalpha():  # Encrypt only alphabetic characters
            # Determine if it's uppercase or lowercase
            base = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around using modulo 26
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_text.append(encrypted_char)
        else:
            # For non-alphabetic characters, keep them unchanged
            encrypted_text.append(char)

    return "".join(encrypted_text)


def caesar_cipher_decrypt(ciphertext, shift):
    decrypted_text = []

    for char in ciphertext:
        if char.isalpha():  # Decrypt only alphabetic characters
            # Determine if it's uppercase or lowercase
            base = ord('A') if char.isupper() else ord('a')
            # Shift character back by N positions and wrap around using modulo 26
            decrypted_char = chr((ord(char) - base - shift) % 26 + base)
            decrypted_text.append(decrypted_char)
        else:
            # For non-alphabetic characters, keep them unchanged
            decrypted_text.append(char)

    return "".join(decrypted_text)


# Example usage
plaintext = "Hello World! This is Caesar Cipher."
shift = 2

# Encryption
encrypted_text = caesar_cipher_encrypt(plaintext, shift)
print("Encrypted Text:", encrypted_text)

# Decryption
decrypted_text = caesar_cipher_decrypt(encrypted_text, shift)
print("Decrypted Text:", decrypted_text)

# Validation
assert decrypted_text == plaintext, "Decryption failed!"

#Question 5
# Define the file path at the top
fasta_filename = r"C:\Users\ADMIN\Desktop\Academia\programming_for_bioinformatics\binf690_wanjiku\hw5\contigs.fasta"  # File path
min_length = 5  # Minimum motif length (N length)

def read_fasta(fasta_filename):
    """
    Reads a FASTA file and returns a list of protein sequences.
    """
    sequences = []
    try:
        with open(fasta_filename, 'r') as f:
            seq = ""
            for line in f:
                if line.startswith(">"):  # Skip the header lines (FASTA format)
                    if seq:  # Add the previous sequence to the list
                        sequences.append(seq)
                    seq = ""  # Start a new sequence
                else:
                    seq += line.strip()  # Append sequence data
            if seq:  # Add the last sequence
                sequences.append(seq)
    except Exception as e:
        print(f"Error reading file {fasta_filename}: {e}")

    return sequences


def find_common_motif(sequences, min_length):
    """
    Finds a common motif of at least `min_length` across all sequences.
    """
    if not sequences:
        print("Error: No sequences found.")
        return set()

    # Start by taking substrings from the first sequence
    first_sequence = sequences[0]
    common_motifs = set()

    # Iterate over all substrings of length `min_length` or more in the first sequence
    for i in range(len(first_sequence) - min_length + 1):
        substring = first_sequence[i:i + min_length]

        # Check if this substring is present in all other sequences
        is_common = all(substring in seq for seq in sequences)

        # If common, add it to the set
        if is_common:
            common_motifs.add(substring)

    return common_motifs


# Step 1: Read the protein sequences from the FASTA file
sequences = read_fasta(r"C:\Users\ADMIN\Desktop\Academia\programming_for_bioinformatics\binf690_wanjiku\hw5\contigs.fasta")

# Step 2: Find common motifs of at least `min_length` in all sequences
common_motifs = find_common_motif(sequences, 4)

# Output the result
if common_motifs:
    print("Common motifs found:")
    for motif in common_motifs:
        print(motif)
else:
    print("No common motifs found.")

#Question 6
def rev(dna_string):
    """
    Returns the reverse of the input DNA string.
    """
    return dna_string[::-1]  # Reverse the string

def comp(dna_string):
    """
    Returns the complementary DNA strand for the input DNA string.
    In DNA, 'A' pairs with 'T', and 'C' pairs with 'G'.
    """
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in dna_string)

def revcomp(dna_string):
    """
    Returns the reverse complement of the input DNA string.
    Uses the `rev()` and `comp()` functions.
    """
    return comp(rev(dna_string))  # Reverse the string and then find the complement
# Example
# Example DNA sequence
dna = "GTCA"

# Get the reverse of the DNA string
print("Reverse:", rev(dna))  # Output: "ACTG"

# Get the complement of the DNA string
print("Complement:", comp(dna))  # Output: "CAGT"

# Get the reverse complement of the DNA string
print("Reverse Complement:", revcomp(dna))  # Output: "TGAC"

#Question 7
# Function to get the reverse complement of a DNA string
def rev(dna_string):
    """
    Returns the reverse of the input DNA string.
    """
    return dna_string[::-1]  # Reverse the string

def comp(dna_string):
    """
    Returns the complementary DNA strand for the input DNA string.
    In DNA, 'A' pairs with 'T', and 'C' pairs with 'G'.
    """
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in dna_string)

def revcomp(dna_string):
    """
    Returns the reverse complement of the input DNA string.
    Uses the `rev()` and `comp()` functions.
    """
    return comp(rev(dna_string))  # Reverse the string and then find the complement

# Function to find all occurrences of a substring (needle) in a larger string (haystack)
def find_all_occurrences(haystack, needle):
    """
    Finds all occurrences of the substring (needle) in the larger string (haystack).
    Returns a list of starting indices.
    """
    positions = []
    start = 0
    while True:
        start = haystack.find(needle, start)
        if start == -1:
            break
        positions.append(start)
        start += 1  # Move to the next character after the current match
    return positions

# Example DNA strings P and C
P = "CTTAAAAGCG"
C = "CGCTTTTAAGACTTAAAAGCGTTTGCTATGGACCTTAAAAGCGATCCACTTAAAAGCGTCTTAAAAGCGAACTTAAAAGCGGCGATTTGTCCTGCCTGAGTGCGGAATCAGAGGTTGATGTGTTGATGGACTCGAGTCATACAAGCGGAACTAGATACGGGGGGACTTCACCTGCGTTCTCAACTGCAGATCTAGAAGTGTTGATGTAGCTAGCACTCCAGAACGACTGTTTAACTTGGAGACCTCTCGTACAACATTTCGTTTCCGACACCCGTGTATAGGCGTCAAGAACGGAACCCGTATCTTAGAGGGGGATTCTCTTTTCTTACTCAAATTTGTGGCGGAATAACCGCGAATGAATCAACTGTATGCGGCTCTACTATGTGTAGATCATTTCGCATCAGCACCCAGAGCGCCCAGTGCAATACTGGTTGCCAGTTGCGCTGTATCCTTGACCCAGATGATAGTCCTAGGATCTAGGCCCGCGCAAACACCCTAACAACTAGTTATCCCAACATTCGCCGCCAAAAGGGTCAACAAGAGCGGGGCTGGAACTTCATCGCTTTTGCTATGAGGTTAAAACATCGGTACAGAGAACCCCCGGTGCAGGGAGGGGATGGGTATTGGGAACAAGATATACGAGCCGGAGCAAAGCGTCATTACCCATGTGTAGGAACACGGGGTTCAAAGTAGTCCACAATCCACGATCGATTCCCATGAACCTGGCCATATGAGCCAAGTCGTACTATAAGAAGCCTCTCCGCGCCTACGCCGCACGTTTTAAGGCCGTTTATCTTCCGTGATACTGGGTCGGTGTGC"

# Step 1: Find the reverse complement of P
rev_comp_P = revcomp(P)
print("Reverse complement of P:", rev_comp_P)

# Step 2: Find all occurrences of P in C and print their starting locations
occurrences_P = find_all_occurrences(C, P)
print("Occurrences of P in C at positions:", occurrences_P)

# Step 3: Find all occurrences of the reverse complement of P in C and print their starting locations
occurrences_rev_comp_P = find_all_occurrences(C, rev_comp_P)
print("Occurrences of reverse complement of P in C at positions:", occurrences_rev_comp_P)




