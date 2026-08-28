class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        current_path = set()
        graph = {}
        for i in prerequisites:
            if i[1] not in graph:
                graph[i[1]] = []
            graph[i[1]].append(i[0])

        def dfs(course):
            if course in current_path:
                return False
            elif course in visited:
                return True
            else:
                current_path.add(course)
                for neighbour in graph.get(course, []):
                    if not dfs(neighbour):
                        return False
                current_path.remove(course)
                visited.add(course)
                return True

        for num in range(numCourses):
            if not dfs(num):
                return False

        return True

