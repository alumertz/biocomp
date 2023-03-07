import numpy as np

names=[]
tree=""

def uiCalculation():
    tam = len(mat)
    global ui
    ui= np.zeros(tam)

    for x in range(tam):
        for y in range(tam):
            ui[x] += mat[x][y]
        
        ui[x] = ui[x]/(tam-2)
    return ui

def smallestDij():
    tam = len(mat)
    m=0
    for x in range (tam):
        m+=tam-1-x

    
    x=0
    y=0
    start=0
    min = [mat[0][1] - ui[0] -ui[1],0,1]
    while (x<tam):
        start+=1    
        y=start
        while (y<tam):
            d = mat[x][y] - ui[x] -ui[y]
            if (d<min[0]):
                min = [d,x,y]  
            
            y+=1 
        x+=1
    return min

def valueBranch(dij):
    x = dij[1]
    y = dij[2]
    dist = mat[x][y]
    print(dist, x, y)
    print(ui[x], ui[y])
    v = np.zeros(2)
    v[0] = abs((dist + (ui[x]-ui[y]))/2)
    v[1] = abs((dist + (ui[y]-ui[x]))/2)
    print(v)
    return v
   

def joinTree(x,y,v):
    global tree
    findx = tree.find(x)
    findy = tree.find(y)

    print(x, findx, y, findy, tree)

    if (x=="end"):
        tree = tree[:len(tree)-1]+ "," +y +":0" + ")"

    elif (findx !=-1 and findy!=-1):#se os dois estão na árvore
        print("e1")
        tree =  tree.replace(x+",","")
        tree = tree.replace(y+",","")
        tree = "("+x+","+y+"),"+tree
            
    elif(findx !=-1):
        print("e2")
        tree =  tree[0:findx] + "("+ tree[findx:findx+len(x)]+":"+ str(round(v[0],4)) + "," +y +":"+ str(round(v[1],4))+ ")" + tree[findx+len(x):len(tree)]

    elif(findy !=-1):
        print("e3")
        tree =  tree[0:findy] + "("+ tree[findx:findy+len(y)]+":"+ str(round(v[1],4))  + "," +x +":"+ str(round(v[0],4))+ ")"+ tree[findy+len(x):len(tree)]

    else:#(len(tree)==0):
        print("e4")
        tree = "("+ x+":"+ str(round(v[0],4)) + ","+ y+":"+ str(round(v[1],4)) + ")"
        #tree = "("+x+","+y+")"
    
    
def newMatrix(dij,v):
    global mat
    x = dij[1]
    y = dij[2]
    tam = len(mat)

    newName = "(" + names[x]+":"+ str(round(v[0],4))+","+names[y]+":"+ str(round(v[1],4))+")"
    
    name1 = names[x]
    name2 = names[y]

    names.remove(name1)
    names.remove(name2)
    names.insert(0,newName)    

    nDist = np.zeros(len(mat))
    for i in range (len(mat)):
        nDist[i] = (mat[x][i] + mat[y][i]-mat[x][y])/2            

    nDist = np.delete(nDist,(x,y),0)

    mat = np.delete(mat,(x,y),0)    
    mat = np.delete(mat,(x,y),1)

    nMat= np.zeros((tam-1,tam-1))
    
    nMat[1:tam-1,0] = nDist
    
    nMat[0,1:tam-1] = nDist
    
    nMat[1:tam-1,1:tam-1] = mat

    mat = nMat

    
if __name__ == '__main__':
    
    global mat
    global ui
    global dij

    #mat = [[0.0,0.01,0.3,0.28],[0.01,0.0,0.28,0.27],[0.3,0.28,0.0,0.015],[0.28,0.27,0.015,0.0]]
    #names = ["brazilienses", "rangeli", "cruzi", "gambiae"]

    # mat = [[0.000,0.385,0.385,0.385,0.692,0.615,0.769,0.538,0.615],
    #         [0.385,0.000,0.231,0.000,0.538,0.462,0.692,0.385,0.538],
    #         [0.385,0.231,0.000,0.231,0.308,0.231,0.538,0.231,0.308],
    #         [0.385,0.000,0.231,0.000,0.538,0.462,0.692,0.385,0.538],
    #         [0.692,0.538,0.308,0.538,0.000,0.385,0.231,0.462,0.462],
    #         [0.615,0.462,0.231,0.462,0.385,0.000,0.615,0.385,0.077],
    #         [0.769,0.692,0.538,0.692,0.231,0.615,0.000,0.462,0.615],
    #         [0.538,0.385,0.231,0.385,0.462,0.385,0.462,0.000,0.462],
    #         [0.615,0.538,0.308,0.538,0.462,0.077,0.615,0.462,0.000]]
    # names = ['r','f','t','s','c','l','b','n','a']


    mat = np.array([[0,5,4,7,6,8],[5,0,7,10,9,11],[4,7,0,7,6,8,],[7,10,7,0,5,9],[6,9,6,5,0,8],[8,11,8,9,8,0]])
    names = ['A','B','C','D','E','F']

    while(len(mat)>2):
        uiCalculation()
        dij = smallestDij()
        v = valueBranch(dij)
        joinTree(names[dij[1]],names[dij[2]],v)
        newMatrix(dij,v)
        # print("\n")
        # print(mat)
        # print("\n")
        # print(tree)
        print("--------------------------\n\n")


    print ("\nbefore end")
    # print (tree)
    # print(names)
    # print("\n", names[0],names[1])
    # print ("\n")
    print(mat)
    joinTree("end",names[1],[0,mat[0][0]])
    print("tree")
    print(tree)
    