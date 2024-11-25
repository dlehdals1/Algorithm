import sys

str = sys.stdin.readline().strip()
bomb = list(sys.stdin.readline().strip())
b = len(bomb)

stack = []

for i in str:
    stack.append(i)
    if stack[:-b:] == bomb:
        for _ in range(b):
            stack.pop()
print(''.join(stack) if stack else 'FRULA')
# if stack:
#     print(*stack, sep="")
# else:
#     print("FRULA")

# i = 0
# while i <= len(str) - len(bomb):
# # for i in range(0, len(str) - len(bomb)):
#     i += 1
#     if str and str[i:i + len(bomb)] == bomb:
#         str = str[:i] + str[i + len(bomb):]
#         i  = max(0, i - len(bomb))
        
# if str == bomb:
#     print("FRULA")
# else:
#     print(str)