class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            if preMap[crs] == []:
                return True

            visit.add(crs)
            for pre in preMap[crs]:
                if dfs(pre) == False:
                    return False

            visit.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        return True