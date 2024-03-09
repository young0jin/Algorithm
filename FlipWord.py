#문자열 뒤집기 (완)

"""
import sys

num = int(sys.stdin.readline())
output = ""
line = ""
for _ in range(num):
    line = sys.stdin.readline().split()
    for word in line:
        output += word[::-1]
        output += " "
    output += "\n"
print(output.rstrip("\n"))
"""

import sys

num = int(sys.stdin.readline())

for _ in range(num):
    line = sys.stdin.readline().split()
    for word in line:
        print(word[::-1], end= " ")
    print()


            
        