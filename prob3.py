

def Compliment(seq):
    comp = ""
    for nuc in seq:
        if nuc == "A":
            comp += "T"
        elif nuc == "G":
            comp += "C"
        elif nuc == "C":
            comp += "G"
        else:
            comp += "A"
    return comp

def reverse(comp):
    rev = ""
    num = len(comp)-1
    while num >= 0:
        rev += comp[num]
        num = num - 1
    return rev

print(reverse(Compliment("TCTTGGGGGTTAACACGCTGCGTACACGTCCTCGCTATGGTAAAGTCTTACACGAAACGCGCAGACCCGTCTGCCGGCGTGCAAACTATGTACTGCGGCACTGTAGTGGTTAGGTTGGCCTGAAGAGGGATAACTCTCATCGGGCCATTCCCAGACAGAGGAGCCCTAACCTTTCGCACCTACGTGTATCGTAATACTGCAACCCAGTCCCCCTCTACATACATTAAATTTGAATGGGAGCAATAGTCCCCCCCGCCTACTCATCCTAAACATCTTAGGTCGTCGGGTCTCAAACTTCAGATCGTGCGCCTCTTTTACACCAAGGTCTTCTAAGCCGGCGATTTAATGGTTACCCTACATTATGTGAGTTGCTCTGCAAGCCAGGGTAGTCGCCTGTCTTGGTTATCCAGAGGTCATCGCGACCAGTTGATGGCCTCAACGGTATCGGTGGCTCCATTTTCACTTGCTATATCCTATGGGCCCCCAACTACCTTGTATGTGATTCAGCCGCAGCCGTACAAATCTTGCCGTTAGGGTGAGACCAAGAGCACGGCATTGCCACTCGACTAGACCTCGACCGTACGTGCAGATAAACTTGGCGATTGACTGAGAATTCAGCCTTAATTTCTGTGCAGGCGCTGGTACTATAGCCTATTAAAAGTAACGGGTGGTCTAGCTTCACGCGACACCTACTCCGCTGTGGTCCGGCTTGACGCTAGAACTACTCAAGGCATAGGAGCGTCTGTTGGTCTACCCGCCCAGCTGCGAACGCTAGAGCTGGGGTGGGTTATCGGGCACATAACATGAGAAGGATACTGCTAAAGACATCCTCAGCTTGTGGTGATAGTCTTGTCAACTGACTTGTACCAAGGGGCCAATGTGAAG")))
