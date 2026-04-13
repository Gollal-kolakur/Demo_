from typing import List

#1check for palindrome
class Solution1:
    def check_palindrome(self,string:str)->bool:
        reverse = string[::-1]
        if string == reverse:
            return True
        return False

ins1 = Solution1()
print(ins1.check_palindrome("Python"))

#2reverse sentence
class Solution2:
    def reverse_sentence(self,string:str)->str:
        break_arr = string.split()
        reverse = break_arr[::-1]
        result = " ".join(reverse)
        return result

ins2 = Solution2()
print(ins2.reverse_sentence("I Love Python"))

#3counting the vowels
class Solution3:
    def count_vowels(self,string:str)->int:
        vowels = "aeiouAEIOU"
        count = 0
        for ch in string:
            if ch in vowels:
                count += 1
        return count
ins3 = Solution3()
print(ins3.count_vowels("gk"))

#4find the factorial of the number
class Solution4:
    def factorial(self,n:int)->int:
        if n <0:
            return None
        fact = 1
        for num in range(1,n+1):
            fact *= num
        return fact
ins4 = Solution4()
print(ins4.factorial(5))

#5find the max_num
class Solution5:
    def max_num(self,arr:List[int])->int:
        max_num = arr[0]
        for num in arr:
            if num>max_num:
                max_num = num
        return max_num
ins5 = Solution5()
print(ins5.max_num([1,2,3,4,5,6]))

#6find the duplicates
class Solution6:
    def duplicate_num(self,arr:List[int])->List[int]:
        non_dupe = []
        dupe = []
        for num in arr:
            if num in non_dupe:
                dupe.append(num)
            else:
                non_dupe.append(num)
        return dupe
ins6 = Solution6()
print(ins6.duplicate_num([2,2,2,2,2]))

#7fibonacci number
class Solution7:
    def fibonnaci(self,n:int)->List[int]:
        fibonacci_series = [0,1]
        for num in range(2,n+1):
            fibonacci_series.append(fibonacci_series[num-1]+fibonacci_series[num-2])
        return fibonacci_series
ins7 = Solution7()
print(ins7.fibonnaci(9))

#8valid string or not
class Solution8:
    def valid_string(self,string:str)->bool:
        if len(string)<2:
            return False
        if not string.isalnum():
            return False
        return True
ins8 = Solution8()
print(ins8.valid_string("dh2"))

#9frequency of the characters as dictionaries
class Solution9:
    def frequency_ch(self,string:str)->dict[str:int]:
        frequency = {}
        for ch in string:
            if ch in frequency:
                frequency[ch] +=1
            else:
                frequency[ch] = 1
        return frequency
ins9 = Solution9()
print(ins9.frequency_ch("gollal"))


#10find the second highest number from array
class Solution10:
    def second_max(self,arr:List[int])->int:
        first = 0
        second = 0
        for num in arr:
            if num >first:
                second = first
                first = num
            elif num > second and num != first:
                second = num
        return second
ins10 = Solution10()
print(ins10.second_max([1,2,2,3]))

#11sum of xor of an array values
class Solution11:
    def sum_xor(self,arr:List[int])->int:
        n = len(arr)
        total = 0
        for i in range(n):
            xor = 0
            for j in range(i,n):
                xor ^= arr[j]
                total += xor
        return total
ins11 = Solution11()
print(ins11.sum_xor([1,2,3,4]))
#12sum of pair of 2 fixed dices
#13count the total number of subarrays non duplicates
class Solution13:
    def num_subarr(self,arr:List[int])->int:
        n = len(arr)
        sub_arrays = []
        for i in range(n):
            for j in range(i,n):
                sub = arr[i:j+1]
                if sub not in sub_arrays:
                    sub_arrays.append(sub)
        return len(sub_arrays)
ins13 = Solution13()
print(ins13.num_subarr([1,2,3,4,5]))

#14 swap the vowels of a string
class Solution14:
    def swap_vowel(self,string:str)->str:
        vowels = "aeiouAEIOU"
        string = list(string)
        left = 0
        right = len(string)-1
        while left<right:
            if string[left] not in vowels:
                left +=1
            if string[right] not in vowels:
                right -= 1
            else:
                string[left], string[right] = string[right], string[left]
                left +=1
                right -=1
        return "".join(string)
ins14 = Solution14()
print(ins14.swap_vowel("gollal"))

#15Find the sum of all subarrays
class Solution15:
    def sum_subarrays(self,arr:List[int])->int:
        n = len(arr)
        sum = 0
        for num in range(n):
            sub_arry_ind= 0
            for j in range(num,n):
                sub_arry_ind += arr[j]
                sum = sum+sub_arry_ind
        return sum
ins15 = Solution15()
print(ins15.sum_subarrays([1,2]))

#16Find the subarray with given sum k
class Solution16:
    def sum_equal(self,arr:List[int],k:int):
        n = len(arr)
        sub_array = []
        for i in range(n):
            sub_arra_count = 0
            for j in range(i,n):
                sub_arra_count += arr[j]
                if sub_arra_count == k:
                    sub_array.append((arr[i],arr[j]))
        return sub_array
ins16 = Solution16()
print(ins16.sum_equal([1,2],2))

#17First non-repeating character

#18Find missing number in array
class Solution18:
    def miss_num(self,arr:List[int], n:int)->int:
        expected_sum = n * (n+1)//2
        actual_sum = sum(arr)
        return expected_sum - actual_sum
ins18 = Solution18()
print(ins18.miss_num([1,2,4,5,6],6))
