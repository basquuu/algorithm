def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if (phone_book[i]) == (phone_book[i+1][:len(phone_book[i])]):
            return False
    return True
    #접두사로 생각하는 건데 해쉬 문제이면 dict 안에 넣어서 생각하기 ? 
    #return answer