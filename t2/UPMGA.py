import numpy as np

global tree

def newMatrix(dij):
    global mat
    x = dij[1]
    y = dij[2]
    tam = len(mat)

    newName = "(" + names[x]+","+names[y]+ ")"
    
    name1 = names[x]
    name2 = names[y]

    names.remove(name1)
    names.remove(name2)
    names.insert(0,newName)    

    nDist = np.zeros(len(mat))
    for i in range (len(mat)):
        nDist[i] = (mat[x][i] +  mat[y][i])/2            

    nDist = np.delete(nDist,(x,y),0)

    mat = np.delete(mat,(x,y),0)    
    mat = np.delete(mat,(x,y),1)

    nMat= np.zeros((tam-1,tam-1))
    
    nMat[1:tam-1,0] = nDist
    nMat[0,1:tam-1] = nDist
    
    nMat[1:tam-1,1:tam-1] = mat

    mat = nMat

def joinTree(x,y):
    global tree
    findx = tree.find(x)
    findy = tree.find(y)

    print(x, findx, y, findy, tree)

    if (findx !=-1 and findy!=-1):
        print("e1")
        tree = tree.replace(x,"")
        tree = tree.replace(y,"")
        tree = tree.replace(",","")
        if (len(tree)>0):
            tree = "("+x+","+y+"),"+tree
        else:
            tree = "("+x+","+y+")"
    elif(findx !=-1):
        print("e2")
        tree =  tree[0:findx] + "("+ tree[findx:findx+len(x)] + "," +y + ")" + tree[findx+len(x):len(tree)]

    elif(findy !=-1):
        print("e3")
        tree =  tree[0:findy] + "("+ tree[findx:findy+len(y)] + "," +x + ")"+ tree[findy+len(x):len(tree)]

    elif(len(tree)==0):
        print("e4")
        tree = "("+ x + ","+ y + ")"
    else:
        print("e5")
        tree = tree+ "," + "("+ x + ","+ y + ")"


def findSmallest(mat):
	tam = len(mat)
	min = [mat[0][1],0,1]
	for x in range(tam):
		for y in range(tam):
			#print(min[0])
			if (mat[x][y]<min[0] and x!=y):
				min=[mat[x][y],x,y]
	#print(min)
	return min


if __name__ == '__main__':
	
    #mat = [[0,2,4,6,6,8],[2,0,4,6,6,8],[4,4,0,6,6,8],[6,6,6,0,4,8],[6,6,6,4,0,8],[8,8,8,8,8,0]]
    #names = ['A','B','C','D','E','F']

    #mat = [[0,7,9,11],[7,8,5,13],[9,5,0,9],[11,13,9,0]]
    #names = ['A','B','C','D']

    #mat = [[0,3,4,2,7],[3,0,4,6,3],[4,4,0,5,8],[2,6,5,0,6],[7,3,8,6,0]]
    #names = ['A','B','C','D','E']

    #mat = [[0,20,60,100,90],[20,0,50,90,80],[60,50,0,90,80],[100,90,40,0,30],[90,90,50,30,0]]
    #names = ['A','B','C','D','E']
    
    #mat = [[0,3,4,3],[3,0,4,5],[4,4,0,2],[3,5,2,0]]
    #names = ['i','j','k','l']

    #mat = [[0,5,9,9,8],[5,0,10,10,9],[9,10,0,8,7],[9,10,8,0,3],[8,9,7,4,0]]
    #names = ['A','B','C','D','E'] wiki

    # mat = [[0,10,12,8],[10,0,4,6],[12,4,0,2],[8,6,2,0]]
    # names= ['A','B','C','D']

    mat = [[0,15,22,21,16],[15,0,13,12,7],[22,13,0,5,18],[21,12,5,0,17],[16,7,18,17,0]]
    names = ['A','B','C','D','E']
    
    tree =""
    
    

    while(len(mat)>=2):
        min = findSmallest(mat)
        joinTree(names[min[1]],names[min[2]])
        #print(tree)
        newMatrix(min)
        print(tree)
        print("--------------------------\n\n")

    print(tree)
    