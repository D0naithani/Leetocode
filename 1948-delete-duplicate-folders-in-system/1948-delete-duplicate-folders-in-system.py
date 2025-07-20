import heapq

class TrieNode:
    def __init__(self, name):
        self.name = name
        self.children = {}  # Map: folder_name -> TrieNode
        self.signature = "" # Hashed representation of its subfolder structure
        self.is_marked_for_deletion = False

# Global map to store signatures to lists of nodes that have that signature
# This is used to detect duplicates and mark them.
# It's crucial to reset this for each test case if running multiple tests in one session.
signature_to_nodes = {}

class Solution:
    # Corrected method name: deleteDuplicateFolder (singular)
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        # Reset the global map for each test case
        # This is important for competitive programming platforms where the Solution class
        # might be instantiated once and multiple test cases run.
        global signature_to_nodes
        signature_to_nodes = {}

        # 1. Build the Trie
        root = TrieNode("") # Dummy root node

        for path in paths:
            curr = root
            for folder_name in path:
                if folder_name not in curr.children:
                    new_node = TrieNode(folder_name)
                    curr.children[folder_name] = new_node
                curr = curr.children[folder_name]
        
        # 2. Post-order traversal to compute signatures and mark duplicates
        # The DFS function returns the signature of the current node's subtree.
        # It also marks nodes for deletion if duplicates are found.
        def dfs_compute_signature(node: TrieNode) -> str:
            # Collect signatures of children.
            # We sort child names to ensure a canonical order for the signature string.
            child_signatures_list = []
            for child_name in sorted(node.children.keys()):
                child_node = node.children[child_name]
                # Recursively get the signature of the child's subtree
                sig_of_child_subtree = dfs_compute_signature(child_node)
                # Append the child's name and its signature to form part of parent's signature.
                # Example format: "child_name(child_subtree_signature)"
                child_signatures_list.append(f"{child_name}({sig_of_child_subtree})")
            
            # The signature of the current node's subtree is a concatenation of its
            # sorted children's (name, signature) representations.
            # If a folder has no children, its `child_signatures_list` will be empty,
            # resulting in an empty `node.signature`.
            node.signature = "".join(child_signatures_list)
            
            # Mark nodes for deletion if their signature is not empty AND it's a duplicate.
            # An empty signature means the folder has no subfolders.
            # The problem wording "same non-empty set of identical subfolders" is tricky.
            # Example 1 implies that empty folders are considered identical (e.g., "/a/b" and "/c/b").
            # Their *parents* ("/a" and "/c") then become identical because they contain
            # an identical empty subfolder ("b"). The signature of "/a" would be "b()", which is non-empty.
            # So, the check `if node.signature:` is crucial: we only consider nodes that *have* a structural
            # definition (i.e., they contain at least one child or a named empty child `b()`).
            # If a folder itself is an empty leaf, its `node.signature` will be `""`.
            # We don't mark based on empty signatures directly, but rather on parent signatures that *include*
            # the empty children's structures (e.g., "b()").

            if node.signature: # Only consider non-empty signatures for potential duplication
                if node.signature in signature_to_nodes:
                    # If this signature has been seen before, it's a duplicate.
                    # Mark the current node for deletion.
                    node.is_marked_for_deletion = True
                    # Also mark all previously seen nodes with this signature for deletion.
                    for other_node in signature_to_nodes[node.signature]:
                        other_node.is_marked_for_deletion = True
                else:
                    # If this is the first time we see this signature, initialize its list.
                    signature_to_nodes[node.signature] = []
                # Add the current node to the list for this signature.
                signature_to_nodes[node.signature].append(node)
            
            return node.signature # Return the computed signature for the parent to use

        # Start the DFS from the dummy root.
        # The signature of the dummy root itself is not relevant for deletion,
        # as it's not a real folder in the filesystem.
        dfs_compute_signature(root)

        # 3. Collect paths of the remaining (unmarked) folders.
        result_paths = []
        
        # Helper DFS function to traverse the Trie and collect paths.
        def collect_paths(node: TrieNode, current_path_parts: List[str]):
            # If the current node is marked for deletion, then this node and all its
            # subfolders should be skipped.
            if node.is_marked_for_deletion:
                return 

            # If it's not the dummy root, add its path to the results.
            # The dummy root has an empty name.
            if node.name: 
                result_paths.append(list(current_path_parts)) # Append a copy of the current path

            # Recursively traverse children.
            for child_name in node.children:
                child_node = node.children[child_name]
                # Add child's name to the current path parts
                current_path_parts.append(child_name)
                # Recursively call collect_paths for the child
                collect_paths(child_node, current_path_parts)
                # Backtrack: remove child's name when returning from recursion
                current_path_parts.pop() 

        # Start collecting paths from the direct children of the dummy root.
        # These are the top-level folders in the original file system.
        for child_name in root.children:
            child_node = root.children[child_name]
            # Only start collection from top-level folders that are NOT marked for deletion.
            if not child_node.is_marked_for_deletion:
                collect_paths(child_node, [child_name])
                
        return result_paths