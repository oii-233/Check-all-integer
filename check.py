class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
        covered = set()
        for start, end in ranges:
            covered.update(range(start, end + 1))
        return all(num in covered for num in range(left, right + 1))


# Create instance of the class
solution = Solution()

# Test case 1
ranges = [[1, 2], [3, 4], [5, 6]]
left = 2
right = 5
print(solution.isCovered(ranges, left, right))  # Output: True

# Test case 2
ranges = [[1, 10], [10, 20]]
left = 21 
right = 21
print(solution.isCovered(ranges, left, right))  # Output: False
