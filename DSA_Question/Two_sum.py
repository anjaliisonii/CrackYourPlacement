class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums1=sorted(nums)
        i=0
        j=len(nums)-1
        while i<j:
            sum1=nums1[i]+nums1[j]
            if sum1==target:
                return [nums.index(nums1[i]),len(nums)-1-nums[::-1].index(nums1[j])]
            elif sum1>target:
                j-=1
            else:
                i+=1
        return -1
#Find all the unique pair of the given sum
def paired_elements(arr, target_sum):
    # Sort the array
    arr.sort()

    # Initialize pointers
    low = 0
    high = len(arr) - 1

    # Dictionary to track unique pairs
    unique_pairs = {}

    # Iterate with two pointers
    while low < high:
        # Check if sum equals the target
        if arr[low] + arr[high] == target_sum:
            # Print pair if elements are not already in the dictionary
            if arr[low] not in unique_pairs or arr[high] not in unique_pairs:
                print("The pair is : (", arr[low], ", ", arr[high], ")")
                unique_pairs[arr[low]] = True
                unique_pairs[arr[high]] = True
            low += 1
            high -= 1
        # Adjust pointers based on sum comparison
        elif arr[low] + arr[high] > target_sum:
            high -= 1
        else:
            low += 1

# Driver code
if __name__ == "__main__":
    arr = [2, 3, 4, -2, 6, 8, 3, 3]
    target_sum = 6

    # Call the paired_elements function
    paired_elements(arr, target_sum)

# Output
# The pair is : (-2, 8)
# The pair is : (2, 4)
# The pair is : (3, 3)

