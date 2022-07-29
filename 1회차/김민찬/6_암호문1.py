import sys

sys.stdin = open("_암호문1.txt")

for i in range(1, 11): # 원본 암호문의 길이(10개 숫자 출력하기 위해)
    N = int(input())
    password = list(map(int, input().split()))
    