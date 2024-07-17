#학점 변환기 함수, 점수 구간에 해당하는 학점이 아래와 같이 정의 되어있다.
#사용자로부터 score를 입력 받아 학점으로 환산하여 반환하는 함수를 작성하여라.


def 학점 (data) :
    result = 0
    if 80 < data <= 100 :
        print("A")
        result ="A"
    if 60 < data <= 80 :
        print("B")
        result = "B"
    if 40 < data <= 60 :
        print("C")
        result = "C"
    if 20 < data <= 40 :
        print("D")
        result = "D"
    if 0 < data <= 20 :
        print("E")
        result = "E"
    return result
num = int(input("학점을 입력해주세요."))
a = 학점(num)
print(a)
