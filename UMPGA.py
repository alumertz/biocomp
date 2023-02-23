global tree
tree= []
def newMatrix(dij):
    global mat
    x = dij[1]
    y = dij[2]
    tam = len(mat)

    newName = "("  + names[x] +"," + names[y] + ")"
    print ("newName " +  newName)
    
    name1 = names[x]
    name2 = names[y]

    names.remove(name1)
    names.remove(name2)
    names.insert(0,newName)    

    nDist = np.zeros(len(mat))
    for i in range (len(mat)):
        nDist[i] = (mat[x][i] +  mat[y][i]-mat[x][y])/2            

    nDist = np.delete(nDist,(x,y),0)

    mat = np.delete(mat,(x,y),0)    
    mat = np.delete(mat,(x,y),1)

    nMat= np.zeros((tam-1,tam-1))
    
    nMat[1:tam-1,0] = nDist
    nMat[0,1:tam-1] = nDist
    
    nMat[1:tam-1,1:tam-1] = mat

    mat = nMat


def joinTree(x,y):
	
	esta= 0
	global tree
	for i in tree:
		findx = tree[i].find(x)
		findy = tree[i].find(y)
		if(findx):
			esta= 1
			tree[i] = "("+tree[i]+")"+","+findx
			
		elif(findy):
			esta= 1
			tree[i] =  "("+tree[i]+")"+","+findy
		
			

	if(not esta):	
		tree.append(names[x]+","+names[y])


def findSmallest(mat):
	tam = len(mat)
	min = [mat[0][0],0,0]
	for x in range(tam):
		for y in range(tam):
			#print(min[0])
			if (mat[x][y]<min[0]):
				min=[mat[x][y],x,y]
	print(min)
	return min


if __name__ == '__main__':
	global tree
	mat = [[0,2,4,6,6,8],[2,0,4,6,6,8],[4,4,0,6,6,8],[6,6,6,4,0,8],[8,8,8,8,8,0]]
	names = ['A','B','C','D','E','F']
	min = findSmallest(mat)
	joinTree(min[1],min[2])


