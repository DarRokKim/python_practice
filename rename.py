import os

# 사진이 있는 폴더에 접근하기
file_path = "C:/Users/eofhr/Downloads/TON2/data"
file_names = os.listdir(file_path)
file_names


# 순서대로 파일 이름은 바꾸고 저장한다.

i = 1
for name in file_names:
    src = os.path.join(file_path, name)
    dst = 'k_' + str(i).zfill(4) + '.jpg' 
    dst = os.path.join(file_path, dst)
    os.rename(src, dst)
    i += 1