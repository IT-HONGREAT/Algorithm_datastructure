def insertion_sort(n_list):


    for idx in range(len(n_list)):
        # 1)
        for now_idx in range(idx, 0, -1):
            if n_list[now_idx - 1] <= n_list[now_idx]:
                break

            n_list[now_idx], n_list[now_idx - 1] = n_list[now_idx - 1], n_list[now_idx]
            # print(bef_s_list)

        # 2)
        # now_idx = idx
        # print(f"index: {idx}, {bef_s_list}")

        # while now_idx > 0 and bef_s_list[now_idx-1] > bef_s_list[now_idx]:
        #     bef_s_list[now_idx], bef_s_list[now_idx-1] = bef_s_list[now_idx-1], bef_s_list[now_idx]
        #     now_idx -= 1
        #     print(bef_s_list)

    return n_list

#
# def selection_sort(num_list):
#     bef_s_list = num_list.copy()
#
#     for i in range(len(bef_s_list)):
#         # 1)
#         min_idx = i
#         for j in range(i, len(bef_s_list)):
#             if bef_s_list[j] < bef_s_list[min_idx]:
#                 min_idx = j
#         print(bef_s_list)
#         # 2)
#         # min_val = min(bef_s_list[i:])
#         # min_idx = bef_s_list.index(min_val)
#
#         bef_s_list[i], bef_s_list[min_idx] = bef_s_list[min_idx], bef_s_list[i]
#         # print(bef_s_list)
#
#     return bef_s_list
#
#
# def bubble_sort(num_list):
#     bef_s_list = num_list.copy()
#
#     # for i in range(len(bef_s_list)-1):
#     #     if bef_s_list[i] > bef_s_list[i+1]:
#     #         bef_s_list[i], bef_s_list[i+1] = bef_s_list[i+1], bef_s_list[i]
#
#     # for i in range(len(bef_s_list)-2):
#     #     if bef_s_list[i] > bef_s_list[i+1]:
#     #         bef_s_list[i], bef_s_list[i+1] = bef_s_list[i+1], bef_s_list[i]
#
#     # for i in range(len(bef_s_list)-3):
#     #     if bef_s_list[i] > bef_s_list[i+1]:
#     #         bef_s_list[i], bef_s_list[i+1] = bef_s_list[i+1], bef_s_list[i]
#
#     # ....
#
#     is_swapped = False
#                                     #길이가 6일때
#     for i in range(len(bef_s_list)): #i => 0,1,2,3,4,5
#         for j in range(len(bef_s_list) - i - 1):   #길이자체를 조정 5,4,3,2,1,0
#             if bef_s_list[j] > bef_s_list[j + 1]:
#                 bef_s_list[j], bef_s_list[j + 1] = bef_s_list[j + 1], bef_s_list[j]
#                 is_swapped = True
#                 print(bef_s_list)
#         if not is_swapped:
#             break
#
#     return bef_s_list


n = int(input())
num_list = []

for _ in range(n):
    num = int(input())
    num_list.append(num)

insertion_sorted_list = insertion_sort(num_list)
print(" ".join(map(str, insertion_sorted_list)))

# selection_sorted_list = selection_sort(num_list)
# print(" ".join(map(str, selection_sorted_list)))

# bubble_sorted_list = bubble_sort(num_list)
# print(" ".join(map(str, bubble_sorted_list)))