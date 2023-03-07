import numpy as np


global tree
global bValue
global bAdded

def newMatrix(dij,v):
    global mat
    x = dij[1]
    y = dij[2]
    tam = len(mat)

    newName = "(" + names[x]+":"+ str(round(v[0],4))+","+names[y]+":"+ str(round(v[1],4))+")"    
    bAdded.append(newName)
    
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

def joinTree(x,y,v):
    global tree
    findx = tree.find(x)
    findy = tree.find(y)
    

    if (findx !=-1 and findy!=-1):#se os dois estão na árvore
        tree =  tree.replace(x+",","")
        tree =  tree.replace(x,"")
        tree = tree.replace(y+",","")
        tree =  tree.replace(y,"")
        if len(tree)>0:
            tree = "("+x+":"+str(v[0])+","+y+":"+str(v[1])+"),"+tree
        else:
            tree = "("+x+":"+str(v[0])+","+y+":"+str(v[1])+")"
            
    elif(findx !=-1): #se x está
        tree =  tree[0:findx] + "("+ tree[findx:findx+len(x)]+":"+ str(round(v[0],4)) + "," +y +":"+ str(round(v[1],4))+ ")" + tree[findx+len(x):len(tree)]

    elif(findy !=-1): #se y está
        tree =  tree[0:findy] + "("+ tree[findx:findy+len(y)]+":"+ str(round(v[1],4))  + "," +x +":"+ str(round(v[0],4))+ ")"+ tree[findy+len(x):len(tree)]

    else: #se nenhum está
        nodo = "("+ x+":"+ str(round(v[0],4)) + ","+ y+":"+ str(round(v[1],4)) + ")"
        if (len(tree)>0):
            tree = nodo + ","+tree
        else:
            tree = nodo

def branchValue(min):
    
    namex = names[min[1]]
    namey = names[min[2]]
    v = [0,0]

    if namex in bAdded:
        x = bAdded.index(namex)
        
        v[0] = round(min[0]/2-bValue[x],2)
    else:
        v[0] = round(min[0]/2,2)

    if namey in bAdded:
        y = bAdded.index(namey)
        v[1] = round(min[0]/2-bValue[y],2)
    else:
        v[1] = round(min[0]/2,2)

    
    bValue.append(min[0]/2)

    return v


def findSmallest(mat):
	tam = len(mat)
	min = [mat[0][1],0,1]
	for x in range(tam):
		for y in range(tam):
			if (mat[x][y]<min[0] and x!=y):
				min=[mat[x][y],x,y]
	return min


if __name__ == '__main__':
	
    #moodle
    mat = [[0,2,4,6,6,8],[2,0,4,6,6,8],[4,4,0,6,6,8],[6,6,6,0,4,8],[6,6,6,4,0,8],[8,8,8,8,8,0]]
    names = ['A','B','C','D','E','F']

    #wikipedia
    #mat = [[0,17,21,31,23],[17,0,30,34,21],[21,30,0,28,39],[31,34,28,0,43],[23,21,39,43,0]]
    #names = ['A','B','C','D','E']

    #https://www.olimpbiol.pl/wp-content/uploads/2018/04/UPGMA.pdf
    #mat = [[0,19,27,8,33,18,13],[19,0,31,18,36,1,13],[27,31,0,26,41,32,29],[8,18,26,0,31,17,14],[33,36,41,31,0,35,28],[18,1,32,17,35,0,12],[13,13,29,14,28,12,0]]
    #names = ['A','B','C','D','E','F', 'G']

    tree =""
    bValue=[]
    bAdded=[]

    while(len(mat)>=2):
        min = findSmallest(mat)
        v = branchValue(min)
        joinTree(names[min[1]],names[min[2]],v)
        newMatrix(min,v)
        
        print(tree)
        print("--------------------------\n\n")
        print(mat)

    print(tree)
    