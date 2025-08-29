# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return None
        
        cloned = {}

        def dfs(curr):
            if curr in cloned:
                return cloned[curr]
            
            copy = Node(curr.val)
            cloned[curr] = copy
            for nei in curr.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        
        return dfs(node)

# Helper: Build graph from adjacency list
def buildGraph(adjList):
    if not adjList:
        return None
    nodes = [Node(i+1) for i in range(len(adjList))]
    for i, neighbors in enumerate(adjList):
        nodes[i].neighbors = [nodes[j-1] for j in neighbors]
    return nodes[0]

# Helper: Convert graph back to adjacency list
def graphToAdjList(node):
    if not node:
        return []
    
    visited = {}
    def dfs(curr):
        if curr.val in visited:
            return
        visited[curr.val] = [nei.val for nei in curr.neighbors]
        for nei in curr.neighbors:
            dfs(nei)
    dfs(node)
    return [visited[i+1] for i in range(len(visited))]

if __name__ == "__main__":
    
    adjList = eval(input("Enter adjacency list: "))
    
    graph = buildGraph(adjList)
    solution = Solution()
    clonedGraph = solution.cloneGraph(graph)
    
    output = graphToAdjList(clonedGraph)
    print("Cloned Graph (Adjacency List):", output)
