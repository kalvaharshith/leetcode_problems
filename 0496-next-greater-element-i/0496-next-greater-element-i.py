class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        for i in range(len(nums1)):
            num = nums1[i]
            for j in range(len(nums2)):
                if nums2[j] == num:
                    for k in range(j + 1, len(nums2)):
                        if nums2[k] > num:
                            res[i] = nums2[k]
                            break
                    break
        return res
                

       
        
        