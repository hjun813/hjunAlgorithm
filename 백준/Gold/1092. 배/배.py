import sys

# 입력 속도 향상을 위해 sys.stdin.readline 사용 권장
input = sys.stdin.readline

N = int(input())
weightLimit = list(map(int, input().split()))
M = int(input())
boxWeight = list(map(int, input().split()))

# 내림차순 정렬
weightLimit.sort(reverse=True)
boxWeight.sort(reverse=True)

# 예외 처리: 가장 무거운 박스를 가장 힘센 크레인도 못 들면 -1
if weightLimit[0] < boxWeight[0]:
    print(-1)
else:
    time = 0
    # 박스가 다 없어질 때까지 반복
    while boxWeight:
        time += 1
        # 이번 시간에 각 크레인이 박스를 하나씩 처리
        for crane in weightLimit:
            # 남은 박스가 없으면 중단
            if not boxWeight:
                break
            
            # 크레인이 들 수 있는 가장 무거운 박스를 찾음
            # 내림차순 정렬되어 있으므로 앞에서부터 찾으면 됨
            for i in range(len(boxWeight)):
                if crane >= boxWeight[i]:
                    del boxWeight[i] # 박스 제거 (메모리/시간 효율)
                    break # 이 크레인은 이번 턴 종료
    print(time)