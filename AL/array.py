from typing import List


class ArrayLikeSolution(object):

    @staticmethod
    def list_input() -> List[int]:
        l = []
        while True:
            try:
                _num = input("input a number, or place 'n' for break the loop: ")
                if _num == 'n':
                    break
                else:
                    _num = int(_num)

                if _num < 0:
                    print(f'integer must be positive, plz re-input!')
                    continue
                else:
                    l.append(_num)

            except ValueError:
                print(f'number must be integer, plz re-input!')
                continue
        return l

    @staticmethod
    def inputer() -> int:
        while True:
            try:
                _num = int(input("input a number: "))
                if _num < 0:
                    print(f'integer must be positive, plz re-input!')
                    continue
                else:
                    return _num
            except ValueError:
                print(f'number must be integer, plz re-input!')
                continue

    def find_missing_number(self) -> int:
        lst = self.list_input()
        num = self.inputer()
        s1 = (num + 1) * num / 2
        s2 = sum(lst)
        return int(s1 - s2)

    def find_pair(self) -> List[int]:
        lst = self.list_input()
        num = self.inputer()
        for idx in range(len(lst)):
            diff = num - lst[idx]
            if diff in lst:
                if idx != lst.index(diff):
                    return [idx, lst.index(diff)]

    def find_number(self) -> int:
        lst = self.list_input()
        num = self.inputer()
        reverse_idx = -1
        for i in range(len(lst)):
            if lst[i] == num:
                return i
            if lst[reverse_idx] == num:
                return reverse_idx + len(lst)
            reverse_idx -= 1

    def max_product(self):
        lst = self.list_input()
        max_num = 0
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                if lst[i] * lst[j] > max_num:
                    max_num = lst[i] * lst[j]
                    pair = [lst[i], lst[j]]
        return max_num, pair

    def is_duplicate(self):
        nums = self.list_input()
        if len(set(nums)) != len(nums):
            return True
        else:
            return False

    def permutation(self):
        n1 = self.list_input()
        n2 = self.list_input()
        if len(n1) != len(n2):
            return False
        n1.sort()
        n2.sort()
        return True if n1 == n2 else False

    @staticmethod
    def rotate_arr(matrix):
        print(matrix)
        n = len(matrix)
        for l in range(n // 2):
            first = l
            last = n - l - 1
            for i in range(first, last):
                top = matrix[l][i]
                matrix[l][i] = matrix[-i - 1][l]
                matrix[-i - 1][l] = matrix[-l - 1][-i - 1]
                matrix[-l - 1][-i - 1] = matrix[i][-l - 1]
                matrix[i][-l - 1] = top
        print(matrix)

    # def first_second(self):
    #     n = self.list_input()
    #     n.sort()
    #     while True:
    #         if n[-1] == n[-2]:
    #     return n[-1], n[-2]