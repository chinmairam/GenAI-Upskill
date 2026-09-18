# Task 1
import numpy as np
arr_oned = np.arange(1,11)
arr_twod = np.arange(1, 10).reshape(3,3)
arr_from_list = np.array([10,20,30,40,50])
print(arr_oned.shape)
print(arr_oned.dtype)
print(arr_twod.shape)
print(arr_twod.dtype)
print(arr_from_list.shape)
print(arr_from_list.dtype)

# Task 2
A = np.array([10,20,30,40])
B = np.array([1,2,3,4])
print(A+B)
print(np.add(A,B))
print(A-B)
print(np.subtract(A,B))
print(A*B)
print(A/B)
print(A**2)

# Task 3
values = np.array([2,4,6,8,10])
print(np.sqrt(values))
print(np.exp(values))
print(np.log(values))
print(np.sum(values))
print(np.cumsum(values))

# Task 4
data = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])
print('Row-wise Sum: ', np.sum(data, axis=1))
print('Column-wise Sum: ', np.sum(data, axis=0))
print('Min Value: ', np.min(data))
print('Max Value: ', np.max(data))
print('Mean: ', np.mean(data))

# Task 5
marks = np.array([78,85,90,66,72,88,95,60])
print('Mean:', np.mean(marks))
print('Median:', np.median(marks))
print('Variance:', np.var(marks))
print('S.D:', np.std(marks))
min_val = np.min(marks)
max_val = np.max(marks)
print('Min:', min_val)
print('Max:', max_val)
print('Range:', max_val-min_val)

# Task 6
sorted_marks = np.sort(marks)
print('Sorted Marks:', sorted_marks)
print('25th Percentile: ', np.percentile(sorted_marks, 25))
print('50th Percentile: ', np.percentile(sorted_marks, 50))
print('75th Percentile: ', np.percentile(sorted_marks, 75))
mean_marks = np.mean(sorted_marks)
print('Mean Marks:', mean_marks)
count_gt_mean = np.sum(sorted_marks > mean_marks)
print('Count of Marks Greater than Mean:', count_gt_mean)
# Another way
res = np.where(sorted_marks > mean_marks)
print('Count of Marks Greater than Mean using np.where:', len(sorted_marks[res]))

# Task 7
sales = np.array([1200,1500,900,2000,1800,1700,1600])
print('Total Sales:', np.sum(sales))
mean_sale = np.mean(sales)
print('Average Sales:', mean_sale)
print('Highest Sales:', np.max(sales))
print('Lowest Sales:', np.min(sales))
print('S.D of Sales:', np.std(sales))
sales_above_avg = np.where(sales > mean_sale)
print('Days where Sales > Avg: ', sales_above_avg[0])