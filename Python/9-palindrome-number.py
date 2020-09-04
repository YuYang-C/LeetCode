# https://leetcode.com/problems/palindrome-number/
import copy
import math


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        digits = 0
        foo = 1
        y = copy.deepcopy(x)
        while foo != 0:
            foo = y//10
            y =  y / 10
            digits += 1
        num_list = list()
        for i in range(digits, 0, -1):
            divisor = int('1'+'0'*(i-1))
            num_list.append(x//divisor)
            x = x % divisor
        for j in range(int(math.ceil(digits/2))):
            if num_list[j] != num_list[-(j+1)]:
                return False
        return True


if __name__ == '__main__':
    import sys
    num = int(sys.argv[1]) if len(sys.argv)==2 else 123454321
    if Solution().isPalindrome(num) is True:
        print(f'{num} is palindrome')
    else:
       print(f'{num} is not palindrome')
