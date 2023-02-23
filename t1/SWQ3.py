import numpy as np

def backtrack (x,y,mat, matCheck, seq1,seq2,gap):
    seq1r = ''
    seq2r = ''
    last = mat[x][y]
    while last>0:
        if(x>0 and y>0 and mat[x][y] == mat[x-1][y-1]+ matCheck[x-1][y-1]):
            seq1r=seq1[x-1]+ seq1r
            seq2r=seq2[y-1]+ seq2r
            x -=1
            y-=1
        elif x>0 and mat[x][y]==mat[x-1][y]+gap:
            seq1r  = seq1[x-1] + seq1r
            seq2r = "_" +seq2r
            x -=1
        else:
            seq1r = "_"+seq1r
            seq2r = seq2[y-1]+seq2r
            y-=1
        last = mat[x][y]
        
    return seq1r,seq2r

def id(seq1,seq2):
    match =0
    for x in range (len(seq1)):
        if seq1[x]==seq2[x]:
            match +=1
            
    return '%.2f'%(match/len(seq1)*100)

def main():
    seq1 = input()
    seq2 = input()

    lseq1 = len(seq1)
    lseq2 = len(seq2)

    match = 1
    mismatch = -1
    gap = -2

    mat = np.zeros((lseq1+1, lseq2+1))
    matCheck = np.zeros((lseq1,lseq2))

    for x in range(lseq1):
        for y in range (lseq2):
            if seq1[x] == seq2[y]:
                matCheck[x][y] = match
            else:
                matCheck[x][y]=mismatch

    maxs =0
    for x in range(1,lseq1+1):
        for y in range(1,lseq2+1):
            mat[x][y] = max(mat[x-1][y-1]+matCheck[x-1][y-1], mat[x-1][y] +gap, mat[x][y-1]+gap,0)
            maxs = max(maxs,mat[x][y])
            

    print("Score: " +str(maxs)+'\n')

    for x in range(1,lseq1+1):
        for y in range(1,lseq2+1):
            if mat[x][y]==maxs:
                seq = backtrack(x,y,mat, matCheck, seq1,seq2,gap)
                identidade = id(seq[0],seq[1])
                print ("Identidade: " + str(identidade)+"%")
                print(seq[0])
                print(seq[1])
                print("")

main()


