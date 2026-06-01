from typing import List
#check for palindrome
class Solution1:
    def palindrome(self,string:str)->bool:
        reverse = string[::-1]
        if string == reverse:
            return True
        return False

obj1 = Solution1()
print(obj1.palindrome("gollal"))

#reverse sentence
class Solution2:
    def reverse_sentence(self,string:str)->str:
        string_array = string.split()
        reverse = string_array[::-1]
        result = " ".join(reverse)
        return result
obj2 = Solution2()
print(obj2.reverse_sentence("I love python"))

#counting the vowels
class Solution3:
    def count_vowels(self,string:str)->int:
        vowels = "aeiouAEIOU"
        count = 0
        for ch in string:
            if ch in vowels:
                count +=1
        return count
obj3 = Solution3()
print(obj3.count_vowels("gollal"))

#find the factorial of the number
class Solution4:
    def factorial(self,n:int)->int:
        if n < 0:
            return None
        fact = 1
        for num in range(1,n+1):
            fact *= num
        return fact

obj4 = Solution4()
print(obj4.factorial(0))

#find the max_num
class Solution5:
    def max_num(self,arr:List[int])->int:
        max_num = arr[0]
        for num in arr:
            if num > max_num:
                max_num = num
        return max_num
obj5 = Solution5()
print(obj5.max_num([1,2,3,4,5]))

#6find the duplicates
class Solution6:
    def find_duplicates(self,arr:List[int])->int:
        original_value = set()
        dupes = set()
        for num in arr:
            if num in original_value:
                dupes.add(num)
            else:
                original_value.add(num)
        return len(list(dupes))
obj6 = Solution6()
print(obj6.find_duplicates([1,2,3,4,4]))

#7fibonacci number
class Solution7:
    def fibonacci_number(self,n:int)->int:
        fibonacci_series = [0,1]
        for num in range(2,n):
            fibonacci_series.append(fibonacci_series[num-1]+fibonacci_series[num-2])
        return fibonacci_series

obj7 = Solution7()
print(obj7.fibonacci_number(7))

#8valid string or not
class Solution8:
    def check_string(self,string:str)->bool:
        if len(string) < 2:
            return False
        if not string.isalnum():
            return False
        return True
obj8 = Solution8()
print(obj8.check_string("gollal1234"))

#9frequency of the characters as dictionaries
class Solution9:
    def frequency_string(self,string:str)->dict[str,int]:
        frequency = {}
        for ch in string:
            if ch in frequency:
                frequency[ch] += 1
            frequency[ch] = 1
        return frequency
obj9 = Solution9()
print(obj9.frequency_string("gollal"))

#10find the second highest number from array
class Solution10:
    def second_max(self,arr:List[int])->int:
        first = 0
        second = 0
        for num in arr:
            if num >first:
                second = first
                first = num
            elif num >second and num != first:
                second = num
        return second

obj10 = Solution10()
print(obj10.second_max([1,2,3,4]))

#11sum of xor of an array values
class Solution11:
    def sum_XOR(self,arr:List[int])->int:
        n = len(arr)
        total = 0
        for i in range(n):
            xor = 0
            for j in range(i,n):
                xor ^= arr[j]
                total +=xor
        return total
obj11 = Solution11()
print(obj11.sum_XOR([1,2,3,4,5]))

#13count the total number of subarrays non duplicates
class Solution13:
    def num_sub_arrays(self,arr:List[int])->int:
        n = len(arr)
        sub_arrays= []
        for i in range(n):
            for j in range(i,n):
                sub = arr[i:j+1]
                if sub not in sub_arrays:
                    sub_arrays.append(sub)
        return len(sub_arrays)
obj13 = Solution13()
print(obj13.num_sub_arrays([1,2,3,4,5]))

#14 swap the vowels of a string
class Solution14:
    def swap_vowels(self,string:str)->str:
        n = len(string)
        string = list(string)
        vowels = "aeiouAEIOU"
        left = 0
        right = n-1
        while left < right:
            if string[left] not in vowels:
                left += 1
            elif string[right] not in vowels:
                right -= 1
            else:
                string[left], string[right] =string[right],string[left]
                left += 1
                right -= 1

        return ''.join(string)
obj14 = Solution14()
print(obj14.swap_vowels("gollal"))

#15Find the sum of all subarrays
class Solution15:
    def sum_sub_arrays(self, arr: List[int]) -> int:
        n = len(arr)
        total = 0
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += arr[j]
                print(f"Subarray ({i},{j}) sum = {current_sum}")
                total += current_sum
        print("FINAL TOTAL:", total)
        return total

obj15 = Solution15()
print(obj15.sum_sub_arrays([1,2,3,4,5]))

#16Find the subarray with given sum k
class Solution16:
    def sub_arrays_const(self, arr: List[int],k:int) -> int:
        n = len(arr)
        outcome = []
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += arr[j]
                print(f"Subarray ({i},{j}) sum = {current_sum}")
                if current_sum == k:
                    outcome.append((arr[i:j+1]))
        return outcome

obj16 = Solution16()
print(obj16.sub_arrays_const([1,2,3,4,5],3))

#17First non-repeating character

#18Find missing number in array
class Solution18:
    def missing_number(self, arr: List[int], n: int):
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(arr)
        return expected_sum - actual_sum

obj18 = Solution18()
print(obj18.missing_number([1,2,4,5], 5))




















































