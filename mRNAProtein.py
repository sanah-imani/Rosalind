codonAA = {}
aminoAcid = ['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']
numCodons = [4,2,2,2,2,4,2,3,2,6,1,2,4,2,6,6,4,4,1,2]
def builtDict():
    index = 0
    for AA in aminoAcid:
        codonAA[AA] = numCodons[index]
        index += 1

def numMRNA(seq):
    totComb = 3
    for AA in seq:
        totComb = totComb * codonAA[AA]
    print(totComb)
    rem = divmod(totComb, 1000000)
    print(rem)


builtDict()
print(codonAA)
numMRNA("MCHCAICFRDPQQSTWAPAESCNVHYNNPPYSKVGERDDCTFTVVSEMSMCHKWKHKCSCRNIGTNKATPTESEWAKTTGPFELSIMINNSFWEYHINKVHAFRMERAGQEGRADSLKQGIWIHPEETEQVKTLQKSHRAYRCFNSHIACSTNWDCQSWTNTNVAGADCVLWSEVWNRTARPNIDNWVYSHMIGWPKWAMFGWDRKITRTLHRSQHIPEFQVEMNYHYCPTQPFTIVDDPCFKIQAWDRAWEMWRWVMEFDPSWPMLECHTIRQSKHRNGCIHITGMNRKNCRMQVSYKFKDTEKYIGRVRWIEMYNLPIPPGGMHQEYEETNLGYWYGGFVHIDTHNSKQCPVMTEPRFERFWDMAAQEKHEMTPGFQYTYCKHWYWWFIFDLMCFIQYPLWGSNPCFVTCAGNKNDLNFFAQIMMGRVYMQKNRHQILWAYMIMTDAQGEVYNEGCNKANCLEHLDVHQCTNVVTAMYEWVHNVEPKVKSYHHIHILIPCNAAQQLLQMFIQYDTTITVGMTLAQATGDQMLSQIIGCRVSKCAVKWHPTTLARINLDIEMNPTMYMMCSYEFPFGHLRDCMHVYACFAMEKYVPNQNWLPIHVCWCRKSKKNDAYIGTPPCVAGTPYGRYCCWWTCNQAWSTYVRGQPDWYYAVKHWRSRNRKAFYTWAEKMAEHQHKYSGKNKHTNSDASFSFLWGQPPIIVWYGAKVEFAHFHPYNQFAATHYNVFSHHTSGQLHNPSHSLGIKAAEADNAVQTEIPYQAELCWAFHVKNCPDTRIWWAEQDDRQINFWWPNRKNNWENTNIIWLDGDAGMRCANRYWICCFFSAGGLPCDLGIRPTCPILWTRPKLLPNIGSAGAWGWEDTKCNCIERQIHNGWDEIHEHFGCMVQSTIGNPLMCPMTKQWYQSHRGWCIETVEDIHYGCCHPEQKMLRDDGWRANNVVLYSDYLSDSAHLPQSDSHAMDYWGSSLKEYAILTNHGTGSTILIKNISNLCTWE")
                
            
