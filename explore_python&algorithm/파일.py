

#파일 읽기1
import csv
from random import randint

f = open('./resource/review.txt','r')
content = f.read()
print(content)
print(dir(f))
f.close()#한번 사용한 리소스는 반드시 닫아줘야한다

print(2)
#파일 읽기2 _ close 안해도됨
with open('./resource/review.txt','r') as f:
    c = f.read()
    print(c)
    print(list(c))
    print(iter(c))

print(3)
#파일 읽기3
with open('./resource/review.txt','r') as f:
    for c in f:
        print(c.strip())
print(4)
#파일 읽기4
with open('./resource/review.txt','r') as f:
    content = f.read()
    print(">", content)
    content = f.read()
    print(">", content)

print(5)
#파일 읽기5
with open('./resource/review.txt','r') as f:

    line = f.readline()

    while line:
        print(line, end="##")
        line = f.readline()

print(6)
#파일 읽기 6
with open('./resource/review.txt') as f:
    contents = f.readlines() #리스트를 출력
    print(contents)
    for c in contents:
        print(c, end= "**")

print(7)
#파일 읽기 7
with open('./resource/score.txt') as f:
    score = []
    for line in f:
        score.append(int(line))
    print(score)
    print("평균구하기: {:6.3}".format(sum(score)/len(score)))


#파일 쓰기 1
with open("./resource/text1.txt","w") as f:
    f.write("Hello World!\n")

#파일 쓰기 2
with open("./resource/text1.txt","a") as f:
    f.write("Hello New World!\n")

#파일 쓰기 3
with open("./resource/text2.txt","w") as f:
    for i in range(6):
        f.write(str(randint(0,50)))
        f.write('\n')

#파일 쓰기 4 _ 리스트를 파일로
with open("./resource/text3.txt","w") as f:
    test = ["hong\n","in\n","yeong\n"]
    f.writelines(test)

#파일 쓰기 4 _ 프린트의 파일옵션
with open("./resource/text4.txt","w") as f:
    print("test context!", file=f)
    print("test context22!", file=f)




# 파일 읽고 응용

with open('./resource/a.csv','r') as f:

    a = csv.reader(f)

    answer = []
    for i in a:
        line = 0

        for j in i:
            line += int(j)
        answer.append(line)
    print(sum(answer))
        # print("띠용?",answer)