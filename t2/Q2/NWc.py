import numpy as np

def needleman_wunsch(seq1,seq2):
    match=1
    mismatch=-1
    gap=-2

    lseq1 = len(seq1)
    lseq2 = len(seq2)
    mat=[]
    for x in range(lseq1+1):
        mat.append([])
        for y in range(lseq2+1):
            if x==0 or y==0:
                mat[x].append(max(x,y)*gap)
            else:
                mat[x].append(0)

    for i in range(1, lseq1):
        for j in range(1, lseq2):
            if seq1[i-1] == seq2[j-1]:
                score = match
            else:
                score = mismatch
            mat[i][j] = max(mat[i-1][j-1] + score,
                               mat[i-1][j] + gap,
                               mat[i][j-1] + gap)

    score = mat[lseq1-1][lseq2-1]
    return score


if __name__ == '__main__':
    
    seq= []
    for i in range(10):
        file = open("seq/seq_"+str(i+1)+".fna", "r")
        seq.append(file.read())
        seq[i]=seq[i][2:]

    print(seq[0][0:5])

    seq[0] = seq[0][9482:9732]
    seq[1] = seq[1][177903:178153]
    seq[2] = seq[2][3519919:3520169]
    seq[3] = seq[3][1490249:1490499]
    seq[4] = seq[4][731123:731373]
    seq[5] = seq[5][682942:683192]
    seq[6] = seq[6][454284:454434]
    seq[7] = seq[7][15079:15329]
    seq[8] = seq[8][234103:234353]
    seq[9] = seq[9][253:503]

    
    for i in range (10):
        for j in range(10):
            if (i!=j):
                score = needleman_wunsch(seq[i],seq[j])
                print ("seq_"+str(i+1)+" vs seq_"+str(j+1)+ ": ",score)

    # for i in range (10):
    #     for j in range(10):
    #         if (i!=j):
    #             score = needleman_wunsch(seq[i],seq[j])
    #             print (score,"\t", end=' ')
    #         else:
    #             print("0","\t", end=' ') 
    #     print("\n")           

    
    

