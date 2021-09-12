# [180, 5000, 10, 600]
# ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
# [14600, 34400, 5000]
import datetime
from collections import Counter
import math

def cal_min(in_time,out_time):
    # ex)cal_min("05:34","06:00")  -> return 26
    time_1,time_2 = in_time,out_time
    splited_1 = time_1.split(":")  #IN
    splited_2 = time_2.split(":")  #OUT
    time_1 = datetime.timedelta(hours= int(splited_1[0]), minutes=int(splited_1[1]))
    time_2 = datetime.timedelta(hours= int(splited_2[0]) , minutes=int(splited_2[1]))
    take_time = str(time_2 - time_1).split(':')
    taken_time_min = int(take_time[0])*60 + int(take_time[1])  #시간차이를 분으로 나눠준 것.

    return taken_time_min

# print(cal_min("05:34","06:00"))  -> 시간계산 테스트 확인 완료 26

def charged(fees,minute):
    basic_min,basic_fee,dan_min,dan_fee = fees[0],fees[1],fees[2],fees[3]
    if minute <= 180:
        return fees[1]
    else:
        return basic_fee + math.ceil((minute-basic_min)/dan_min) * dan_fee

# print("chargee",charged([180, 5000, 10, 600],334))  -> 0000차량 14600 출력확인

def solution(fees, records):

    record_car_num = []
    sep_rec = [] #기록 구분(시간 번호)
    for i in records:
        # print(i.split(" ")[1])
        record_car_num.append(i.split(" ")[1])
        sep_rec.append(i.split(" "))
    car_num = set(record_car_num)
    # print(sep_rec)

    #들어오고 나간차: 카운트횟수가 짝수 out_ok/ 나가지 않은 차:카운트횟수가 홀수 out_no

    out_ok,out_no = [],[]
    print(Counter(record_car_num))
    for i in car_num:
        if Counter(record_car_num)[i] % 2 == 0:
            out_ok.append(i)
        else:
            out_no.append(i)
        # print("?",Counter(record_car_num)[i])
        # print("_",i)

    #최종 답안과 효율을 위한 출입차량 번호별 오름차순 정렬
    for_carnum_record = sorted(sep_rec, key=lambda x: x[1])
    print("차번호 정렬",sorted(sep_rec,key= lambda x:x[1]))
    print("out_ok,out_no",out_ok,out_no)


    #out_no에 있는 차라면 시간 계산할때 out_time => 23:59에 출차
    print("??",Counter(record_car_num).values())

    sunseo = sorted(record_car_num)

    print(sunseo.append)
    while True:
        if

    # return answer

print(solution([180, 5000, 10, 600],
               ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))