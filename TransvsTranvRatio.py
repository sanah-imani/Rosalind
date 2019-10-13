#http://rosalind.info/problems/tran/


comp = {}

comp["A"] = "G"
comp["G"] = "A"
comp["T" ] = "C"
comp["C"] = "T"
def ratio(seq1,seq2):
    transitions = 0
    tranversions = 0
    same = 0
    for i in range(0, len(seq1)):
        
        if seq1[i] == seq2[i]:
            same += 1
        elif seq1[i] == comp[seq2[i]]:
            
            transitions += 1
        else:
            tranversions += 1
    return (transitions/tranversions)

print(ratio("GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGAAGTACGGGCATCAACCCAGTT","TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGCGGTACGAGTGTTCCTTTGGGT")) 
    
dnaArray = []
idArray = []

fh = open('/Users/saltside/Desktop/rosalind/rosalind_tran.txt','r')
line = fh.readline()
meta = ''
sequence = ''
x = 0 
while line:
    line = line.rstrip('\n')
    if '>' in line:
        idArray.append(line[1:])
        if sequence != '':
           dnaArray.append(sequence)
        sequence = ''
    else:
        sequence = sequence + line
    line = fh.readline()

print(ratio(dnaArray[0],dnaArray[1]))
