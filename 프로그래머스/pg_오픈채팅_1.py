def solution(record):
    # record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
    new = [] #문자열을 분리후 리스트로 구분함
    temp_dict = {}
    answer = []
    result = []

    for i in record:
        seper = i.split(" ")
        new.append(seper)



    for i in new:
        if i[0] == 'Enter':
            temp_dict[i[1]] = i[2]
            # answer.append(f"{temp_dict[i[1]]}님이 입장했습니다")
        # elif i[0] == 'Leave':
            #leave에는 이름이 안들어가있으므로 leave의 i[1]과 같은 문자를 갖고있는 리스트의 i[2]를 넣어줘야한다.

            # answer.append(f"{temp_dict[i[1]]}님이 나갔습니다")  # leave 할때 당사자 오류(1)
        elif i[0] == 'Change':

            temp_dict[i[1]] = i[2]

    #딕셔너리는 잘 바뀌었으니까 리스트new의 각 인덱스[1]와 일치하는 딕셔너리의 key를 받아서 리스트로 뽑아내보기.
    for a in new:
        id = temp_dict[a[1]]
        act = a[0]
        if act == "Enter":
            result.append(id+"님이 들어왔습니다.")
        elif act == "Leave":
            result.append(id+"님이 나갔습니다.")

    return result
# print(temp_dict)
# print(new)
# print(answer)
# print(result)

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))



