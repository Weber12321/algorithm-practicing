class Solution(object):
    @staticmethod
    def inputer() -> int:
        while True:
            try:
                _num = int(input("input a number: "))
                if _num < 0:
                    print(f'integer must be positive, plz re-input!')
                    continue
                else:
                    break
            except ValueError:
                print(f'number must be integer, plz re-input!')
                continue
        return _num

    def factorial(self, num: int) -> int:
        if num <= 1:
            return num
        else:
            return num * self.factorial(num - 1)

    def fibonacci(self, num: int) -> int:
        if num == 0 or num == 1:
            return num
        else:
            return self.fibonacci(num - 1) + self.fibonacci(num - 2)

    def sum_of_digits(self, num: int) -> int:
        if num / 10 < 1:
            return num
        else:
            return num % 10 + self.sum_of_digits(num // 10)

    def power_of_number(self, num: int, exp: int) -> int:
        if exp == 0:
            return 1
        elif exp == 1:
            return num
        else:
            return num * self.power_of_number(num, exp - 1)

    def greatest_common_divisor(self, num_1: int, num_2: int) -> int:
        """
        input a,b
        if b == 0:
        do return a
        else:
        do gcd(b, a mod b)
        """
        if num_2 == 0:
            return num_1
        else:
            return self.greatest_common_divisor(num_2, num_1 % num_2)

    def decimal_to_binary(self, num: int):
        """
        n mod 2 + 10 * f(n/2)
        """
        if num // 2 == 0:
            return 1
        else:
            return num % 2 + 10 * self.decimal_to_binary(num//2)


if __name__ == '__main__':
    s = Solution()
    # print(s.greatest_common_divisor(s.inputer(), s.inputer()))
    print(s.decimal_to_binary(s.inputer()))