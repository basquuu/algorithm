def solution(participant, completion):
    
    dict = {}
    #빈 dictionary 만들고 particiapnt에 있고 dict에 있으면 수 추가 아니면 그냥 1 
    for p in participant:
        if p in dict:
            dict[p] += 1
        else:
            dict[p] = 1
    
    for p in completion:
        if p in dict:
            dict[p] -= 1
    
    for p in dict:
         if dict[p] == 1:
            return p