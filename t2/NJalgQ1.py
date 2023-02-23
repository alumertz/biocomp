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
    
    #print (ui)
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
    
    while (x<tam and y<tam):
        start+=1    
        y=start
        while (y<tam):
            d = mat[x][y] - ui[x] -ui[y]
            if (d<min[0]):
                min = [d,x,y]
            
            y+=1           
        
        x+=1
    
    #print("min dij")
    #print (min[1],min[2], names[min[1]], names[min[2]])
    #print("\n")
    return min

def valueBranch(dij):
    x = dij[1]
    y = dij[2]
    #print(mat)
    dist = mat[x][y]
    v = np.zeros(2)
    #v.append(1)
    #v[1] = 2
    v[0] = (dist + (ui[x]-ui[y]))/2
    v[1] = (dist + (ui[y]-ui[x]))/2
   

def joinNode(name1,name2):
    
    branch = "("  + str(name1) + ","+ str(name2)+")"
    global tree 
    if(tree!=""):
        #print(" node" +str(name1) + " " + str(name2)+  " tree " + tree)
        begin = tree.find(str(name1))
        end = begin +len(str(name1))
        #print (begin, end)
        ntree = tree[0:begin]+"("+tree[begin:end]+"," +str(name2) + ")"+ tree[end:len(tree)]
        tree = ntree
        #tree = "("+tree+","+ branch +")"
    else:
        tree=branch
    
    
def newMatrix(dij):
    global mat
    x = dij[1]
    y = dij[2]
    tam = len(mat)

    newName = "(" + names[x]+","+names[y]+ ")"
    print ("newName " + newName)
    
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

    # mat = [[0.0,0.01,0.3,0.28],[0.01,0.0,0.28,0.27],[0.3,0.28,0.0,0.015],[0.28,0.27,0.015,0.0]]
    # names = ["brazilienses", "rangeli", "cruzi", "gambie"]

    mat = np.array([[0,5,4,7,6,8],[5,0,7,10,9,11],[4,7,0,7,6,8,],[7,10,7,0,5,9],[6,9,6,5,0,8],[8,11,8,9,8,0]])
    names = ['A','B','C','D','E','F']

        
    
    #joinNode(mat,ui,dij)

    while(len(mat)-2!=0):
        uiCalculation()
        dij = smallestDij()
        # print(dij)
        # print("\n")
        valueBranch(dij)
        joinNode(names[dij[1]],names[dij[2]])
        newMatrix(dij)
        mat = mat.astype(int)
        #print("\n")
        #print(mat)
        #print("names")
        #print(names)
        
        #print("tree")
       # print(tree)
        #print("\n----------------------------------\n")

    #print ("\n\nFINISH")
    print (names)

    joinNode(names[1], names[2])

    print("tree")
    print(tree)
    