import numpy as np

global tree
global bValue
global bAdded

def newMatrix(dij,v):
    global mat
    x = dij[1]
    y = dij[2]
    tam = len(mat)

    #altera os nomes dos nodos
    newName = "(" + names[x]+":"+ str(round(v[0],4))+","+names[y]+":"+ str(round(v[1],4))+")"    
    bAdded.append(newName)
    
    name1 = names[x]
    name2 = names[y]

    names.remove(name1)
    names.remove(name2)
    names.insert(0,newName)    

    #calcula as novas distancias
    nDist = np.zeros(len(mat))
    for i in range (len(mat)):
        nDist[i] = (mat[x][i] +  mat[y][i])/2         
    nDist = np.delete(nDist,(x,y),0)

    #deleta as colunas/linhas que serão descartadas da matrix antiga
    mat = np.delete(mat,(x,y),0)    
    mat = np.delete(mat,(x,y),1)

     #calcula a nova matriz, usando parte da antiga e as novas distancias nDist
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
        tree = "("+x+":"+str(v[0])+","+y+":"+str(v[1])+"),"+tree
            
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

def inputF(op):
    mat = []
    if not op:
        names = input()
        names = names.split("\t")
        for i in range (len(names)):
            linha = input()
            mat[i] = linha.split("\t")
    else:
        mat = [[0.0,0.01,0.3,0.28],[0.01,0.0,0.28,0.27],[0.3,0.28,0.0,0.015],[0.28,0.27,0.015,0.0]]
        names = ["brazilienses", "rangeli", "cruzi", "gambiae"]

    return [mat,names]

if __name__ == '__main__':
	
    tree =""
    bValue=[]
    bAdded=[]

    print ("0 - Digitar matriz\n1 - Utilizar matriz exemplo")
    op = input()
    mat,names = inputF(op)   

    while(len(mat)>=2):
        min = findSmallest(mat)
        v = branchValue(min)
        joinTree(names[min[1]],names[min[2]],v)
        newMatrix(min,v)

    print(tree)
    