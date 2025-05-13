# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val   = val
#         self.left  = left
#         self.right = right
        
class Solution:
    def selfNode(value):
        return TreeNode(value, None, None)

    def middleSplit(left: int, right: int, nums: List[int]):
        if right - left <  0: return None
        if right - left == 0: return Solution.selfNode(nums[left])
        if right - left == 1:
            return TreeNode(
                nums[right],
                Solution.selfNode(nums[left]), 
                None
            )

        mid = (right + left) // 2

        return TreeNode(
            nums[mid],
            Solution.middleSplit(left , mid-1, nums),
            Solution.middleSplit(mid+1, right, nums)
        )
    
    def sortedArrayToBST(self, nums: List[int]):
        tree = Solution.middleSplit(0, len(nums)-1, nums)
        return tree
        
        # ans  = [tree]
        # i    = 0
        # while i < len(ans):
        #     if type(ans[i]) == TreeNode:
        #         temp   = ans[i]
        #         ans[i] = temp.val
        #         ans.append(temp.left)
        #         ans.append(temp.right)
        #     i += 1
        
        # i = len(ans)-1
        # while ans[i] == None:
        #     del ans[i]
        #     i -= 1
        
        # return ans
