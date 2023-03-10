def multiplication_table(num1):
    for i in range(1,10):
        # 포맷팅
        print(f"{num1} x {i} = {num1 * i}")


num1 = int(input("Enter the first number(1~9): "))
multiplication_table(num1)