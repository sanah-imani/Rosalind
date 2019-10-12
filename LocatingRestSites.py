lengths = [4,6,8,10,12]

pos = []

length = []

comp = {}

comp["A"] = "T"
comp["T"] = "A"
comp["G"] = "C"
comp["C"] = "G"

def findPalindrome(seq):
    for i in range(0,len(seq)-3):
        for j in range(0,len(lengths)):
            if (i+lengths[j])-1 <=len(seq)-1:
                
                frag = seq[i:i+lengths[j]]
                mid = ((i+lengths[j] - 1) + i)/2
                count = 0
                dec = 'Y'
                while count < lengths[j]/2:
                   
                    if seq[int(mid)-count] != comp[seq[int(mid)+1+count]]:
                        dec = 'N'
                        break
                    count += 1
                
                if dec == 'Y':
                    
                    print(str(i+1) + " " + str(lengths[j]))
dnaArray = []
idArray = []
fh = open('/Users/saltside/Desktop/rosalind/rosalind_revp.txt','r')
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
findPalindrome(dnaArray[0])


                    
                
