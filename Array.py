def search(nums, target):
        l = 0
        r = len(nums) -1
        index = -1
        while l != r:
            p = l+r
            mid = p//2
            if nums[mid] == target:
                index = mid
                break
            else:
                if nums[mid] < target:
                    l = mid+1
                else:
                    r = mid
        return index

print(search([-1,0,3,5,9,12],12))
