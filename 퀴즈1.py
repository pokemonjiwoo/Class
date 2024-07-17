#구구단 2-9단을 출력하라. 출력할 때. 2x3 = 6과같이 어떤 값을 곱하였는지도 함께 출력하라.

for numbers in range(2, 10) :
    for num in range(1, 10) :
        num2= num*numbers

        print(numbers, 'x', num, '=', num2)

