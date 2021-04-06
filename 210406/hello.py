print('hello 파이썬')
print('파이썬')

#한줄주석
# 파이썬 변수

'''
여러줄주석
ㅇ
ㅇ
ㅇ
'''

#변수 선언 및 초기화
str = '홍길동'
num = 10
print(str)
print('숫자 num: ', num)
print('문자열 str : ', str)

print('숫자: %d'% num)
print('문자열: %s'% str)
PI = 3.14152
print('실수: %.2f'% PI)

#---------------------------
str1 = '홍길동'
str2 = '남'
str3 = '조선 한양 홍대감댁 11번지'
str4 = '무술훈련'
num = 200
print('1.이름 : %s'% str1)
print('2.성별 : %s'% str2)
print('3.나이 : %d살'% num)
print('4.주소 : %s'% str3)
print('5.취미 : %s'% str4)
#---------------------------
line = '--------------------'
title = '개인 주소록'
name = '홍길동'
gender = '남'
age = 200
address = '조선 한양 홍대감댁 11번지'
hobby = '무술훈련'
print(line)
print(title)
print(line)
print('1. 이름: ', name)
print('2. 성별: %s'% gender)
print('3. 나이: %d'% age)
print('4. 주소: ', address)
print('5. 취미: %s'%hobby)
print(line)

print('이름:{0}, 성별:{1}, 나이:{2}'.format(name, gender, age))
print('이름:%s, 성별:%s, 나이:%d' % (name, gender, age))

print(name, gender, age, address, sep='::')
print(name, gender, age, address, sep='/', end='!!')