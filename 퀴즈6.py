#홀수/짝수 판별기 함수, 매개변수, 입력에 따라 홀수 또는 짝수를 자동으로 판별하는 함수를 작성하시오
#반환되는 값을 '홀수' 또는 '짝수"이다.



def 자동 (a) :
    if a%2 == 1 :
        result = '홀'
    elif a%2 == 0 :
        result = '짝'
    return result

x =자동(int(input("숫자를 입력하세요.")))
print(x)
