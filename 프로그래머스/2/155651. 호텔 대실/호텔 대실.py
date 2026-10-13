def solution(book_time):
    answer = 0
    
    time = []
    for i in range(len(book_time)):
        st_h, st_m = map(int, book_time[i][0].split(":"))
        end_h, end_m = map(int, book_time[i][1].split(":"))
        
        startT = st_h * 60 + st_m
        endT = end_h * 60 + end_m + 10
        
        time.append([endT, startT])
    
    time.sort(reverse = True)
    
    room = []
    max_room = 0
    
    for i in range(len(book_time)):
        flag = 1
        temp = []
        for j in range(len(room)):
            if room[j] >= time[i][0]:
                # 끝나는 시간보다 먼저 끝나면
                # 방이 빔
                flag = 0
        if flag == 1:
            room.append(time[i][1])
        else:
            for j in range(len(room)):
                if room[j] < time[i][0]:
                    temp.append(room[j])
            temp.append(time[i][1])
            room = temp
        
        max_room = max(max_room, len(room))
        
    
        
    answer = max_room
    return answer