def hammingDist(seq1, seq2):
    differ = 0
    for x in range(0,len(seq1)):
        if seq1[x] != seq2[x]:
            differ += 1
    return differ

fh = open('/Users/saltside/Desktop/rosalind/rosalind_hamm.txt', 'r')

seq = fh.readlines()


    



print(hammingDist(seq[0], seq[1]))
