def solution(w, h):
    end_point = -w, -h
    answer = 0
    square = [[0 for _ in range(w + 1)] for _ in range(h + 1)]

    count = 0

    def check_dfs(x1, y1, x2, y2, now):
        """
        공간좌표
        :param x1:
        :param y1:
        :param x2:
        :param y2:
        tuple(now_x, now_y)
        :param now:
        """

        if (y2 > (h / w) * now) and ((h / w) * now>y1):
            if (x2 > (h / w) * now) and ((h / w) * now>x1):


        return

    for one_line in square:
        for i in range(1, w + 1):
            count += 1
            print(check_dfs(i))

    return answer


print(solution(8, 12))
