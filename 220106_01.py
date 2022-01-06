import numpy as np

# # 아래 A와 B는 결과적으로 같은 ndarray 객체를 생성합니다. 
# A = np.arange(5)
# B = np.array([0,1,2,3,4])  # 파이썬 리스트를 numpy ndarray로 변환

# # 하지만 C는 좀 다를 것입니다. 
# C = np.array([0,1,2,3,'4'])

# # D도 A, B와 같은 결과를 내겠지만, B의 방법을 권합니다. 
# D = np.ndarray((5,), np.int64, np.array([0,1,2,3,4]))

# print(A)
# print(type(A))
# print("--------------------------")
# print(B)
# print(type(B))
# print("--------------------------")
# print(C)
# print(type(C))
# print("--------------------------")
# print(D)
# print(type(D))


# A = np.arange(10).reshape(2, 5)   # 길이 10의 1차원 행렬을 2X5 2차원 행렬로 바꿔봅니다.

# print("행렬의 모양:", A.shape)
# print("행렬의 축 개수:", A.ndim)
# print("행렬 내 원소의 개수:", A.size)


A = np.arange(10)
print('A: ', A)
B = np.arange(10).reshape(2,5)
print('B: ', B)
C = np.arange(10).reshape(3,3)  # 이 줄에서 에러가 날 것입니다.
print('C: ', C)

############

A= np.arange(6).reshape(2, 3)
print(A)
print(A.dtype)
print(type(A))
print("-------------------------")

B = np.array([0, 1, 2, 3, 4, 5])  
print(B)
print(B.dtype)
print(type(B))
print("-------------------------")

C = np.array([0, 1, 2, 3, '4', 5])
print(C)
print(C.dtype)
print(type(C))
print("-------------------------")

D = np.array([0, 1, 2, 3, [4, 5], 6])  # 이런 ndarray도 만들어질까요?
print(D)
print(D.dtype)
print(type(D))

# 3 X 3 행렬에 1 X 3 행렬을 더했을 때
A = np.arange(9).reshape(3,3)
B = np.array([1, 2, 3])
print("A:", A)
print("B:", B)
print("\nA+B:", A+B)

# 3 X 3 행렬에 3 X 1 행렬을 더했을 때
A = np.arange(9).reshape(3,3)
C = np.array([[1], [2], [3]])
print("A:", A)
print("C:", C)
print("\nA+C:", A+C)

# 3 X 3 행렬에 1 X 2 행렬을 더하는 것은 허용되지 않습니다. 
A = np.arange(9).reshape(3,3)
D = np.array([1, 2])
print("A:", A)
print("D:", D)
print("\nA+D:", A+D) # 에러 발생

print([1,2]+[3,4])
print([1,2]+3)

print(np.array([1,2])+np.array([3,4]))
print(np.array([1,2])+3)

# 3 X 3 행렬의 첫번째 행을 구해 봅시다. 
A = np.arange(9).reshape(3,3)
print("A:", A)
B = A[0]
print("B:", B)

# 0, 1을 인덱싱 하면 A의 첫번째 행에서 두번째 값을 참조합니다.
# 아래 두 결과는 정확히 같습니다.
print(A[0, 1])
print(B[1])

# 슬라이싱도 비슷합니다.
A[:-1]

# 이 슬라이싱의 결과는 
print(A[:,2:])
print("--------------")
print(A[:,1:])
print("--------------")
print(A[:,:])
print("--------------")
# 이 슬라이싱의 결과와 동일합니다.
print(A[:,-1:])
print("--------------")
print(A[:,-2:])
print("--------------")
print(A[:,-3:])


print(np.random.random()) 		# 0~1 사이의 실수형 난수 하나를 생성
print(np.random.randint(0,10)) 	# 0~9 사이 1개 정수형 난수 하나를 생성
print(np.random.choice([0,1,2,3,4,5,6,7,8,9])) 	# 리스트에 주어진 값 중 하나를 랜덤하게 고른다

# 무작위로 섞인 배열을 만들어준다, 밑에 두 값은 동일
print(np.random.permutation(10))
print(np.random.permutation([0,1,2,3,4,5,6,7,8,9]))

# 어떤 분포를 따르는 변수를 임의로 표본추출해준다

# 정규분포
print(np.random.normal(loc=0, scale=1, size=5))		# 평균(loc), 표준편차(scale), 추출 개수(size)

# 균등분포
print(np.random.uniform(low=1, high=1, size=5)) 	# 최소(low), 최대(high), 추출개수(size)


A = np.arange(24).reshape(2,3,4)
print("A : ", A)		# A는 (2,3,4) 모양의 행렬
print("A의 전치행렬 : ", A.T)
print("A의 전치행렬의 shape : ", A.T.shape)	# A의 전치행렬은 (4,3,2) 모양의 행렬

# np.transpose는 행렬의 축을 어떻게 변환해 줄지 임의로 지정해 줄 수 있다.
B = np.transpose(A, (2,0,1))
print("A : ", A)		# A는 (2,3,4) 모양의 행렬
print("B : ", B)		# B는 A의 3,1,2 번째 축을 자신의 1,2,3번째 축으로 가진 행렬
print("B.shape : ", B.shape)	# B는 (4,2,3) 모양의 행렬

# np.transpose(A, (2,1,0))은 A.T와 같다

print("B.shape : ", B.shape)


import numpy as np

def numbers():
    X = []
    number = input("Enter a number (<Enter key> to quit)") 
    # 하지만 2개 이상의 숫자를 받아야 한다는 제약조건을 제외하였습니다.
    while number != "":
        try:
            x = float(number)
            X.append(x)
        except ValueError:
            print('>>> NOT a number! Ignored..')
        number = input("Enter a number (<Enter key> to quit)")
    return X

def main():
    nums = numbers()       # 이것은 파이썬 리스트입니다. 
    num = np.array(nums)   # 리스트를 Numpy ndarray로 변환합니다.
    print("합", num.sum())
    print("평균값",num.mean())
    print("표준편차",num.std())
    print("중앙값",np.median(num))   # num.median() 이 아님에 유의해 주세요.

main()


import matplotlib as mpl
import PIL

print( f'# matplotlib: {mpl.__version__}' )  
print(f'# PIL:  {PIL.__version__}')

from PIL import Image, ImageColor
import os
img_path = os.getenv("HOME") + "/저장 위치/newyork.jpg"
img = Image.open(img_path)
print(img_path)
print(type(img))
img

img.size

print(img.format)
print(img.size)
print(img.mode)

img.crop((30,30,100,100)) # 이미지 자르기

# 자른 이미지 저장하기
# 새로운 이미지 파일명
cropped_img_path = os.getenv("HOME") + "/저장위치/cropped_img.jpg"
img.crop((30,30,100,100)).save(cropped_img_path)
print("저장 완료!")

# 이미지 행렬로 변환

import numpy as np
img_arr = np.array(img)
print(type(img))
print(type(img_arr))
print(img_arr.shape)
print(img_arr.ndim)

img_arr # 행렬의 값 확인

# 컬러 이미지 흑백으로 변환
img_g = Image.open(img_path).convert('L')
img_g

# 행렬로 변환하는 방법은 동일하다
img_g_arr = np.array(img_g)
print(type(img_g_arr))
print(img_g_arr.shape)
print(img_g_arr.ndim)

img_g_arr # 단, 흑백이므로 행렬은 2차원이다

# RGB 값 반환

red = ImageColor.getcolor('RED','RGB')
reda = ImageColor.getcolor('red','RGBA')
yellow = ImageColor.getcolor('yellow','RGB')
print(red)
print(reda)
print(yellow)