def sortColors(nums):
        for pos in range(len(nums)-1):
            min_ = pos
            for i in range(pos+1,len(nums)):
                if nums[i]<nums[min_]:
                    min_ = i
            nums[pos], nums[min_]= nums[min_], nums[pos]
        return nums

print(sortColors([4,6,2,1,7,9]))