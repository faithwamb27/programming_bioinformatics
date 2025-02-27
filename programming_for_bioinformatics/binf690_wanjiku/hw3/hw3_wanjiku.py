#!/usr/bin/env python3

#################################################
# Programming assignment #3
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

seq1_name = ">GWAB866TF length: 899 gc: 395 gcpercent: 0.439377085650723"
seq1_base = "GTAAGCAGGGCGGGCAAACTTTCGATGAAATGGCAGAAACTTTGCGTGGTTTTGGTTATAATATAACCGGCGCCAATGAGTTATTGAGTAATATCGATAATTCCCTTAGTGGTAAAAAGGTTGTCTCCCATGAATATGACCATACAACCGATATAGAGCAGGCCGAACAAGAACGCTATCAGGACGACGGTTACGACCTGGA"

seq2_name = ">GWAB873TF length: 802 gc: 298 gcpercent: 0.371571072319202"
seq2_base = "CATACGAGAAAGAATACCGTTTAAAAAATAAAGAACAGCTACAGGATAATTATTTTAAAAATGCTGAATATATAAAAGAACAACACAAAGATAGCATGGGAACCAGAAACAAAAGAACTCAGACGAAATTATTTGTCTCATAAATATAAAACAGATATTAATTTTAGACTAGTCAACCTTTGCAGAAACAGAATTTGGAGAG"

seq3_name = ">GWAB833TF length: 756 gc: 366 gcpercent: 0.484126984126984"
seq3_base = "ATCGGGGCCAATAGCTGTTGCAGTACCCGTGCTGGGCGGCTGTCCAATATTTGCCATCTTATTTCTCCTGTAAGGTTAAGCCCCCCGAAGGGGGCTATACCAATACTAATTAGATTGCGCTCTTAACCTGACCGCTGCCAGAACCATTCTTCGCACGCAAACCATACTCAGCAATCAAAAGCTGCTTTACACTGTCACCAGA"

seq4_name = ">GWAB856TF length: 821 gc: 472 gcpercent: 0.574908647990256"
seq4_base = "AGCCGAAGCACGAGGAATGGCGCCGGCTCATCAAGCAGTACAACCTCGACCTGAAGGTCTCCAAGCTGCCCGCCGATAAGGTGGTGAAGATCTCCCGCTTCCTACCCCTGACCCGGCAGATCATCACGTCTATCGCCTTCAATTACCCTCGCATCTTCATGCGGGTGGAAAACCAGACCATGGCCTTCCAGGCGGAGATTCT"

seq5_name = ">GWAB870TF length: 728 gc: 263 gcpercent: 0.361263736263736"
seq5_base = "CATTGCTTTAAAAGGTTGTGATTTACTTAACATTTGAACTTTGCTTGGCACTGGACCTTTACCTGTTTTTGCTGGTTCAATGACATCCTTGTAATATTTATCAGGAAATGTCATATCTAAAAATTCTTTTGTAATTAAATCTGCCATTATCGTCTCCTATCCGGTTGTAAGTCTACTTGAAAAGTTCCAAATCTCCAGTACT"

seq6_name = ">GWAB812TF length: 657 gc: 352 gcpercent: 0.535768645357686"
seq6_base = "TTGGTATCAGGGCGCAGGCAACGCAGGGAGGACCTCAAGGCAAATGATTGTCGAGAGGTCGATCCCGGTGAGAGACAGCATATGATGAAGTGGAAGGACCGGAACGTGAAGGTCCCGGAAATTTTACAGAACGATAACTTTGAGCGATCAGCCTAACAGTCCCGGATATTTGGGACGTAGGCGAAAGGACAACATGGCAGAA"

seq7_name = ">GWAB822TF length: 695 gc: 347 gcpercent: 0.499280575539568"
seq7_base = "GCCTGATGGTGTTGACACCTTTGCTGGGCCTATAGCAGTAGACATCCTTGAGGGATCGGCTGATGTCGAGATAAGGACACCTGAATAATGCCTCATGCCGTTTTTTTCTGGAAGCAGAACGATACGAGCCCAGCCTTAGAGGTCGTACTCCGAGACGGCTTTGGGTCACCGGTAAATATGACCGGGGCCACCGTTGTTTTGA"

seq8_name = ">GWAB817TF length: 699 gc: 287 gcpercent: 0.410586552217453"
seq8_base = "AATAAGCACCTCAGACGCGGAACCATTCGTTGCGCCTAGAGTCACGTTTCTTTCAGAGTTGTACGATGTGAAATCAGCCTCACTCACATAGCTTGTACTAGACGCTGAACCAGTACCGGTTTCTTTGGTGATTGTCGCCATATTTACTCCGCTGGATGCTCAAAATAACTAACTGCTATAAAAACCTTGCTTACGTTTCCAA"

seq9_name = ">GWAB858TF length: 789 gc: 373 gcpercent: 0.472750316856781"
seq9_base = "CTCAACCACCTCTCTGGCAAGCTTCCTGCACATATACTTTATATGGAAGTTACTTTTATTAAACTCCGTATGGTAGAAGGGAACTCCTTCTCCCTTATTGGAAGTATGTCCATATGAGTGTGGTGTGAAGTAAAGGATATGCTTTGCTAAATGATCGCAAAACTCTATATCCAACCAATCGTCCATGACACTAAGAATCATA"

seq10_name = ">GWAB841TF length: 941 gc: 354 gcpercent: 0.376195536663124"
seq10_base = "GAACAGTTATCTCATTGGGTTTATAAATATTTCCCCACTTTTCTTTATTTATTAATCGCAAACCATATTCCACATGAATATGCTCACGCATATAAGTATCCAACATATCCCAAGCTCGTGAGTAGGGAAATTTTTTATTATTGATTTGTGAGTTTAAAATATCTTCTTGAAGTTTGTCTCGGTCTATTTCAAAACCTTTGGG"

#### assign number of following variables.
a = 11
b = 12
c = 13
d = 14
# Assume right angle triangle with base = b and height = a return length of hypotenuse
print(f"The length of the hypotenuse of a right angle triangle with base {b} and height {a} is {((a**2 + b**2) ** 0.5)}")
#Assume a rectangle of length = c and width = d
print(f"The area of a rectangle of length{c} and width{d} is {c*d}")
print(f"The perimeter of a rectangle of length{c} and width{d} is {(2*(c+d))}")
# Assume a circle where radius=a
print(f"The area of a circle with radius{a} is {math.pi*a**2}")
print(f"The circumference of a circle with radius{a} is {3.142*a*2}")
#### list
name_lst = ["GWAB866TF", "GWAB873TF", "GWAB833TF", "GWAB856TF", "GWAB870TF", "GWAB812TF", "GWAB822TF", "GWAB817TF", "GWAB858TF", "GWAB841TF"]
base_lst = ["GTAAGCAGGGCGGGCAAACTTTCGATGAAATGGCAGAAACTTTGCGTGGTTTTGGTTATAATATAACCGGCGCCAATGAGTTATTGAGTAATATCGATAATTCCCTTAGTGGTAAAAAGGTTGTCTCCCATGAATATGACCATACAACCGATATAGAGCAGGCCGAACAAGAACGCTATCAGGACGACGGTTACGACCTGGA", "CATACGAGAAAGAATACCGTTTAAAAAATAAAGAACAGCTACAGGATAATTATTTTAAAAATGCTGAATATATAAAAGAACAACACAAAGATAGCATGGGAACCAGAAACAAAAGAACTCAGACGAAATTATTTGTCTCATAAATATAAAACAGATATTAATTTTAGACTAGTCAACCTTTGCAGAAACAGAATTTGGAGAG", "ATCGGGGCCAATAGCTGTTGCAGTACCCGTGCTGGGCGGCTGTCCAATATTTGCCATCTTATTTCTCCTGTAAGGTTAAGCCCCCCGAAGGGGGCTATACCAATACTAATTAGATTGCGCTCTTAACCTGACCGCTGCCAGAACCATTCTTCGCACGCAAACCATACTCAGCAATCAAAAGCTGCTTTACACTGTCACCAGA", "AGCCGAAGCACGAGGAATGGCGCCGGCTCATCAAGCAGTACAACCTCGACCTGAAGGTCTCCAAGCTGCCCGCCGATAAGGTGGTGAAGATCTCCCGCTTCCTACCCCTGACCCGGCAGATCATCACGTCTATCGCCTTCAATTACCCTCGCATCTTCATGCGGGTGGAAAACCAGACCATGGCCTTCCAGGCGGAGATTCT", "CATTGCTTTAAAAGGTTGTGATTTACTTAACATTTGAACTTTGCTTGGCACTGGACCTTTACCTGTTTTTGCTGGTTCAATGACATCCTTGTAATATTTATCAGGAAATGTCATATCTAAAAATTCTTTTGTAATTAAATCTGCCATTATCGTCTCCTATCCGGTTGTAAGTCTACTTGAAAAGTTCCAAATCTCCAGTACT", "TTGGTATCAGGGCGCAGGCAACGCAGGGAGGACCTCAAGGCAAATGATTGTCGAGAGGTCGATCCCGGTGAGAGACAGCATATGATGAAGTGGAAGGACCGGAACGTGAAGGTCCCGGAAATTTTACAGAACGATAACTTTGAGCGATCAGCCTAACAGTCCCGGATATTTGGGACGTAGGCGAAAGGACAACATGGCAGAA", "GCCTGATGGTGTTGACACCTTTGCTGGGCCTATAGCAGTAGACATCCTTGAGGGATCGGCTGATGTCGAGATAAGGACACCTGAATAATGCCTCATGCCGTTTTTTTCTGGAAGCAGAACGATACGAGCCCAGCCTTAGAGGTCGTACTCCGAGACGGCTTTGGGTCACCGGTAAATATGACCGGGGCCACCGTTGTTTTGA", "AATAAGCACCTCAGACGCGGAACCATTCGTTGCGCCTAGAGTCACGTTTCTTTCAGAGTTGTACGATGTGAAATCAGCCTCACTCACATAGCTTGTACTAGACGCTGAACCAGTACCGGTTTCTTTGGTGATTGTCGCCATATTTACTCCGCTGGATGCTCAAAATAACTAACTGCTATAAAAACCTTGCTTACGTTTCCAA", "CTCAACCACCTCTCTGGCAAGCTTCCTGCACATATACTTTATATGGAAGTTACTTTTATTAAACTCCGTATGGTAGAAGGGAACTCCTTCTCCCTTATTGGAAGTATGTCCATATGAGTGTGGTGTGAAGTAAAGGATATGCTTTGCTAAATGATCGCAAAACTCTATATCCAACCAATCGTCCATGACACTAAGAATCATA", "GAACAGTTATCTCATTGGGTTTATAAATATTTCCCCACTTTTCTTTATTTATTAATCGCAAACCATATTCCACATGAATATGCTCACGCATATAAGTATCCAACATATCCCAAGCTCGTGAGTAGGGAAATTTTTTATTATTGATTTGTGAGTTTAAAATATCTTCTTGAAGTTTGTCTCGGTCTATTTCAAAACCTTTGGG"]

print("#### Length of name list: " + str(len(name_lst)))
print("#### Length of base list: " + str(len(base_lst)))


#### complex Lists and Dictionaries

lst_of_D = [
    {'name': seq1_name, 'base': seq1_base},
    {'name': seq2_name, 'base': seq2_base},
    {'name': seq3_name, 'base': seq3_base},
    {'name': seq4_name, 'base': seq4_base},
    {'name': seq5_name, 'base': seq5_base},
    {'name': seq6_name, 'base': seq6_base},
    {'name': seq7_name, 'base': seq7_base},
    {'name': seq8_name, 'base': seq8_base},
    {'name': seq9_name, 'base': seq9_base},
    {'name': seq10_name, 'base': seq10_base}]

print("#### Length of list_of_D: " + str(len(lst_of_D)))


Sequences = {
    'seq1': {'name': seq1_name, 'base': seq1_base},
    'seq2': {'name': seq2_name, 'base': seq2_base},
    'seq3': {'name': seq3_name, 'base': seq3_base},
    'seq4': {'name': seq4_name, 'base': seq4_base},
    'seq5': {'name': seq5_name, 'base': seq5_base},
    'seq6': {'name': seq6_name, 'base': seq6_base},
    'seq7': {'name': seq7_name, 'base': seq7_base},
    'seq8': {'name': seq8_name, 'base': seq8_base},
    'seq9': {'name': seq9_name, 'base': seq9_base},
    'seq10': {'name': seq10_name, 'base': seq10_base}
}

#### this should print length of 10.
print("#### Length of dictionaries sequences: " + str(len(Sequences)))

# List of sequence names and bases
sequences = [
    {"name": seq1_name, "base": seq1_base},
    {"name": seq2_name, "base": seq2_base},
    {"name": seq3_name, "base": seq3_base},
    {"name": seq4_name, "base": seq4_base},
    {"name": seq5_name, "base": seq5_base},
    {"name": seq6_name, "base": seq6_base},
    {"name": seq7_name, "base": seq7_base},
    {"name": seq8_name, "base": seq8_base},
    {"name": seq9_name, "base": seq9_base},
    {"name": seq10_name, "base": seq10_base}
]

#Create keys called a, c, t and g each storing respective counts of As, Cs, Ts and Gs in the sequence bases.
#Create new key called gc which stores the count of G's plus count of C's in the sequence bases.
Sequences = {
    'seq1': {'name': "GWAB866TF", 'base': seq1_base, 'a': seq1_base.count('A'), 'c': seq1_base.count('C'),
             't': seq1_base.count('T'), 'g': seq1_base.count('G'),
             'gc': seq1_base.count('G') + seq1_base.count('C')},
    'seq2': {'name': "GWAB873TF", 'base': seq2_base, 'a': seq2_base.count('A'), 'c': seq2_base.count('C'),
             't': seq2_base.count('T'), 'g': seq2_base.count('G'),
             'gc': seq2_base.count('G') + seq2_base.count('C')},
    'seq3': {'name': "GWAB833TF", 'base': seq3_base, 'a': seq3_base.count('A'), 'c': seq3_base.count('C'),
             't': seq3_base.count('T'), 'g': seq3_base.count('G'),
             'gc': seq3_base.count('G') + seq3_base.count('C')},
    'seq4': {'name': "GWAB856TF", 'base': seq4_base, 'a': seq4_base.count('A'), 'c': seq4_base.count('C'),
             't': seq4_base.count('T'), 'g': seq4_base.count('G'),
             'gc': seq4_base.count('G') + seq4_base.count('C')},
    'seq5': {'name': "GWAB870TF", 'base': seq5_base, 'a': seq5_base.count('A'), 'c': seq5_base.count('C'),
             't': seq5_base.count('T'), 'g': seq5_base.count('G'),
             'gc': seq5_base.count('G') + seq5_base.count('C')},
    'seq6': {'name': "GWAB812TF", 'base': seq6_base, 'a': seq6_base.count('A'), 'c': seq6_base.count('C'),
             't': seq6_base.count('T'), 'g': seq6_base.count('G'),
             'gc': seq6_base.count('G') + seq6_base.count('C')},
    'seq7': {'name': "GWAB822TF", 'base': seq7_base, 'a': seq7_base.count('A'), 'c': seq7_base.count('C'),
             't': seq7_base.count('T'), 'g': seq7_base.count('G'),
             'gc': seq7_base.count('G') + seq7_base.count('C')},
    'seq8': {'name': "GWAB817TF", 'base': seq8_base, 'a': seq8_base.count('A'), 'c': seq8_base.count('C'),
             't': seq8_base.count('T'), 'g': seq8_base.count('G'),
             'gc': seq8_base.count('G') + seq8_base.count('C')},
    'seq9': {'name': "GWAB858TF", 'base': seq9_base, 'a': seq9_base.count('A'), 'c': seq9_base.count('C'),
             't': seq9_base.count('T'), 'g': seq9_base.count('G'),
             'gc': seq9_base.count('G') + seq9_base.count('C')},
    'seq10': {'name': "GWAB841TF", 'base': seq10_base, 'a': seq10_base.count('A'), 'c': seq10_base.count('C'),
             't': seq10_base.count('T'), 'g': seq10_base.count('G'),
             'gc': seq10_base.count('G') + seq10_base.count('C')}
}
print(f"Sequence Name: {Sequences['seq1']['name']}, Base: {Sequences['seq1']['base']}, A count: {Sequences['seq1']['a']}, C count: {Sequences['seq1']['c']}, T count: {Sequences['seq1']['t']}, G count: {Sequences['seq1']['g']}, GC count: {Sequences['seq1']['gc']}")
print(f"Sequence Name: {Sequences['seq2']['name']}, Base: {Sequences['seq2']['base']}, A count: {Sequences['seq2']['a']}, C count: {Sequences['seq2']['c']}, T count: {Sequences['seq2']['t']}, G count: {Sequences['seq2']['g']}, GC count: {Sequences['seq2']['gc']}")
print(f"Sequence Name: {Sequences['seq3']['name']}, Base: {Sequences['seq3']['base']}, A count: {Sequences['seq3']['a']}, C count: {Sequences['seq3']['c']}, T count: {Sequences['seq3']['t']}, G count: {Sequences['seq3']['g']}, GC count: {Sequences['seq3']['gc']}")
print(f"Sequence Name: {Sequences['seq4']['name']}, Base: {Sequences['seq4']['base']}, A count: {Sequences['seq4']['a']}, C count: {Sequences['seq4']['c']}, T count: {Sequences['seq4']['t']}, G count: {Sequences['seq4']['g']}, GC count: {Sequences['seq4']['gc']}")
print(f"Sequence Name: {Sequences['seq5']['name']}, Base: {Sequences['seq5']['base']}, A count: {Sequences['seq5']['a']}, C count: {Sequences['seq5']['c']}, T count: {Sequences['seq5']['t']}, G count: {Sequences['seq5']['g']}, GC count: {Sequences['seq5']['gc']}")
print(f"Sequence Name: {Sequences['seq6']['name']}, Base: {Sequences['seq6']['base']}, A count: {Sequences['seq6']['a']}, C count: {Sequences['seq6']['c']}, T count: {Sequences['seq6']['t']}, G count: {Sequences['seq6']['g']}, GC count: {Sequences['seq6']['gc']}")
print(f"Sequence Name: {Sequences['seq7']['name']}, Base: {Sequences['seq7']['base']}, A count: {Sequences['seq7']['a']}, C count: {Sequences['seq7']['c']}, T count: {Sequences['seq7']['t']}, G count: {Sequences['seq7']['g']}, GC count: {Sequences['seq7']['gc']}")
print(f"Sequence Name: {Sequences['seq8']['name']}, Base: {Sequences['seq8']['base']}, A count: {Sequences['seq8']['a']}, C count: {Sequences['seq8']['c']}, T count: {Sequences['seq8']['t']}, G count: {Sequences['seq8']['g']}, GC count: {Sequences['seq8']['gc']}")
print(f"Sequence Name: {Sequences['seq9']['name']}, Base: {Sequences['seq9']['base']}, A count: {Sequences['seq9']['a']}, C count: {Sequences['seq9']['c']}, T count: {Sequences['seq9']['t']}, G count: {Sequences['seq9']['g']}, GC count: {Sequences['seq9']['gc']}")
print(f"Sequence Name: {Sequences['seq10']['name']}, Base: {Sequences['seq10']['base']}, A count: {Sequences['seq10']['a']}, C count: {Sequences['seq10']['c']}, T count: {Sequences['seq10']['t']}, G count: {Sequences['seq10']['g']}, GC count: {Sequences['seq10']['gc']}")

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
set_a = set(a)
set_b = set(b)
####list of all unique elements
unique_elements = list(set_a.union(set_b))
print("Unique elements:", unique_elements)

####Get all common elements
common_elements = list(set_a.intersection(set_b)) #Elements common to a and b
print("Common elements:", common_elements)

# Get all elements (Concatenation)
all_elements = a + b  #Elements in a and b
print("All Elements:", all_elements)