num1 = 3
num2 = 4
print(type(num1))
print('덧셈:', num1+num2)
print('곱셈:', num1*num2)
print('나머지:', num2 % num1)

res = num1 + num2
print('res:', res)
res += num1
print('res', res)
# ++, -- 지원x
#res = res++
res += 1
res = res + 1
# 비교연산자
print(num1 > num2)
print(num1 == num2)
print(num1 != num2)
# 논리연산자
print(num1 > num2 and num1 < num2)
print(num1 > num2 or num1 < num2)
print(not(num1 > num2))
# 3항 연산자
'''
result = (num > num2) and \
'num1이 num2보다 크다' or \
'num1이 num2보다 작다'
print(result)
'''

# 문자열
str1 = '홍길동'
str2 = '입니다.'
# 문자열(string) 연결
fullStr = str1 + str2
print('문자열 연결:',fullStr)
fullStr = fullStr + '\n' + '안녕하세요'
# '\n', '\t' 사용 가능
print('개행문자:', fullStr)

# 문자열 인덱싱(indexing)
print(str1[0], str1[1], str1[2])

#[] --> 리스트(list)
# 문자열 자르기(slicing)
fullStr = '홍길동 입니다.'
print(fullStr[0:2]) # 0~1까지
print(fullStr[1:]) # 1~끝까지
print(fullStr[:3]) # 처음부터~2까지
print(fullStr[1::2])#처음부터 끝까지 2번째 위치만

# in 연산자
search = '홍길동' in fullStr
print(search)

length = len(fullStr)
print('변수값 크기:', length)

# 입력 처리
print('1번째 숫자 입력: ')
input1 = input()
print(type(input1))
input2 = input('2번째 숫자 입력: ')
print(input2)

# int() : 문자열 -> 숫자
# str() : 숫자 -> 문자열
sum = int(input1) + int(input2)
print('숫자 덧셈: ', sum)
input3 = int(inut('3번째 숫자 입력:'))
print(type(input3))

# 1.원주율이PI를 저장하는 변수 생성 PI=3.14
# 2.원의 반지름 입력받기
# 3.원의 면적 구하기 (반지름x반지름xPI)

# 온도(화씨->섭씨) 구하는 프로그램
# 1.화씨 온도 입력받기
# 2.섭씨온도 = {화씨온도 -32}/1.8
# 3. 섭씨온도 출력하기

# 총점과 평균 구하는 프로그램

# 1.국어, 영어, 수학 점수 입력받기
# 2.총점과 평균값 구하고 출력하기

PI = 3.14
round = int(input('반지름 입력: '))
circle = PI * r * r
print('원의 면적: %d' ,circle)

f = float(input('화씨 온도: '))
c = (f - 32) / 1.8
print('섭씨온도: %d',c)

kor = int(input('국어점수 : '))
eng = int(input('영어점수 : '))
mat = int(input('수학점수 : '))
sum = kor + eng + mat
evg = (kor * eng * mat) / 3
print('총점 평균: %d %d' ,sum ,evg)

# 홀수, 짝수 판단 프로그램(3항 연산자)
# 1.숫자 1개 입력
# 2.홀짝 판단하여 "홀수", "짝수" 출력하기

#########################################
# 동전교환기 프로그램
# 1.동전은 각각 500원, 100원, 50원, 10원
# 2.특정 금액의 지폐 입력받기 (ex: 1360)
# 3.아래 출력형식으로 출력

int(input('숫자입력: '))
result = (numb % 2 == 0) and '짝수입니다' or '홀수입니다'
print(result)

inNum = int(input('숫자입력: '))
outStr = (inNum % 2 == 0) and '짝수입니다' or '홀수입니다'
print(outStr)

print('동전교환기 v1.0')
money = int(input('금액입력: '))

c500 = money//500
money %= 500

c100 = money//100
money %= 100

c50 = money//50
money %= 50

c10 = money//10
money %= 10

print('500원짜리 : %d개' %c500)
print('100원짜리 : %d개' %c100)
print('50원짜리 : %d개' %c50)
print('10원짜리 : %d개' %c10)

coin500 = 0
money = int(input('특정 금액 입력: '))
coin500 = money / 500
nmg = money % 500;
coin100 = nmg / 100

print('나머지: ', nmg)
print('----------------------------')
print('동전교환기 프로그램 v1.0')
print('----------------------------')
print('오백원 개수: %d개' % coin500)
print('백원 개수: %d개' % coin100)
print('오십원 개수: %d개' % coin50)
print('십원 개수: %d개' % coin10)
print('----------------------------')
