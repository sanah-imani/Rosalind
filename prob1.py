http://rosalind.info/problems/dna/
count = [0]*4
def countNucleotides(dnaSeq):
    for nuc in dnaSeq:
        if nuc == "A":
            count[0] += 1
        elif nuc == "C":
            count[1] += 1
        elif nuc == "G":
            count[2] += 1
        else:
            count[3] += 1

    return count

print(countNucleotides("CACTAATTGGAAGGCTCTCAGGTCCGTTTAATTCCAGTCGTCCGGCGTCGAGATCGCGTTGTTTTCCGCGGCGCACTAAAACCGTCACGGCTTTCACTGACATGTCGTTCATATACATATGGCTTCGGTGCTATGAAATGGAACAAGTTTAAGGCTTCTATGTCAAAGTCCTAAAGTGCTTCGGAACTGAGCCTCTGTATGTTCACCGAGTCGACAGCCATGGTGGTTGTGAATCATGCATACACCCCCCTACAGATTTAGCCTTAATAGAGCCAATTGAGGGAGCTAGAAGTCTCTCGGAATTGCGCCATCACTCTGCACGGCTGACAGTGATCCGTCAGGTAAGTATTACCATTGACTAAGGAATAGGAAGAACCCCTTATATGCGTATACCTAGCATCATCGTAAGTACTTGCAAGGCTCGGCAACCATGCGAGAGGACCCATGCCCTGACATTGTTTCAATTACGGTTTACCAGCGGTAGTTGACATCAACTCCGCCTGTACATAAAGCTTTTGTGCGCGGCACGGACTAGATTACCGCCAAGCGACAGGGACTAACAGATTCCATTCGACTCACGCCTAGCGCTTTAGAGTCACACTGATGTACAGGCACTCGGGTCACAAGAAATGAATAGTAAGTATACAACCAAAATTTTTACCGCACACACTTAACGGGGTTACTCGGGTAGAGGCCGATCTCGCACCATCGTCGTGTCTCACATTACAAAGAGGCCGAGCATAATTCACTTAATGGATTGCAGATTGACAACAGTTTTACTGTCCGTAACAAACCGAGCTCGACCGCACCACACACGGATAAGACTCTTCTGCGTTGTGACGCGCTGGGCAATTCG"))
