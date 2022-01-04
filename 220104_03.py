# my_list 값 하나씩 출력
my_list = ['a', 'b', 'c', 'd']

# for i in my_list:
#     print("값 : ", i)

# for i, value in enumerate(my_list):
#     print("번호 : ", i, " , 값 : " , value)

# result_list = []

# for i in range(2):
#     for j in my_list:
#         result_list.append((i,j))

# print(result_list)

# def get_dataset_list(my_list):
#     result_list = []
#     for i in range(2):
#         for j in my_list:
#             result_list.append((i, j))
#     print('>> {} data loaded..'.format(len(result_list)))
#     return result_list

# for X, y in get_dataset_list(my_list):
#     print(X, y)

# def get_dataset_generator(my_list):
#     result_list = []
#     for i in range(2):
#         for j in my_list:
#             yield(i, j) # 이전의 append 코드 대체
#             print(">> 1 data loaded...")
# dataset_generator = get_dataset_generator(my_list)
# for X, y in dataset_generator:
#     print(X, y)

