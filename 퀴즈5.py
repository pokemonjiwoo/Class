#리스트 변수의 평균 값을 구하는 함수를 작성하시오.
#리스트의 길이는 매번 달라질 수 있음에 유의하고, sum() 함수를 사용할 수 없다.


var = [1, 2, 3, 4, 5, 6, 7, 8, 100]
var2 = [4, 5, 6]
def average_numbers(a) :
    b = 0
    for i in a :
        b = b + i
    result = b/len(a)
    return result
print(average_numbers(var2))
