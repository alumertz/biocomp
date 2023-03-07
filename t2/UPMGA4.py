import numpy as np

global tree
global bValue
global bAdded
global bQuant

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

    

    


    #calcula as novas distancias
    nDist = np.zeros(len(mat))
    
    
    
    for i in range (len(mat)):
        
        nDist[i] = (mat[x][i]*bQuant[x]+  mat[y][i]*bQuant[y])/(bQuant[x]+bQuant[y])   

    nDist = np.delete(nDist,(x,y),0)



    sum = bQuant[x] +bQuant[y]
    bQuant.pop(y)
    bQuant.pop(x)    
    bQuant.insert(0,sum)

    
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

    print("juntar", x,y)
    

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
    print(tree)


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
    #mat = [[0,2,4,6,6,8],[2,0,4,6,6,8],[4,4,0,6,6,8],[6,6,6,0,4,8],[6,6,6,4,0,8],[8,8,8,8,8,0]]
    #names = ['A','B','C','D','E','F']


    #wikipedia
    #mat = [[0,17,21,31,23],[17,0,30,34,21],[21,30,0,28,39],[31,34,28,0,43],[23,21,39,43,0]]
    #names = ['A','B','C','D','E']

    #https://www.olimpbiol.pl/wp-content/uploads/2018/04/UPGMA.pdf
    #mat = [[0,19,27,8,33,18,13],[19,0,31,18,36,1,13],[27,31,0,26,41,32,29],[8,18,26,0,31,17,14],[33,36,41,31,0,35,28],[18,1,32,17,35,0,12],[13,13,29,14,28,12,0]]
    #names = ['A','B','C','D','E','F', 'G']

    mat=np.array([
    [0, -49, -47, -39, -39, -38, -131, 84, -42, -45],
    [-49, 0, 35, 72, 61, -55, -139, -43, 42, 52],	
    [-47, 35, 0, 41, 112, -47, -134, -40, 42, 147],
    [-39, 72, 41, 0, 66, -49, -133, -33, 78, 59],
    [-39, 61, 112, 66, 0 , -43, -133, -38, 52, 132],
    [-38, -55, -47, -49, -43, 0, -145, -33, -53, -44],
    [-131, -139, -134, -133, -133, -145, 0, -123, -135, -146],
    [84, -43, -40, -33, -38, -33, -123, 0, -29, -46],
    [-42, 42, 42, 78, 52, -53, -135, -29, 0, 52 ],
    [-45, 52, 147, 59, 132, -44, -146, -46, 52, 0] ])
    mat = mat * -1
    names =["seq1","seq2","seq3","seq4","seq5","seq6","seq7","seq8","seq9","seq0"]

    tree =""
    bValue=[]
    bAdded=[]
    #bQuant = np.full(len(names),1)
    bQuant = [1 for col in range(len(names))]

    mat = mat*-1

    while(len(mat)>=2):
        min = findSmallest(mat)
        v = branchValue(min)
        joinTree(names[min[1]],names[min[2]],v)
        newMatrix(min,v)        

    print(tree)
    