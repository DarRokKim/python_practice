f = open("hello.txt", "w")

for i in range(10):
    f.write("안녕")
f.close()

print("완료!")


with open("hello.txt", "r") as f:
    print(f.read())

quotes = ["\n안녕하세요.\n", "반갑습니다.\n", "오랫만입니다.\n"]

with open("hello.txt", "a") as f:
    f.writelines(quotes)

with open("hello.txt", "r") as f:
    hello = f.readlines()
    print(f'위치 : {f.tell()}')
    print(hello)
    print("------------------------")
    f.seek(10)
    print(f'location : {f.tell()}')

#################################

billboardchart = {
  				 1 : ["Tho Box","Roddy Ricch","2019-12-19"],
                 2 : ["Don't Start Now", "Dua Lipa", "2019-11-01"],
                 3 : ["Life Is Good", "Future Featuring Drake", "2020-02-10"],
                 4 : ["Blinding", "The Weeknd", "2019-11-29"],
                 5 : ["Circles", "Post Malone","2019-08-30"]
                 }
                 
with open("billboardchart.csv", "w") as f:
    for i in billboardchart.values():
        data = ",".join(i)
        f.write(data+"\n")

# 위 빌보드 차트에 title, singer, released date 추가

import csv

header = ["title", "singer", "released date"]

with open("billboardchart.csv","r") as inputfile:
    with open("billboardchart_out.csv","w", newline='\n') as outputfile:
        fi = csv.reader(inputfile, delimiter=',')
        fo = csv.writer(outputfile, delimiter=',')
        fo.writerow(header)
        for row in fi:
            fo.writerow(row)

#################################

# pandas를 활용한 csv 파일 저장

# 데이터 준비
fields = ["title", "singer", "released date"]
rows = [ ["Tho Box","Roddy Ricch","2019-12-19"],
               ["Don't Start Now", "Dua Lipa", "2019-11-01"],
               ["Life Is Good", "Future Featuring Drake", "2020-02-10"],
               ["Blinding", "The Weeknd", "2019-11-29"],
               ["Circles", "Post Malone","2019-08-30"]]

# pandas 이용 데이터 csv 파일로 저장
import pandas as pd

df=pd.DataFrame(rows, columns=fields)
df.to_csv('pandas.csv', index=False)

# 동일한 내용 csv.writer 사용해서 수행
import csv

filename = "text.csv"
with open(filename, 'w+', newline='\n') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(fields)
    csv_writer.writerows(rows)

print("끝")

# 반대로 csv 파일 DataFrame으로 변환 시키기

df = pd.read_csv('pandas.csv')
df.head()