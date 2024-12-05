import sys
n = int(sys.stdin.readline())
start = 0
end = 0
sum = 0
count = 0
while start < n:
    if sum < n:
        end += 1
        sum += end
    elif sum > n:
        start += 1
        sum -= start
    else:
        start += 1
        sum -= start
        count += 1

print(count)