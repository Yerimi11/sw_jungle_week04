# 그리디 : 문제를 풀어나가는 과정, 단계에 있어서 이 단계에서 가장 좋은게 뭔지 보고 가장 좋은 것을 선택하는 것
# 그리디 문제는 정렬 후 차근차근 선택해나감. 대부분의 그리디 문제는 정렬과 동반해서 풀어나감.

# 회의가 끝나는 시간을 기준으로 정렬
import sys
input = sys.stdin.readline
n = int(input())
meeting = []

for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e)) # 튜플 형태로 넣음
# s, e의 순서를 바꾼 모습에서 정렬(정렬 순위 바꿈). -> 튜플 두번째 값인 끝나는 시간 기준으로 정렬 됨
meeting.sort(key=lambda x : (x[1], x[0])) 
end_time = 0
count = 0

for start, end in meeting:
    if start >= end_time: 
        end_time = end # 끝나는 시간 기록
        count += 1
print(count)