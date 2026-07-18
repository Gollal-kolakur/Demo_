from typing import List
import os

#1check for palindrome for interview
class Solution1:

    def __init__(self,word):
        self.word = word

    def palindrome_check(self)->bool:
        reverse = self.word[::-1]
        if reverse == self.word:
            return True
        return False
obj1 = Solution1("madam")
print(obj1.palindrome_check())


#2reverse sentence
class Solution2:
    def __init__(self,string):
        self.string = string
    def reverse_sentence(self):
        break_arr = self.string.split()
        reverse = break_arr[::-1]
        result = " ".join(reverse)
        return result

ins2 = Solution2("I Love Python")
print(ins2.reverse_sentence())

#3counting the vowels
class Solution3:
    def __init__(self,string):
        self.string = string

    def count_vowels(self):
        vowels = "aeiouAEIOU"
        count = 0
        for ch in self.string:
            if ch in vowels:
                count +=1
        return count
ins2 = Solution3("gollal")
print(ins2.count_vowels())



#4find the factorial of the number
class Solution4:
    def __init__(self,n):
        self.n = n

    def factorial(self):
        if self.n<0:
            return None
        fact = 1
        for num in range(1,self.n+1):
            fact *=num
        return fact
ins4 = Solution4(7)
print(ins4.factorial())

#5find the max_num
class Solution5:
    def __init__(self,arr:List[int]):
        self.abc = arr

    def max_num(self):
        first_num = self.abc[0]
        max_num = 0
        for num in self.abc:
            if num>max_num:
                max_num = num
        return max_num

ins5 = Solution5([1,2,3,4,5])
print(ins5.max_num())

#6find the duplicates
class Solution6:
    def __init__(self,arr:List[int]):
        self.arr = arr

    def duplicate_num(self):
        non_dupes = set()
        dupes = []
        for num in self.arr:
            if num in non_dupes:
                dupes.append(num)
            else:
                non_dupes.add(num)
        return dupes

ins6 = Solution6([2,2,2,2,2])
print(ins6.duplicate_num())

#7fibonacci number
class Solution7:

    def __init__(self,num):
        self.num = num

    def fibonnaci(self):
        fibonacci_series = [0,1]
        for num in range (2, self.num+1):
            fibonacci_series.append(fibonacci_series[num-1]+fibonacci_series[num-2])
        return fibonacci_series

ins7 = Solution7(9)
print(ins7.fibonnaci())

#8valid string or not
class Solution8:
    def __init__(self,string):
        self.string = string

    def valid_string(self):
        if len(self.string) <2:
            return False
        if not self.string.isalnum():
            return False
        return True

ins8 = Solution8("dh2")
print(ins8.valid_string())

#9frequency of the characters as dictionaries
class Solution9:
    def __init__(self,string):
        self.string = string
    def frequency_ch(self):
        frequency = {}
        for ch in self.string:
            if ch in frequency:
                frequency[ch] +=1
            else:
                frequency[ch] = 1
        return frequency

ins9 = Solution9("gollal")
print(ins9.frequency_ch())


#10find the second highest number from array
class Solution10:
    def __init__(self,arr:List):
        self.arr = arr
    def second_max(self):
        first = 0
        second = 0
        for i in self.arr:
            if i > first:
                second = first
                first = i
            elif i>second and  i != first:
                second = i
        return second

ins10 = Solution10([1,2,3,4])
print(ins10.second_max())

#11sum of xor of an array values
class Solution11:
    def __init__(self,arr:List[int]):
        self.arr = arr

    def sum_xor(self):
        n = len(self.arr)
        sum = 0
        for i in range(n):
            count_num = 0
            for j in range(i,n):
                count_num +=self.arr[j]
                sum += count_num
        return sum

ins11 = Solution11([1,2,3,4])
print(ins11.sum_xor())

#12sum of pair of 2 fixed dices


#13count the total number of subarrays non duplicates
class Solution13:
    def __init__(self,arr):
        self.arr = arr

    def num_sub_arr(self):
        n = len(self.arr)
        outcome = []
        for i in range(n):
            for j in range(i,n):
                outcome.append(self.arr[i:j+1])
        return len(outcome)

ins13 = Solution13([1,2,3,4,5])
print(ins13.num_sub_arr())

#14 swap the vowels of a string
class Solution14:
    def __init__(self,string):
        self.string = string

    def swap_vowel(self):
        vowels = "aeiouAEIOU"
        str = list(self.string)
        left = 0
        right = len(self.string)-1
        while left<right:
            if str[left] not in vowels:
                left +=1
            if str[right] not in vowels:
                right -=1
            else:
                str[left] , str[right] = str[right], str[left]
                left += 1
                right += 1
        return "".join(str)

ins14 = Solution14("gollal")
print(ins14.swap_vowel())

#15Find the sum of all subarrays
class Solution15:
    def __init__(self,arr:List[int]):
        self.arr = arr

    def sum_subarrays(self):
        n = len(self.arr)
        total = 0
        for i in range(n):
            count_num = 0
            for j in range(i,n):
                count_num = self.arr[j]
                total += count_num

        return total
ins15 = Solution15([1,2])
print(ins15.sum_subarrays())

#16Find the subarray with given sum k
class Solution16:
    def sum_equal(self,arr:List[int],k:int):
        pass

ins16 = Solution16()
print(ins16.sum_equal([1,2],2))

#17First non-repeating character

#18Find missing number in array
class Solution18:
    def __init__(self,arr):
        self.arr = arr

    def miss_num(self,n):
        expected_num = n*(n+1)//2
        actual_sum = sum(self.arr)
        return expected_num - actual_sum

ins18 = Solution18([1,2,4,5,6])
print(ins18.miss_num(6))




