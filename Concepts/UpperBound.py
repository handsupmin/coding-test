# UpperBound.py
# 정렬 된 배열(nums)에서 찾고자 하는 값(target)보다 큰 값이 처음 나타나는 위치
# nums[k] > target 을 만족하는 최소 k를 찾는다
# bisect_right

def upper_bound(nums, target):

    left, right = 0, len(nums) - 1

    while left < right:  #left와 right가 만나는 지점이 target값 보다 큰 값이 처음 나오는 위치
        mid = (left + right)  // 2

        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid 

    return right

nums = [100, 101, 108]
print(upper_bound(nums, 101))