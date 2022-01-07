# 타이핑 게임 제작 및 기본

import random
import time
words = [] # 영단어 1000개 로드

n = 1  # 게임 시도 횟수
cor_cnt = 0 # 정답 개수

with open('/explore_python&algorithm/resource/word.txt', 'r') as f:

    for i in f:
        words.append(i.strip())

print(words) # 단어 리스트

input("Ready? Press Enter Key!") #Enter Game Start!

start = time.time()

while n <= 5:

    random.shuffle(words)
    q = random.choice(words)

    print()
    print("*Question : {}".format(n))
    print(q)

    x = input()

    print()

    if str(q).strip() == str(x).strip():

        print("pass!")
        cor_cnt += 1
    else:
        print("wrong!")

    n += 1

end = time.time()
et = end - start # 총게임시간
et = format(et, ".3f")

if cor_cnt >= 3:
    print("합격")
else:
    print("불합격")

print("소요시간 : {} 초, 정답개수 : {}".format(et, cor_cnt))

# 시작 지점

if __name__ == '__main__':
    pass
