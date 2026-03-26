
nums = list(map(int, input().strip().split(',')))

if len(nums) == 1:
    print(nums[0])
    exit()

max_product = 1
negatives = []
zero_count = 0

for num in nums:
    if num == 0:
        zero_count += 1
        continue
    if num < 0:
        negatives.append(num)
    max_product *= num

# If all zeros
if zero_count == len(nums):
    print(0)
    exit()

# If odd number of negatives → remove largest negative (closest to 0)
if len(negatives) % 2 != 0:
    max_neg = max(negatives)  # e.g., -1 > -5
    max_product //= max_neg

# Edge case: only one negative and rest zeros
if len(negatives) == 1 and zero_count + 1 == len(nums):
    print(0)
else:
    print(max_product)