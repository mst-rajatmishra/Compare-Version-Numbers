class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Split the version strings into components
        v1_parts = version1.split('.')
        v2_parts = version2.split('.')
        
        # Determine the maximum length for comparison
        max_length = max(len(v1_parts), len(v2_parts))
        
        for i in range(max_length):
            # Get the current revision, or 0 if out of bounds
            v1_revision = int(v1_parts[i]) if i < len(v1_parts) else 0
            v2_revision = int(v2_parts[i]) if i < len(v2_parts) else 0
            
            # Compare the two revisions
            if v1_revision < v2_revision:
                return -1
            elif v1_revision > v2_revision:
                return 1
            
        return 0

# Example usage:
# sol = Solution()
# print(sol.compareVersion("1.2", "1.10"))      # Output: -1
# print(sol.compareVersion("1.01", "1.001"))    # Output: 0
# print(sol.compareVersion("1.0", "1.0.0.0"))   # Output: 0
