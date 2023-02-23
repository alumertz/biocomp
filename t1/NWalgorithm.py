import numpy as np

seq1 = input()
seq2 = input()

lseq1 = len(seq1)
lseq2 = len(seq2)

match = 2
mismatch = -2
gap = -5

mat = np.zeros((lseq1+1, lseq2+1))
matCheck = np.zeros((lseq1,lseq2))

for x in range(lseq1):
    for y in range (lseq2):
        if seq1[x] == seq2[y]:
            matCheck[x][y] = match
        else:
            matCheck[x][y]=mismatch

            
for x in range(lseq1+1):
    for y in range(lseq2+1):
        if x==0 or y==0:
            mat[x][y] = max(x,y)*gap

for x in range(1,lseq1+1):
    for y in range(1,lseq2+1):
        mat[x][y] = max(mat[x-1][y-1]+matCheck[x-1][y-1], mat[x-1][y] +gap, mat[x][y-1]+gap)

score = mat[lseq1][lseq2]
x=lseq1
y=lseq2

seq1r = ''
seq2r = ''


while x>0 or y>0:
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

match =0
for x in range (len(seq1r)):
    if seq1r[x]==seq2r[x]:
        match +=1

print("Score: " +str(score))
print ("Identidade: " + str('%.2f'%(match/len(seq1r)*100)) + "%")
print(seq1r)
print(seq2r)


