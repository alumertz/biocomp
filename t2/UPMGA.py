import numpy as np

global tree

def newMatrix(dij):
    global mat
    x = dij[1]
    y = dij[2]
    tam = len(mat)

    newName = "(" + names[x]+","+names[y]+ ")"
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

# def insert_node(new_label, parent_label, branch_length,tree):
    
#     print(tree)
#     # Traverse the tree to find the position where the new node should be inserted
#     for i, node in enumerate(tree):
#         print("aqui")
#         if isinstance(node, list):
#             print(node)
#             # Recursively traverse this subtree
#             subtree = insert_node(new_label, parent_label, branch_length, node)
#             print("a2")
#             if subtree is not None:
#                 print("a3")
#                 # If a new subtree was returned, insert it into the current list
#                 tree[i] = subtree
#                 return tree
#         elif node == parent_label:
#             print("a4")
#             # Insert the new node as a child of this node
#             new_node = [new_label, branch_length]
#             tree[i] = [tree[i], new_node]
#             return tree
    
    
#     new_node = [new_label, parent_label,branch_length]
#     print("new node")
#     print(new_node)
#     tree.append(new_node)
#     return tree

#     return None


def joinTree(x,y):
    global tree
    findx = tree.find(x)
    findy = tree.find(y)

    if (findx !=-1 and findy!=-1):
        tree = tree[0:findx] + "("+ tree[findx:findx+len(x)] + "," + tree[findy:findy+len(y)+ ")"+ tree[findy+len(y):len(tree)]]
    elif(findx !=-1):
        print("temx" + x)
        tree =  tree[0:findx] + "("+ tree[findx:findx+len(x)] + "," +y + ")"

    elif(findy !=-1):
        print("temy")
    elif(len(tree)==0):
        tree = "("+ x + ","+ y + ")"
    else:
        print("n tem nehum")
        tree = tree+ "," + "("+ x + ","+ y + ")"



# def joinTree(x,y):
	
# 	esta= 0
# 	global tree
# 	for i in tree:
# 		findx = tree[i].find(x)
# 		findy = tree[i].find(y)
# 		if(findx):
# 			esta= 1
# 			tree[i] = "("+tree[i]+")"+","+findx
			
# 		elif(findy):
# 			esta= 1
# 			tree[i] =  "("+tree[i]+")"+","+findy
#         elif (findx and findy):

		
			

# 	if(not esta):	
# 		tree.append(names[x]+","+names[y])


def findSmallest(mat):
	tam = len(mat)
	min = [mat[0][1],0,1]
	for x in range(tam):
		for y in range(tam):
			#print(min[0])
			if (mat[x][y]<min[0] and x!=y):
				min=[mat[x][y],x,y]
	print(min)
	return min


if __name__ == '__main__':
	
    mat = [[0,2,4,6,6,8],[2,0,4,6,6,8],[4,4,0,6,6,8],[6,6,6,0,4,8],[6,6,6,4,0,8],[8,8,8,8,8,0]]
   
    tree =""
   # print(mat)  
    names = ['A','B','C','D','E','F']
    min = findSmallest(mat)
    print(names[min[1]],names[min[2]])
    #tree = insert_node(names[min[1]],names[min[2]],min[0],tree)
    #tree = insert_node("D","E",4,tree)
    #tree = insert_node("A","C",4,tree)
    joinTree('A','B')
    print(tree)
    joinTree('D','E')
    print(tree)
    joinTree("(A,B)",'C')
    print(tree)
    joinTree("((A,B),C)",'(D,E)')
    print(tree)
    #joinTree(names[min[1]],names[min[2]],0)