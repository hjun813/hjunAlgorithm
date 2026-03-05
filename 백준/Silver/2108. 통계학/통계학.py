import sys
from collections import Counter

# 1. 입력 받기 (속도를 위해 sys.stdin.readline 사용)
input = sys.stdin.readline
n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))

# 정렬 (중앙값, 범위, 최빈값 정렬을 위해 필요)
numbers.sort()

# --- 산술평균 ---
print(round(sum(numbers) / n))

# --- 중앙값 ---
print(numbers[n // 2])

# --- 최빈값 ---
def get_mode(nums):
    # 각 숫자별 빈도수를 딕셔너리 형태로 반환
    counts = Counter(nums).most_common() 
    # counts는 [(숫자1, 빈도수1), (숫자2, 빈도수2)...] 형태이며 빈도수 내림차순 정렬됨
    
    max_freq = counts[0][1] # 가장 높은 빈도수
    
    # 최대 빈도를 가진 숫자들만 뽑기
    modes = []
    for num, freq in counts:
        if freq == max_freq:
            modes.append(num)
        else:
            break # 빈도수가 낮아지면 더 이상 볼 필요 없음
    
    # 최빈값이 여러 개라면 두 번째로 작은 값 (이미 정렬된 리스트라면 index 1)
    # Counter.most_common()은 빈도가 같을 때 원래 리스트 순서를 유지하므로, 
    # numbers가 이미 정렬되어 있다면 modes도 정렬된 상태입니다.
    if len(modes) > 1:
        return modes[1]
    else:
        return modes[0]

print(get_mode(numbers))

# --- 범위 ---
print(numbers[-1] - numbers[0]) 