import numpy as np

global tree

def newMatrix(dij,v):
    global mat
    print(dij)
    x = dij[1]
    y = dij[2]
    print(names[x],names[y])
    print(names)
    tam = len(mat)

    #altera os nomes dos nodos
    newName = "(" + names[x]+":"+ str(round(v[0],4))+","+names[y]+":"+ str(round(v[1],4))+")"    
    name1 = names[x]
    name2 = names[y]
    names.remove(name1)
    names.remove(name2)
    names.insert(0,newName)    

    #calcula as novas distancias
    nDist = np.zeros(len(mat))
    for i in range (len(mat)):
        nDist[i] = (mat[x][i] + mat[y][i]-mat[x][y])/2      
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
        tree = tree.replace(y+",","")
        tree = "("+x+","+y+"),"+tree
            
    elif(findx !=-1): #se x está
        tree =  tree[0:findx] + "("+ tree[findx:findx+len(x)]+":"+ str(round(v[0],4)) + "," +y +":"+ str(round(v[1],4))+ ")" + tree[findx+len(x):len(tree)]

    elif(findy !=-1): #se y está
        tree =  tree[0:findy] + "("+ tree[findx:findy+len(y)]+":"+ str(round(v[1],4))  + "," +x +":"+ str(round(v[0],4))+ ")"+ tree[findy+len(x):len(tree)]

    else: #se nenhum está
        tree = "("+ x+":"+ str(round(v[0],4)) + ","+ y+":"+ str(round(v[1],4)) + ")"

def valueBranch(min):
    print ("valuebranch")
    name1 = names[min[1]]
    name2 = names[min[2]]
    print(name1,name2)
    
    branch1 = name1.find(":")
    branch2 = name2.find(":")
    oldV=v=[0,0]
    
    if branch1!=-1:
        s = name1[branch1:]
        print("s + "+ s)
        por = s.find(")")
        value = name1[branch1:por-1]
        print("v+" +value)
        oldV[0] = int(value)
    
    if branch2!=-1:
        s = name2[branch2:]
        por = s.find(")")
        value = name2[branch2:por-1]
        print("v+" +value)
        oldV[1] = int(value)

    v[0] = mat[min[1]][min[2]]/2 - oldV[0]
    v[1] = mat[min[1]][min[2]]/2 - oldV[1]

    print(round(v[0],2))
    print("end")
    
    return v

def findSmallest(mat):
	tam = len(mat)
	min = [mat[0][1],0,1]
	for x in range(tam):
		for y in range(tam):
			#print(min[0])
			if (mat[x][y]<=min[0] and x!=y):
				min=[mat[x][y],x,y]
	#print(min)
	return min


if __name__ == '__main__':
	
    mat = [[0,2,4,6,6,8],[2,0,4,6,6,8],[4,4,0,6,6,8],[6,6,6,0,4,8],[6,6,6,4,0,8],[8,8,8,8,8,0]]
    names = ['A','B','C','D','E','F']

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

    #mat = [[0,15,22,21,16],[15,0,13,12,7],[22,13,0,5,18],[21,12,5,0,17],[16,7,18,17,0]]
    #names = ['A','B','C','D','E']
    
    tree =""
    
    

    while(len(mat)>=2):
        min = findSmallest(mat)
        print (min)
        v = valueBranch(min)
        #v= mat[min[1]][min[2]]/2
        joinTree(names[min[1]],names[min[2]],v)
        #print(tree)
        newMatrix(min,v)
        #print(tree)
        print("--------------------------\n\n")

    print(tree)
    