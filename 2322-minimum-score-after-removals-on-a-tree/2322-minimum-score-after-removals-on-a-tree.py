import collections

class Solution:
    def minimumScore(self, nums: list[int], edges: list[list[int]]) -> int:
        n = len(nums) # n is defined here
        adj = collections.defaultdict(list) # Now n is in scope
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        xor_subtree = [0] * n
        entry_time = [0] * n
        exit_time = [0] * n
        timer = 0

        # DFS to compute subtree XORs and entry/exit times for ancestry checks
        def dfs_precompute(u, p):
            nonlocal timer
            entry_time[u] = timer
            timer += 1
            
            current_node_xor = nums[u]
            for v in adj[u]:
                if v == p:
                    continue
                current_node_xor ^= dfs_precompute(v, u) # Recursively get XOR sum of child subtree
            
            xor_subtree[u] = current_node_xor # Store the full subtree XOR sum for node u
            exit_time[u] = timer
            timer += 1
            return xor_subtree[u]

        # Start DFS from root (node 0) with a dummy parent (-1)
        dfs_precompute(0, -1)
        
        # The total XOR sum of the tree is the subtree XOR sum of the root
        S_total = xor_subtree[0] 

        # Helper function to check if u is an ancestor of v (inclusive of u itself)
        def is_ancestor(u, v):
            return entry_time[u] <= entry_time[v] and exit_time[u] >= exit_time[v]

        min_score = float('inf')

        # Iterate over all distinct pairs of edges
        # Each edge (u, v) is effectively a cut that separates the subtree rooted at the child from the rest.
        # We ensure u is always the parent of v in the rooted tree for consistency.
        all_edges_rooted = []
        for u_raw, v_raw in edges:
            if is_ancestor(u_raw, v_raw): # u_raw is parent of v_raw
                all_edges_rooted.append((u_raw, v_raw))
            else: # v_raw is parent of u_raw
                all_edges_rooted.append((v_raw, u_raw))

        num_edges = len(all_edges_rooted)
        for i in range(num_edges):
            u1, v1 = all_edges_rooted[i] # First edge: (parent1, child1)
            for j in range(i + 1, num_edges):
                u2, v2 = all_edges_rooted[j] # Second edge: (parent2, child2)

                # Determine the three component XOR sums
                xor_comp1, xor_comp2, xor_comp3 = 0, 0, 0

                # Case 1: The subtree of v2 is nested within the subtree of v1
                # This means cutting (u1, v1) isolates subtree(v1), and then cutting (u2, v2) further splits subtree(v1)
                if is_ancestor(v1, v2):
                    xor_comp1 = xor_subtree[v2] # Component 1: Subtree rooted at v2
                    xor_comp2 = xor_subtree[v1] ^ xor_subtree[v2] # Component 2: Nodes in subtree v1 but not in subtree v2
                    xor_comp3 = S_total ^ xor_subtree[v1] # Component 3: Nodes not in subtree v1
                # Case 2: The subtree of v1 is nested within the subtree of v2
                # Symmetric to Case 1
                elif is_ancestor(v2, v1):
                    xor_comp1 = xor_subtree[v1] # Component 1: Subtree rooted at v1
                    xor_comp2 = xor_subtree[v2] ^ xor_subtree[v1] # Component 2: Nodes in subtree v2 but not in subtree v1
                    xor_comp3 = S_total ^ xor_subtree[v2] # Component 3: Nodes not in subtree v2
                # Case 3: The subtrees rooted at v1 and v2 are disjoint
                # This means cutting (u1, v1) isolates subtree(v1), and cutting (u2, v2) isolates subtree(v2) from the *remaining* part of the tree
                else: 
                    xor_comp1 = xor_subtree[v1] # Component 1: Subtree rooted at v1
                    xor_comp2 = xor_subtree[v2] # Component 2: Subtree rooted at v2
                    xor_comp3 = S_total ^ xor_subtree[v1] ^ xor_subtree[v2] # Component 3: The remaining nodes (total XOR minus the two isolated subtrees)
                
                # Calculate the score for this pair of cuts
                current_xors = sorted([xor_comp1, xor_comp2, xor_comp3])
                score = current_xors[2] - current_xors[0] # Largest XOR - Smallest XOR
                min_score = min(min_score, score)

        return min_score