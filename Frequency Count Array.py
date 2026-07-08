arr = [1, 4, 1, 2, 7, 5, 2]
count_arr = [0] * 10

for num in arr:
    count_arr[num] += 1

print("Frequency count array:", count_arr)
