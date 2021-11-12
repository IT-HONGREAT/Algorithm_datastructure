from collections import Counter

N = int(input())
nlist = []

for _ in range(N):
    nlist.append(int(input()))

# N개의 친구들이 있는 리스트 nlist
def san_ave(N,nlist):

    return int(sum(nlist)//N)

def mid(N,nlist):

    s = sorted(nlist)
    return s[N//2]

def choi_bin(nlist):
    a = Counter(nlist) #리스트에서 뭐가 몇개인지 세기
    nd = {}  #카운터타입을 딕셔너리로 바꿔주기
    for i in a:
        nd[i] = a[i]

    choi_bin_num = max(nd.values())  #최빈값 #사전의밸류가 왓이즈최빈넘버
    find_choi = []  #최빈값이 여러개일 경우를 대비해서 리스트에 담아주는 것.

    for j in nd:
        if nd[j] == choi_bin_num:
            find_choi.append(j)
    kind_choi = sorted(find_choi)
    print(kind_choi)
    #최빈값이 여러개면 두번째로 작은 값을 돌려주자.
    if len(find_choi) >= 2:
        return kind_choi[1]

    else:
        return kind_choi[0]

def bum(nlist):

    return max(nlist)-min(nlist)


print(san_ave(N,nlist))
print(mid(N,nlist))
print(choi_bin(nlist))
print(bum(nlist))
# print(nlist)