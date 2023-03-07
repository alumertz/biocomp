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

def smallestDij(ui):
    tam = len(mat)
    x = y = start =0
   
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

def valueBranch(dij,ui):
    x = dij[1]
    y = dij[2]
    dist = mat[x][y]
    v = np.zeros(2)
    v[0] = abs((dist + (ui[x]-ui[y]))/2)
    v[1] = abs((dist + (ui[y]-ui[x]))/2)
    return v
   

def joinTree(x,y,v):
    global tree
    findx = tree.find(x)
    findy = tree.find(y)

    if (x=="end"): #se é o último nodo a ser inserido
        tree = tree[:len(tree)-1]+ "," +y +":0" + ")"

    elif (findx !=-1 and findy!=-1):#se os dois estão na árvore
        tree =  tree.replace(x+",","")
        tree = tree.replace(y+",","")
        tree = "("+x+","+y+"),"+tree
            
    elif(findx !=-1): #se x está
        tree =  tree[0:findx] + "("+ tree[findx:findx+len(x)]+":"+ str(round(v[0],4)) + "," +y +":"+ str(round(v[1],4))+ ")" + tree[findx+len(x):len(tree)]

    elif(findy !=-1): #se y está
        tree =  tree[0:findy] + "("+ tree[findx:findy+len(y)]+":"+ str(round(v[1],4))  + "," +x +":"+ str(round(v[0],4))+ ")"+ tree[findy+len(x):len(tree)]

    else: #se nenhum está
        tree = "("+ x+":"+ str(round(v[0],4)) + ","+ y+":"+ str(round(v[1],4)) + ")"
    
    
def newMatrix(dij,v):
    global mat
    x = dij[1]
    y = dij[2]
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

def inputF(op):
    mat = []
    if not op:
        names = input()
        names = names.split("\t")
        for i in range (len(names)):
            linha = input()
            mat[i] = linha.split("\t")
    else:        
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
        names =["seq1","seq2","seq3","seq4","seq5","seq6","seq7","seq8","seq9","seq0"]

        #mat = [[0,1,3,2.8],[1,0,2.8,2.7],[3,2.8,0,0.15],[2.8,2.7,0.15,0]]#exemplo
        #names = ["b", "r", "c", "g"]#exemplo



    return [mat,names]
    
if __name__ == '__main__':
    
    global mat
    
    print ("0 - Digitar matriz\n1 - Utilizar matriz exemplo")
    op = input()
    mat,names = inputF(op)
    mat = mat*-1 
    print (mat)
    while(len(mat)>2):
        ui = uiCalculation()
        dij = smallestDij(ui)
        v = valueBranch(dij,ui)
        joinTree(names[dij[1]],names[dij[2]],v)
        newMatrix(dij,v)

    
    joinTree("end",names[1],[0,mat[0][0]])
    print(tree)
    