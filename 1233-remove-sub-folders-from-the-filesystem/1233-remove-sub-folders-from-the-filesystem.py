class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # Sort the folder paths lexicographically.
        # This is crucial because it ensures that any parent folder
        # will always appear before its sub-folders in the sorted list.
        # For example: "/a" will be before "/a/b", "/a/b" before "/a/b/c".
        folder.sort()

        result = []
        
        # If the input list is empty, return an empty list.
        if not folder:
            return []
            
        # Initialize last_added_root with the first folder in the sorted list.
        # The very first folder cannot be a sub-folder of any preceding folder,
        # as there are no preceding folders. So, it's always a root.
        last_added_root = folder[0]
        result.append(last_added_root)

        # Iterate through the sorted list starting from the second folder.
        for i in range(1, len(folder)):
            current_folder = folder[i]
            
            # Check if current_folder is a sub-folder of the last_added_root.
            # A folder 'A' is a sub-folder of 'B' if 'A' starts with 'B/'
            # This handles cases like "/a" and "/a/b" correctly,
            # while distinguishing "/a" from "/ab" (where "/ab" is not a sub-folder of "/a").
            # The check `current_folder.startswith(last_added_root + '/')`
            # ensures that `last_added_root` is a proper prefix followed by a directory separator.
            if not current_folder.startswith(last_added_root + '/'):
                # If current_folder is NOT a sub-folder of the last_added_root,
                # then it means current_folder itself is a root folder (or a sub-folder
                # of some higher-level root that's not in the list or was already added).
                # Due to sorting, if it's not a sub-folder of the *last added* root,
                # it cannot be a sub-folder of any *earlier added* root either.
                result.append(current_folder)
                # Corrected variable name here:
                last_added_root = current_folder
                
        return result