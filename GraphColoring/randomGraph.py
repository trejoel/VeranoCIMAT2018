import matplotlib.pyplot as plt
import networkx as nx
from random import randint
import sys

#Number of nodes N, probability P
def randomGraphErdos(N,P):
    G=nx.erdos_renyi_graph(N,P)
    while (nx.is_connected(G)!=True):
        G=nx.erdos_renyi_graph(N,P)
    return G 

def randomCycle(N):
    C=nx.cycle_graph(N)
    return C

def randomGraphBarbasi(N,M):
    G=nx.barabasi_albert_graph(N,M,seed=None)
    while (nx.is_connected(G)!=True):
        G=nx.barabasi_albert_graph(N,M,seed=None)
    return G     


#Save graph G as S, where S is a string
def saveGraph(G,S):
   nx.write_gml(G,S)

def readGraph(S):
	G=nx.read_gml(S)
	return G

def drawGraph(G):
    nx.draw(G,with_labels=True)
    plt.show()

def drawGraphColors(G, ListColors):
    color=['red','green','blue','black','royalblue','cyan','orange',
    'magenta','pink','purple','silver','rosybrown','firebrick','darksalmon',
    'sienna','bisque','moccasin','gold','tan','olivedrab','palegreen',
    'darkgreen','aliceblue','plum','navy','grey','maroon','coral','olive',
    'skyblue','crimson','indianred','wheat','beige','aqua','hotpink','snow']
    color_map = []
    cont=0
    for node in G:
        cont=cont+1
        color_map.append(color[cont])    
    nx.draw(G,node_color = color_map, with_labels=True)
    plt.show()

def printLines(G, size):
    file = open("test.txt","w") 
    for i in range(0,size):
        list=[n for n in G.neighbors(i)]
        for neighbor in list:
            strneighbor=str(neighbor+1)
            strneighbor=strneighbor+" "
            xstr=''.join(strneighbor)
            #xstr=xstr.join(' ')
            file.write(xstr) 
        if (i<size-1):
            file.write("\n")
    file.close()

def main():
    xSize=int(sys.argv[1])
    G=randomGraphErdos(xSize,0.1)
    printLines(G,xSize)
    xName="test"+str(xSize)+str(".gml")
    #drawGraphColors(G)
    saveGraph(G,xName)

def main4():
    for i in range(1,21):
        y=100*i
        x=5*i
        C=randomCycle(100*x)
        str1="cycle"
        str1=str1+str(x)
        str1=str1+".gml"
        saveGraph(C,str1)
        #drawGraph(G)

def main3():
	G=readGraph("cactus1.gml")
	drawGraph(G)

def main2():
    for i in range(0,1):
        G=randomGraphErdos(20,0.1)
        str1="graphErdos1.gml"
        #str1=str1+str(i)
        #str1=str1+".gml"
        saveGraph(G,str1)
        drawGraph(G)

if __name__ == "__main__":
    main()