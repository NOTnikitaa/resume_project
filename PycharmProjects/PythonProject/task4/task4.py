nums = []

task_4_file = open('task_4_file.txt', 'r')
for num in task_4_file:
    nums.append(int(num.strip()))


srednee_chislo = round(sum(nums)/len(nums))
count = 0
for i in range(len(nums)):
    while nums[i] != srednee_chislo:
        if nums[i] > srednee_chislo:
            nums[i] -= 1
            count += 1
        elif nums[i] < srednee_chislo:
            nums[i] += 1
            count += 1
print(count)