class Solution(object):
    def minReorder(self, n, connections):
        graph = defaultdict(list)

        # Build adjacency with direction cost
        for a, b in connections:
            graph[a].append((b, 1))  # original a->b, needs reversal
            graph[b].append((a, 0))  # reverse direction, fine

        visited = [False] * n
        changes = 0
        queue = deque([0])
        visited[0] = True

        while queue:
            node = queue.popleft()
            for nei, cost in graph[node]:
                if not visited[nei]:
                    changes += cost
                    visited[nei] = True
                    queue.append(nei)

        return changes
        