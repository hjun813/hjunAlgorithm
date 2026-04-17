def solution(cost, hint):
    answer = float('inf')
    n = len(cost)
    getHint = [0 for _ in range(n + 1)]
    
    def stage(s, c):
        nonlocal answer
        
        # 가지치기: 이미 최소 비용을 넘었다면 탐색 중단
        if c >= answer:
            return
            
        # 베이스 케이스: 모든 스테이지를 클리어함
        if s == n + 1:
            answer = min(c, answer)
            return
        
        # 현재 스테이지 클리어 비용 계산
        hintN = min(getHint[s], len(cost[s-1]) - 1)
        clear_cost = cost[s-1][hintN]
        
        # [선택 1] 현재 스테이지 클리어만 함
        stage(s + 1, c + clear_cost)
        
        # [선택 2] 현재 스테이지 클리어 + 힌트 구매
        # (주의: 해당 스테이지에 구매할 수 있는 힌트 데이터가 있을 때만)
        if s-1 < len(hint):
            buy_cost = hint[s-1][0]
            targets = hint[s-1][1:]
            
            # 힌트 적용
            for tmp in targets:
                if tmp <= n:
                    getHint[tmp] += 1
            
            # 다음 스테이지로 (클리어 비용 + 힌트 비용 합산)
            stage(s + 1, c + clear_cost + buy_cost)
            
            # 백트래킹 (복구)
            for tmp in targets:
                if tmp <= n:
                    getHint[tmp] -= 1
    
    stage(1, 0)
    return answer