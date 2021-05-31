from sys import maxsize 
from itertools import permutations
V = 4
 
# implementation of traveling Salesman Problem 
def travellingSalesmanProblem(graph, s): 
 
    # store all vertex apart from source vertex 
    vertex = [] 
    for i in range(V): 
        if i != s: 
            vertex.append(i) 
 
    # store minimum weight Hamiltonian Cycle 
    min_path = maxsize 
    next_permutation=permutations(vertex)
    #print(list(next_permutation))
    for i in next_permutation:
 
        # store current Path weight(cost) 
        current_pathweight = 0
 
        # compute current path weight 
        k = s 
        for j in i: 
            current_pathweight += graph[k][j] 
            k = j 
        current_pathweight += graph[k][s] 
 
        # update minimum 
        if current_pathweight<=min_path:
            min_path=current_pathweight
            path=map(str,i)
            path=' '.join(path)
         
    return str("Minimum Distance: ")+ str(min_path)+' '+str("\nPath: ")+str(s)+' '+str(path)+' '+str(s)
 
 
# Driver Code 
if __name__ == "__main__": 
 
    # matrix representation of graph 
    graph = [[0,  20, 42, 35],
    [20,  0, 30,  34],
    [42,  30, 0,  12],
    [35, 34, 12,  0]]
    s = 0
    print("Graph:",graph)
    print(travellingSalesmanProblem(graph, s))
