from typing import List


def combine(k: int, n: int) -> List[List[int]]:
    """
    :param k: 表示个数
    :param n: 表示值范围长度
    :return:
    """
    ret = []

    def dfs(data: List[int], start: int):
        if len(data) == k:
            ret.append(data)
            return

        for i in range(start, n + 1):
            d = data.copy()
            d.append(i)
            dfs(d, i + 1)

    dfs([], 1)

    return ret


# print(combine(2, 4))


def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    ret = []
    _hash = set()

    def dfs(data: List[int], start: int) -> None:
        key = str(len(data)) + "_"
        for i in data:
            key += str(i)

        if key in _hash:
            return

        _hash.add(key)
        ret.append(data)

        for i in range(start, len(nums)):
            d = data.copy()
            d.append(nums[i])
            dfs(d, i + 1)

    dfs([], 0)
    return ret


# print(subsetsWithDup([1, 2, 2]))


def minimumTotal2(nums: List[List[int]]) -> int:
    if not len(nums):
        return 0

    ret = float("inf")

    def dfs(d_sum: int, cur_x: int, cur_y: int):
        nonlocal ret

        if cur_x >= len(nums):

            if d_sum < ret:
                ret = d_sum
            return

        dfs(d_sum + nums[cur_x][cur_y], cur_x + 1, cur_y)
        dfs(d_sum + nums[cur_x][cur_y + 1], cur_x + 1, cur_y + 1)

    dfs(nums[0][0], 1, 0)
    return int(ret)


# print("222: ", minimumTotal2([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))



