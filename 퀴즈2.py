#구구단 함수를 작성하시오. 매개변수 입력에 따라 해당 구구단을 화면에 출력하는 함수를 작성하시오.


def mul_numbers(num1) :
    for numbers in range(1, 10) :
        result = num1 * numbers
        print(numbers, 'x', num1, '=', result)

mul_numbers(8)


