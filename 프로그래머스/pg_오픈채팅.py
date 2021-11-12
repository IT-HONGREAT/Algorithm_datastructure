
result = []
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
save_information = {}

for i in record:
    if 'Enter' in i:  # leave는 닉네임이 없어서 아무것도 없는 문자열이 딕셔너리에 저장되기 때문에,딕셔너리생성 조건을 만들었다.
        id = i[6:13]  #key
        name = i[14:]  #val

        save_information[id] = name


for j in record:
    #입장
    if 'Enter' in j:
        enter_people = save_information[j[6:13]]    #key를 활용해 value를 변수로
        put = f"{enter_people}님이 들어왔습니다"  #변수인 value를 포매팅
        result.append(put)
    #퇴장
    elif 'Leave' in j:
        leave_people = save_information[j[6:13]]
        out = f"{leave_people}님이 나갔습니다"
        result.append(out)

    elif 'Change' in j:
        #change가 있는 문자열의 id값을 갖고있는, 리스트의 이름을 새로운걸로 바꿔줘야함.
        save_information[j[7:14]] = j[15:19]  #7:14 는 아이디임

        for c in result:
            if j[7:14] in c:  #결과리스트의 각 문장에 id가 있으면..
                j[7:14] = save_information[j[7:14]]

print(save_information)
print(result)
