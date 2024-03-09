#괄호가 있는 문자열을 모든 괄호가 쌍을 이루는지 찾는것
# 입력은 T개의 테스트 데이터, 제일 첫 줄에서 T 입력 (완)
import sys

dataNum = int(input())
output = ""
for _ in range(dataNum):
    command = sys.stdin.readline().strip()

    stack = []
    for char in command:
        if char == ')' and len(stack) == 0:
            output += "NO\n"
            break
        else:
            if char == '(':
                stack.append(char)
            else:
                stack.pop()
    else: 
        output += "YES\n"  if len(stack) == 0 else "NO\n"
        stack = []
    
print(output.rstrip('\n'))
