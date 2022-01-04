# 딕셔너리
conductor = {'first_name' : '단테', 'last_name' : '안'}
# print(conductor['first_name'])

conductor['gender'] = 'male'

# conductor.pop('last_name')
# print(conductor)

for key, value in conductor.items():
    print(key + ':' + value)

###########

# FibonaChicken

def FibonaChicken(n):
    if n <= 2:
        number = 1
    else:
        number = FibonaChicken(n-1) + FibonaChicken(n-2)
    return number

print(FibonaChicken(20))

################

# memoization 프로그래밍에서 중간값을 기억해 두고 다시 계산하는 대신 값을 바로 읽어 쓰는 방식

memory = {1: 1, 2: 1}

def fibonacci(n):
    if n in memory:
        number = memory[n]
    else:
        number = fibonacci(n-1) + fibonacci(n-2)
        memory[n] = number
    return number

print(fibonacci(40))

print(memory)

################

# 문자열

my_str = 'Welcome!'
ur_str = "You're welcome"

print(my_str)
print(ur_str)

print(type(my_str))
print(type(ur_str))

#################

# 이스케이프 문자

# s = 'I don't like Python' # ' 가 세 개가 되니 뒤에 문자열은 인식을 못함

# 이스케이프 문자를 무시하고 싶을 떄는 원시 문자열을 사용한다
# 문자열 시작 따옴표 앞에 r을 붙으면 이스케이프 문자가 적용되지 않음

print('Please don\'t touch it')
print(r'Please don\'t touch it')

#################

# startswith

EmployeeID = ['OB45382', 'OW32185', 'OB84153', 'OB94382', 'OW34723', 'OB32308', 'OB83461', 'OB74830', 'OW37402', 'OW11235', 'OB82345']

Production_Employee = [P for P in EmployeeID if P.startswith('OB')] # 0B로 시작하는 직원을 추린다
print(Production_Employee)

################

# endswith

import os
image_dir_path = os.getenv("HOME") + "/data/pictures"   
# 각자의 사진이 보관된 디렉토리를 골라 주세요. 
# 클라우드의 경우에는 사진이 이미 있으므로 코드를 실행시켜주세요. 
photo = os.listdir(image_dir_path )
png = [png for png in photo if png.endswith('.png')]
print(png)

################

str = "Life is what you make of it"
print(str.upper())
print(str.lower())
print(str.capitalize())

################

# 정규 표현식

import re
#1단계 :  "the"라는 패턴을 컴파일한 후 패턴 객체를 리턴합니다. 
pattern = re.compile("the")    

# 2단계 : 컴파일된 패턴 객체를 활용하여 다른 텍스트에서 검색을 수행합니다.
pattern.findall('of the people, for the people, by the people')

# 1단계를 거치지 않고도 한 줄로 동일한 처리가 가능
re.findall('the', 'of the people, for the people, by the people')

################

src = "My name is..."
regex = re.match("Your", src)
print(regex)
if regex:
    print(regex.group())
else:
    print("No!")

################

#- 연도(숫자) 찾기
import re

text = """
The first season of America Premiere League  was played in 1993. 
The second season was played in 1995 in South Africa. 
Last season was played in 2019 and won by Chennai Super Kings (CSK).
CSK won the title in 2000 and 2002 as well.
Mumbai Indians (MI) has also won the title 3 times in 2013, 2015 and 2017.
"""
pattern = re.compile("[1-2]\d\d\d")
pattern.findall(text)

################

#- 전화번호(숫자, 기호)
phonenumber = re.compile(r'\d\d\d-\d\d\d\d-\d\d\d\d')
phone = phonenumber.search('This is my phone number 010-1111-1111')
if phone:
  print(phone.group())
print('------')
phone = phonenumber.match ('This is my phone number 010-1111-1111')
if phone:
  print(phone.group())

################

#- 이메일(알파벳, 숫자, 기호)
text = "My e-mail adress is doingharu@aiffel.com, and tomorrow@aiffel.com"
pattern = re.compile("[0-9a-zA-Z]+@[0-9a-z]+\.[0-9a-z]+")
pattern.findall(text)