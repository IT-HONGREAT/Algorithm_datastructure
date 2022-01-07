# 파이썬 외부 파일 처리

# 파이썬 Excel, CSV 파일 읽기 및 쓰기

#CSV 가 전부 , 구분되어있는 것은 아니다
import csv



#1
with open('sample1.csv','r',encoding='cp949') as f:

    reader = csv.reader(f)
    #컬럼명 스킵할때
    # next(reader)


    #확인 과정
    print(reader)
    print(type(reader))
    print(dir(reader))  # __iter__ 가 있으면 반복문에서 사용가능하기 때문에 반목문으로 출력해본다.
    print()

    for i in reader:
        print(i)

#2
with open('sample2.csv','r',encoding='cp949') as f:

    reader = csv.reader(f, delimiter='|')   # csv파일 중에 '|' 등의 기호로 구분되어있는 것들도 있기 때문에, delimiter옵션을 사용해서 split해준다.

    #컬럼명 스킵할때
    # next(reader)


    #확인 과정
    print(reader)
    print(type(reader))
    print(dir(reader))  # __iter__ 가 있으면 반복문에서 사용가능하기 때문에 반목문으로 출력해본다.
    print()

    for i in reader:
        print(i)


#3
with open('sample1.csv','r',encoding='cp949') as f:

    reader = csv.DictReader(f)

    for i in reader:
        print(i)
        # 딕셔너리 형태를 가져올때 tip
        for k, v in i.items():
            print(k, v)

        print('_______')

#4 반목문사용

w = [ [i+(j*3) for i in range(1,4)] for j in range(6)]

with open('sample3.csv','w',newline='') as f:

    wt = csv.writer(f)

    for v in w:
        wt.writerow(v)

#5 _ 반복문을 안쓰고 사용 write뒤에 s 붙히기

with open('sample4.csv','w',newline='') as f:

    wt = csv.writer(f)
    wt.writerows(w)


# XSL, XLSX
# openpyxl, xlsxwriter, xlrd, xlwt, xlutils 등으로 사용할수있다
# 주로 판다스를 사용한다 (openpyxl, xlrd)
# pip install openpyxl
# pip install pandas
# pip install xlrd

import pandas as pd

# 엑셀 시트명 지정가능 sheetname='시트명' 혹은 숫자
# header옵션도 있음, skiprow옵션도있음
test = pd.read_excel('sample.xlsx')

print(test.head())
print('-'*10)

print(test.tail())
print('-'*10)

print(test.shape)
print('-'*10)

# 엑셀이나 csv 다시쓰기

test.to_excel('new.xlsx', index=False)
test.to_csv('new2.csv',index=False)

