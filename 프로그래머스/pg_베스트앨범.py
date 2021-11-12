# ["classic", "pop", "classic", "classic", "pop"]
# [500, 600, 150, 800, 2500]
# return [4, 1, 3, 0]

def solution(genres, plays):

    kind_genres = []    #장르 종류 확인리스트
    hash_brown = {}  #번호 : (장르,횟수)
    for idx, info in enumerate(zip(genres, plays)):
        if info[0] not in kind_genres:
            kind_genres.append(info[0])

        hash_brown[idx] = info  #해시브라운 저장

    #각 장르의 횟수를 찾는 여정

    save = []
    for play in kind_genres:
        playsave = 0
        for j in hash_brown:


            if play in hash_brown[j]:
                playsave += hash_brown[j][1]

        save.append(playsave)    #중복제거한 장르리스트순서에 맞는 플레이 횟수


    #장르,횟수 한 리스트로 묶고 정렬하기
    g_and_p = []
    for g, p in zip(kind_genres, save):

        g_and_p.append((g,p))

    #총 횟수의 내림차순 정렬한 리스트
    rank = sorted(g_and_p, key=lambda x:-x[1])


    #해시 브라운(모든정보 담은 리스트)를 횟수기준으로 내림차순 정렬한 것(딕셔너리).

    sorted_info = sorted(hash_brown, key=lambda x: -hash_brown[x][1])

    #정답 담는 리스트
    answer = []
    #답 찾아가기
    #같은 장르 2개까지만 허용..
    record_two = []
    for f in rank:

        for info_loc in sorted_info:
            genre = hash_brown[info_loc][0]

            if genre == f[0] and record_two.count(genre)<2:
                answer.append(info_loc)
                record_two.append(genre)


    return answer





    # print(sorted(g_and_p, key=lambda x:-x[1]))

    # print(g_and_p)

    # print(sorted(hash_brown, key=lambda x: hash_brown[x][0]))
    # print(hash_brown)
    # print(kind_genres)



print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))

