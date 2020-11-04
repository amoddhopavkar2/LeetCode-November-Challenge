# Minimum Height Trees

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        edgelist = collections.defaultdict(set)
        for u, v in edges:
            edgelist[u].add(v)
            edgelist[v].add(u)

        leaves = [node for node, sibs in edgelist.items() if len(sibs) == 1]

        while len(edgelist) > 2:
            nextleaves = []
            for leaf in leaves:
                parent = edgelist[leaf].pop()
                del edgelist[leaf]
                edgelist[parent].remove(leaf)
                if len(edgelist[parent]) == 1:
                    nextleaves.append(parent)

            leaves = nextleaves

        return leaves
        