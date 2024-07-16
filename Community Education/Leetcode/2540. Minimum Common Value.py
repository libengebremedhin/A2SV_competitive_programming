class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        for i in nums2:
            l, r = 0, len(nums1) -1
            while l <= r:
                mid = (l+r)//2
                if nums1[mid] < i:
                    l = mid + 1
                elif nums1[mid] > i:
                    r = mid - 1
                else:
                    return nums1[mid]
        return -1
        
