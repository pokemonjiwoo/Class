#문자메세지 길이 판별 함수
#문자메시지 길이에 따라 문자 요금이 결정되는 프로그램을 작성하시오. 메시지의 길이가 20 이하이면 5원이이며, 20을 초과하면 100원이다.
#문자메시지를 입력 받아서 문자 요금을 반환하는 코드를 작성하시오.



data = len(input('사용자 입력 값'))
def message (data) :
    result = 0
    if data  <= 20 :
        result = 50
        print("50원")
    else:
        result = 100
        print("100원")
    return result

a = message(data)
print(a)







