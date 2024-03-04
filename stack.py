#백준 알고리즘 10828 스택
#정수를 저장하는 스택 구현

# push X : 정수 X를 스택에 넣는 연산
# pop X : 가장 위에 있는 정수를 빼고 출력 ( 스택에 수가 없는 경우 -1 )
# size : 스택에 들어있는 정수의 개수
# empty : 스택 비어있으면 1 아니면 0
# top : 스택의 가장 위에 있는 정수 출력 ( 스택에 정수가 없으면 -1 )

#첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.
import sys

def stack():
    stack_size = int(input())
    stack = []

    for _ in range(stack_size):
        command = sys.stdin.readline().split()

        if command[0] == 'push':
            stack.append(command[1])
        elif command[0] == 'pop':
            if len(stack) == 0:
                print("-1")
            else:
                print(stack[-1])
                stack.pop()
        elif command[0] == 'size':
            print(len(stack)) 
        elif command[0] == 'empty':
            print("1") if len(stack) == 0 else print("0")
        elif command[0] == 'top':
            print("-1") if len(stack) == 0 else print(stack[-1])

stack()