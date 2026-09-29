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
        q = deque()
        q.append(src)
        while q:
            curr = q.popleft()
            if curr == dst:
                return True
            visited.add(curr)
            for neighbor in self.adjList[curr]:
                if neighbor not in visited:
                    q.append(neighbor)
                    visited.add(neighbor)
        return False
            
