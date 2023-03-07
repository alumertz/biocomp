from ntpath import join

tree=""

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


if __name__ == '__main__':
    joinTree('A','F')
    print(tree)
    joinTree('A','B')
    print(tree)
    joinTree('(A,B)','C')
    print(tree)