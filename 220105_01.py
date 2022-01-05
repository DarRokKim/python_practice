def print_twice(text):
    print(text)
    print(text)

print_twice("안녕")

list_data = [10, 20, 30, 40]
list_data2 = [20, 30, 40, 50]

length = len(list_data)
max_result = list_data[0]
for i in range(length):
    if max_result < list_data[i]:
        max_result = list_data[i]
        
print("최댓값은 ", max_result)

length = len(list_data2)
max_result = list_data2[0]
for i in range(length):
    if max_result < list_data2[i]:
        max_result = list_data2[i]
        
print("최댓값은 ", max_result)

def function_f(input_x):
    output_x = input_x*input_x
    return output_x

list_data = [10, 20, 30, 40]
list_data2 = [20, 30, 40, 50]

def max_function(x):
    length = len(x)
    max_result = x[0]
    for i in range(length):
        if max_result < x[i]:
            max_result = x[i]
    return max_result

print("최댓값은 ", max_function(list_data))
# print("최댓값은 ", max_function(list_data2))

list_data = [30, 20, 30, 40]

def minmax_function(x_list):
        
    def inner_min_function(x):
        length = len(x)
        min_result = x[0]
        for i in range(length):
            if min_result > x[i]:
                min_result = x[i]
        return min_result
    
    def inner_max_function(x):
        length = len(x)
        max_result = x[0]
        for i in range(length):
            if max_result < x[i]:
                max_result = x[i]
        return max_result
        
    x_min = inner_min_function(x_list)
    x_max = inner_max_function(x_list)
    
    minmax_list = [x_min, x_max]

    return minmax_list

print("최솟값, 최댓값 : ", minmax_function(list_data))
print("최솟값 : ", minmax_function(list_data)[0])
print("최댓값 : ", minmax_function(list_data)[1])

def list_mul(x):
     return x * 2

result = list(map(list_mul, [1, 2, 3]))
print(result)

# 각 함수를 실행할 때마다 어떤 결과가 나오는지 궁금하다면 아래 주석을 풀고 실행해보세요! 
# map_res = map(list_mul, [1, 2, 3])
# print(map_res)
# list_map_res = list(map_res)
# print(list_map_res)

result = list(map(lambda i: i * 2, [1,2,3]))
print(result)

# mycalculator.py

test = "you can use this module."

def add(a,b):
	return a+b

def mul(a,b):
	return a*b

def sub(a,b):
	return a-b
   
def div(a,b):
	return a/b
    
class all_calc():

	def __init__(self, a, b):
		self.a = a
		self.b = b

	def add(self):
		return self.a + self.b
        
	def mul(self):
		return self.a * self.b

	def sub(self):
		return self.a - self.b

	def div(self):
		return self.a / self.b