class node:
    def __init__(self, num, weight ):
        self.num = num
        self.w = weight 


def dfs(graph,   start_node ):
        
    dp = [float('inf') for _ in range( len(graph) ) ]

    def dfs_recursive(node):
        if dp[ node.num ] != float('inf') :
            return 
        
        if not graph[ node.num ]:
            dp[node.num] = node.w
            return 

        for neighbor in graph[ node.num ]:
            dfs_recursive(neighbor)
            if node.w + dp[ neighbor.num ] < dp[ node.num ]:
                dp[ node.num ] = node.w + dp[ neighbor.num ]

    dfs_recursive( start_node )
    return dp[0]

def nodeNumber(i, j):
    return int((1 + i)* i / 2 ) + j

def make_graph(triang):
    graph = [[] for _ in range( int(((1 + len(triang)) * len(triang))/2)  ) ]
    for i in range(0, len(triang)):
        for j in range(len (triang[i]) ):
            if i + 1  < len(triang) and j+1 < len (triang[i+1]):
                graph[ nodeNumber(i, j) ].append( node( nodeNumber(i+1, j) , triang[i+1][j] ) )
                graph[ nodeNumber(i, j) ].append( node( nodeNumber(i+1, j+1) , triang[i+1][j+1] ) )
    return graph


if __name__ == '__main__':

    triang = [[2],[3,1],[6,5,7],[4,1,8,0]]
    print( dfs( make_graph(triang), node(0, triang[0][0]) ) )