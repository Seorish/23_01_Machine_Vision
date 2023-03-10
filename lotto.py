import random
# lotto 번호는 중복값 필요 X , 원하는 개수만큼 돌아야 함

def generate_lotto_numbers(count):
    # 여러개 담아야 하니까 리스트 
    lotto_numbers = []
    # input으로 받은 count만큼 돈다 (조건)
    while len(lotto_numbers) < count:
        # random 의 ranint 함수
        # 랜덤하게 뽑은 값을 number에 할당
        number = random.randint(1, 45)
        # 중복 제거

        # lotto_numbers에 number가 없다면 참
        if number not in lotto_numbers:
            # 이전에 뽑힌 값과 지금 뽑은 값이 같지 않다면 -> 중복이 아니라면
            # 리스트에 추가하기
            lotto_numbers.append(number)
    # return은 while문이 끝나면 실행 
    return lotto_numbers

# 함수 정의 아래 코드 부터 보기

# input 내장함수는 값은 String 형으로 받아옴
# int 로 감싸주면서 String -> int 형으로 바꿔줌
count = int(input("Enter the number of lotto numbers you want to generate(1~100) : "))
lotto_numbers = generate_lotto_numbers(count)
print("Generated lotto numbers:", lotto_numbers)

# 함수 많을 때 함수 찾는 법 
# 함수에 커서 대고 Ctrl+b -> 해당 함수 정의 코드로 이동