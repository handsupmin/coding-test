# LowerBound.py
# 정렬 된 배열(nums)에서 찾고자 하는 값(target) 이상이 처음 나타나는 위치
# nums[k-1] < target 이고 nums[k] >= target인 k를 찾는다
# bisect_left

def lower_bound(nums, target):
    
    left, right = 0, len(nums) - 1
    
    while left < right:  #left와 right가 만나는 지점이 target값 이상이 처음 나오는 위치
        mid = (left + right)  // 2
        
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return right

nums = [100, 101, 108]
print(lower_bound(nums, 101))