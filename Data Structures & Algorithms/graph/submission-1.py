class Graph:
    
    def __init__(self):
        self.adjList = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adjList:
            self.adjList[src] = []
        if dst not in self.adjList:
            self.adjList[dst] = []
        self.adjList[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src in self.adjList and dst in self.adjList and dst in self.adjList[src]:
            self.adjList[src].remove(dst)
            return True
        return False

    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()
        return self.dfs(src, dst, visited)
    
    def dfs(self, src: int, dst: int, visited: set) -> bool:
        if src == dst:
            return True
        visited.add(src)
        for neighbor in self.adjList[src]:
            if neighbor not in visited:
                if self.dfs(neighbor, dst, visited):
                    return True
        return False
