# Pattern: Hashmap (one-pass)
# Intuition: for each number, the complement (target - num) must have been seen
# already -> store num->index in a dict as we go. O(n) time, O(n) space.

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []  # no solution (LeetCode guarantees one exists)


# --- test ---
if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    print(two_sum([3, 2, 4], 6))        # [1, 2]
    print(two_sum([3, 3], 6))           # [0, 1]
