31.
def func_a(arr):
    ret = arr + arr
    return ret

def func_b(first, second):
    MAX_NUMBER = 1001
    counter = [0 for _ in range(MAX_NUMBER)]
    for f, s in zip(first, second):
        counter[f] += 1
        counter[s] -= 1
    for c in counter:
        if c != 0:
            return False
    return True

def func_c(first, second):
    length = len(second)
    for i in range(length):
        if first[i : i + length] == second:
            return True
    return False

def solution(arrA, arrB):
    if len(arrA) != len(arrB):
        return False
    if func_@@@(@@@):
        arrA_temp = func_@@@(@@@)
        if func_@@@(@@@):
            return True
    return False

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 
arrA1 = [1, 2, 3, 4]
arrB1 = [3, 4, 1, 2]
ret1 = solution(arrA1, arrB1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

arrA2 = [1, 2, 3, 4]
arrB2 = [1, 4, 2, 3]
ret2 = solution(arrA2, arrB2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")

32.
def func_a(arr, s):
    return s in arr

def func_b(s):
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - i - 1]:
            return False
    return True

def func_c(palindromes, k):
    palindromes = sorted(palindromes)
    if len(palindromes) < k:
        return "NULL"
    else:
        return palindromes[k - 1]

def solution(s, k):
    palindromes = []
    length = len(s)
    for start_idx in range(length):
        for cnt in range(1, length - start_idx + 1):
            sub_s = s[start_idx : start_idx + cnt]
            if func_@@@(@@@) == True:
                if func_@@@(@@@) == False:
                    palindromes.append(sub_s)

    answer = func_@@@(@@@)
    return answer


#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
s1 = "abcba"
k1 = 4
ret1 = solution(s1, k1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

s2 = "ccddcc"
k2 = 7
ret2 = solution(s2, k2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")

33.
#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(bishops):
    #여기에 코드를 작성해주세요.
    answer = 0
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
bishops1 = ["D5"]
ret1 = solution(bishops1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

bishops2 = ["D5", "E8", "G2"]
ret2 = solution(bishops2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")

34.
# 다음과 같이 import를 사용할 수 있습니다.
# import math

def solution(s1, s2):
    # 여기에 코드를 작성해주세요.
    answer = 0
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
s1 = "ababc"
s2 = "abcdab"
ret = solution(s1, s2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

35.
# 다음과 같이 import를 사용할 수 있습니다.
# import math

def solution(phrases, second):
    # 여기에 코드를 작성해주세요.
    answer = ''
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
phrases = "happy-birthday"
second = 3
ret = solution(phrases, second)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
36.
def solution(n):
    answer = 0
    primes = [2]
    for i in range (3, n + 1, 2) :
        is_prime = True
        for j in range(2, i) :
            if i % j == 0 :
                is_prime = False
                break
        if @@@ :
            primes.append(i)

    prime_len = len(primes)
    for i in range(0, prime_len - 2) :
        for j in range(i + 1, prime_len - 1) :
            for k in range(j + 1, prime_len) :
                if @@@ :
                    answer += 1
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
n1 = 33
ret1 = solution(n1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

n2 = 9
ret2 = solution(n2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")
37.
def solution(k):
    answer = []
    for i in range(1, k + 1):
        square_num = i * i
        divisor = 1
        while square_num % divisor != 0:
            front = square_num // divisor
            back = square_num % divisor
            divisor *= 10
            if back != 0 and front != 0:
                if front + back == i:
                    answer.append(i)
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution 함수만 수정하세요.
k = 500
ret = solution(k)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")
38.
def solution(k, student):
    answer = 0
    for s in student:
        s -= 4*k
        if s <= 0:
            break
        answer += (s + k - 1) // k
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
k1 = 1
student1 = [4, 4, 4, 4]
ret1 = solution(k1, student1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

k2 = 3
student2 = [15, 17, 19, 10, 23]
ret2 = solution(k2, student2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")
39.
def solution(revenue, k) :
    answer = 0
    rsum = sum(revenue[0:k])
    answer = rsum
    for i in range(len(revenue)) :
        rsum = rsum - revenue[i - k] + revenue[i]
        if answer < rsum :
            answer = rsum
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
revenue1 = [1, 1, 9, 3, 7, 6, 5, 10]
k1 = 4
ret1 = solution(revenue1, k1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret1, " 입니다.")

revenue2 = [1, 1, 5, 1, 1]
k2 = 1
ret2 = solution(revenue2, k2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret2, " 입니다.")
30(0)
class Customer:
    def __init__(self, id, time, num_of_people):
        self.id = id
        self.time = time
        self.num_of_people = num_of_people

class Shop:
    def __init__(self):
        self.reserve_list = []
    
    def reserve(self, customer):
        self.reserve_list.append(customer)
        return True

class HairShop@@@:
    def __init__(self):
        super().__init__()
        
    @@@:
        if @@@ != 1:
            return False
        for r in self.reserve_list:
            if @@@:
                return False
        self.reserve_list.append(customer)
        return True
    
class Restaurant@@@:
    def __init__(self):
        super().__init__()
        
    @@@:
        if @@@:
            return False
        count = 0
        for r in self.reserve_list:
            if @@@:
                count += 1
        if count >= 2:
            return False
        self.reserve_list.append(customer)
        return True
    

def solution(customers, shops):
    hairshop = HairShop()
    restaurant = Restaurant()
    
    count = 0
    for customer, shop in zip(customers, shops):
        if shop == "hairshop":
            if hairshop.reserve(Customer(customer[0], customer[1], customer[2])):
                count += 1
        elif shop == "restaurant":
            if restaurant.reserve(Customer(customer[0], customer[1], customer[2])):
                count += 1
    
    return count

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
customers = [[1000, 2, 1],[2000, 2, 4],[1234, 5, 1],[4321, 2, 1],[1111, 3, 10]]
shops = ["hairshop", "restaurant", "hairshop", "hairshop", "restaurant"]
ret = solution(customers, shops)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
41.
words = []

def create_words(lev, s):
    global words
    VOWELS = ['A', 'E', 'I', 'O', 'U']
    words.append(s)
    for i in range(0, 5):
        if lev < 5:
            create_words(lev, s + VOWELS[i])

def solution(word):
    global words
    words = []
    answer = 0
    create_words(0, '')
    for idx, i in enumerate(words):
        if word == i:
            answer = idx
            break
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니, 위의 코드만 수정하세요.
word1 = "AAAAE"
ret1 = solution(word1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret1, " 입니다.")

word2 = "AAAE"
ret2 = solution(word2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret2, " 입니다.")
42.
def solution(s):
    s = s.lower()
    answer = ""
    previous = s[0]
    counter = 1
    for alphabet in s[1:]:
        if alphabet == previous:
            counter += 1
        else:
            answer += previous + str(counter)
            counter = 1
            previous = s[0]
    answer += previous + str(counter)
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니, 위의 코드만 수정하세요.
s = "YYYYYbbbBbbBBBMmmM"
ret = solution(s)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
43.
def solution(one_day_price, multi_day, multi_day_price, n):
    if one_day_price * multi_day <= multi_day_price:
        return n * one_day_price
    else:
        return (n % multi_day) * multi_day_price + (n // multi_day) * one_day_price
        
# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니, 위의 코드만 수정하세요.
one_day_price1 = 3
multi_day1 = 5
multi_day_price1 = 14
n1 = 6
ret1 = solution(one_day_price1, multi_day1, multi_day_price1, n1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

one_day_price2 = 2
multi_day2 = 3
multi_day_price2 = 5
n2 = 11
ret2 = solution(one_day_price2, multi_day2, multi_day_price2, n2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")
44.
def func_a(matrix):
    n = 4
    ret = []
    exist = [False for _ in range(n*n + 1)]
    for i in range(0, n):
        for j in range(0, n):
                exist[matrix[i][j]] = True
    for i in range(1, n*n+1):
        if exist[i] == False:
            ret.append(i)
    return ret

def func_b(matrix):
    n = 4
    ret = []
    for i in range(0, n):
        for j in range(0, n):
            if matrix[i][j] == 0:
                ret.append([i, j])
    return ret

def func_c(matrix):
    n = 4
    goal_sum = sum(range(1, n*n+1))//n
    for i in range(0, n):
        row_sum = 0
        col_sum = 0
        for j in range(0, n):
            row_sum += matrix[i][j]
            col_sum += matrix[j][i]
        if row_sum != goal_sum or col_sum != goal_sum:
            return False

    main_diagonal_sum = 0
    skew_diagonal_sum = 0
    for i in range(0, n):
        main_diagonal_sum += matrix[i][i]
        skew_diagonal_sum += matrix[i][n-1-i]
    if main_diagonal_sum != goal_sum or skew_diagonal_sum != goal_sum:
        return False
    return True

def solution(matrix):
    answer = []
    coords = func_@@@(@@@)
    nums = func_@@@(@@@)

    matrix[coords[0][0]][coords[0][1]] = nums[0]
    matrix[coords[1][0]][coords[1][1]] = nums[1]
    if func_@@@(@@@):
        for i in range(0, 2):
            answer.append(coords[i][0] + 1)
            answer.append(coords[i][1] + 1)
            answer.append(nums[i])
    else:
        matrix[coords[0][0]][coords[0][1]] = nums[1]
        matrix[coords[1][0]][coords[1][1]] = nums[0]
        for i in range(0, 2):
            answer.append(coords[1-i][0] + 1)
            answer.append(coords[1-i][1] + 1)
            answer.append(nums[i])
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
matrix = [[16,2,3,13],[5,11,10,0],[9,7,6,12],[0,14,15,1]]
ret = solution(matrix)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")
45.
def solution(n):
    answer = ''
    for i in range(n):
        answer += str(@@@)
        answer = answer[@@@]
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
n = 5
ret = solution(n)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
46.
def power(base, exponent):
    val = 1
    for i in range(exponent):
        val *= base
    return val

def solution(k):
    answer = []
    bound = power(10, k)
    for i in range(bound // 10, bound):
        current = i
        calculated = 0
        while current != 0:
            @@@
            @@@
        if calculated == i:
            answer.append(i)
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
k = 3
ret = solution(k)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
47.
class Unit:
    def __init__(self):
        self.HP = 1000
    def under_attack(self, damage):
        pass

class Monster@@@:
    def __init__(self, attack_point):
        super().__init__()
        self.attack_point = attack_point
    @@@:
        self.HP -= damage
    @@@:
        return self.attack_point

class Warrior@@@:
    def __init__(self, attack_point):
        super().__init__()
        self.attack_point = attack_point
    @@@:
        self.HP -= damage
    @@@:
        return self.attack_point

class Healer@@@:
    def __init__(self, healing_point):
        super().__init__()
        self.healing_point = healing_point
    @@@:
        self.HP -= damage
    @@@:
        unit.HP += self.healing_point


def solution(monster_attack_point, warrior_attack_point, healing_point):
    monster = Monster(monster_attack_point)
    warrior = Warrior(warrior_attack_point)
    healer = Healer(healing_point)

    # 전사가 몬스터를 한 번 공격
    monster.under_attack(warrior.attack())
    # 몬스터가 전사를 한 번 공격
    warrior.under_attack(monster.attack())
    # 몬스터가 힐러를 한 번 공격
    healer.under_attack(monster.attack())
    # 힐러가 전사의 체력을 한 번 회복
    healer.healing(warrior)
    # 힐러가 몬스터의 체력을 한 번 회복
    healer.healing(monster)

    answer = [monster.HP, warrior.HP, healer.HP]
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
monster_attack_point = 100
warrior_attack_point = 90
healing_point = 30
ret = solution(monster_attack_point, warrior_attack_point, healing_point)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
48.
# 다음과 같이 import를 사용할 수 있습니다.
# import math

def solution(card, n):
    # 여기에 코드를 작성해주세요.
    answer = 0
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
card1 = [1, 2, 1, 3]
n1 = 1312
ret1 = solution(card1, n1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret1, " 입니다.")

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
card2 = [1, 1, 1, 2]
n2 = 1122
ret2 = solution(card2, n2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret2, " 입니다.")
49.
# 다음과 같이 import를 사용할 수 있습니다.
# import math

def solution(hour, minute):
    answer = ''
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
hour = 3
minute = 0
ret = solution(hour, minute)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")
40(0)
#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(a, b):
    # 여기에 코드를 작성해주세요.
    answer = 0
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
a =  6
b =  30
ret = solution(a, b)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
51.
def solution(n):
	answer = 0
	steps = [0 for _ in range(n+1)]
	steps[1] = 1
	steps[2] = 2
	steps[3] = 4
	for i in range(4, n+1):
		steps[i] = @@@
	answer = steps[n]
	return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
n1 = 3
ret1 = solution(n1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

n2 = 4
ret2 = solution(n2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")
52.
def solution(walls):
    answer = 0
    for i in range(len(walls)):
    	for j in range(i+1, len(walls)):
    		area = 0
    		if walls[i][1] > walls[j][1]:
    			area = walls[i][1] * (walls[j][0] - walls[i][0])
    		else:
    			area = walls[j][1] * (walls[j][0] - walls[i][0])
    		if answer < area:
    			answer = area
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니, 위의 코드만 수정하세요.
walls = [[1, 4], [2, 6], [3, 5], [5, 3], [6, 2]]
ret = solution(walls)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
53.
def solution(numbers):
    answer = []
    numbers.sort()
    mid = (len(numbers) - 1) // 2
    numbers[mid], numbers[len(numbers)-1] = numbers[len(numbers)-1], numbers[mid]
    left = mid + 1
    right = len(numbers) - 1
    while left <= right:
    	numbers[left], numbers[right] = numbers[right], numbers[left]
    	left = left + 1
    	right = right - 1
    answer = numbers
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니 위의 코드만 수정하세요.
numbers = [7, 3, 4, 1, 2, 5, 6]
ret = solution(numbers)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
54.
def solution(number):
    answer = ''
    number_count = [0 for _ in range(10)]
    while number > 0:
        number_count[number % 10] += 1
        number //= 10
    for i in range(10):
        if number_count[i] != 0:
            answer += (str(i) + str(number_count[i]))
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니, 위의 코드만 수정하세요.
number1 = 2433
ret1 = solution(number1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

number2 = 662244
ret2 = solution(number2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")
55.
#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(enemies, armies):
    #여기에 코드를 작성해주세요.
    answer = 0
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
enemies1 = [1, 4, 3]
armies1 = [1, 3]
ret1 = solution(enemies1, armies1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

enemies2 = [1, 1, 1]
armies2 = [1, 2, 3, 4]
ret2 = solution(enemies2, armies2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")
56.
#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(s1, s2, p, q):
    #여기에 코드를 작성해주세요.
    answer = ''
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
s1 = "112001"
s2 = "12010"
p = 3
q = 8
ret = solution(s1, s2, p, q)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
57.
def find(parent, u):
    if u == parent[u]:
        return u
    parent[u] = @@@
    return parent[u]

def merge(parent, u, v):
    u = find(parent, u)
    v = find(parent, v)
    if u == v:
        return True
    @@@
    return False

def solution(n, connections):
    answer = 0
    parent = @@@
    for i, connection in enumerate(connections):
        if merge(parent, connection[0], connection[1]):
            answer = i + 1
            break
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
n = 3
connections = [[1, 2], [1, 3], [2, 3]]
ret = solution(n, connections)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
58.
def func_a(a, b):
	mod = a % b
	while mod > 0:
		a = b
		b = mod
		mod = a % b
	return b

def func_b(n):
	answer = 0
	for i in range(1, n+1):
		if func_@@@(@@@):
			answer += 1
	return answer

def func_c(p, q):
	if p % q == 0:
		return True
	else:
		return False

def solution(a, b, c):
    answer = 0
    gcd = func_@@@(func_@@@(@@@)@@@)
    answer = func_@@@(@@@)
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
a = 24
b = 9
c = 15
ret = solution(a, b, c)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
59.
#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(number, target):
    #여기에 코드를 작성해주세요.
    answer = 0
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
number1 = 5
target1 = 9
ret1 = solution(number1, target1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

number2 = 3
target2 = 11
ret2 = solution(number2, target2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")
50(0)
class Job:
	def __init__(self):
		self.salary = 0
	
	def get_salary(self):
		return salary

class PartTimeJob@@@:
	def __init__(self, work_hour, pay_per_hour):
		super().__init__()
		self.work_hour = work_hour
		self.pay_per_hour = pay_per_hour
	
	@@@:
		self.salary = self.work_hour * self.pay_per_hour
		if self.work_hour >= 40:
			self.salary += (self.pay_per_hour * 8)
		return self.salary

class SalesJob@@@:
	def __init__(self, sales_result, pay_per_sale):
		super().__init__()
		self.sales_result = sales_result
		self.pay_per_sale = pay_per_sale

	@@@:
		if self.sales_result > 20:
			self.salary = self.sales_result * self.pay_per_sale * 3
		elif self.sales_result > 10:
			self.salary = self.sales_result * self.pay_per_sale * 2
		else:
			self.salary = self.sales_result * self.pay_per_sale
		return self.salary

def solution(part_time_jobs, sales_jobs):
	answer = 0
	for p in part_time_jobs:
		part_time_job = PartTimeJob(p[0], p[1])
		answer += part_time_job.get_salary()
	for s in sales_jobs:
		sale_job = SalesJob(s[0], s[1])
		answer += sale_job.get_salary()
	return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
part_time_jobs = [[10, 5000], [43, 6800], [5, 12800]]
sales_jobs = [[3, 18000], [12, 8500]]
ret = solution(part_time_jobs, sales_jobs)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
61.
#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(n, garden):
    #여기에 코드를 작성해주세요.
    answer = 0
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
n1 = 3
garden1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
ret1 = solution(n1, garden1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

n2 = 2
garden2 = [[1, 1], [1, 1]]
ret2 = solution(n2, garden2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")
62.
#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(K, words):
    #여기에 코드를 작성해주세요.
    answer = 0
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
K = 10
words = ["nice", "happy", "hello", "world", "hi"]
ret = solution(10, words)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
63.
#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(arr, K):
    #여기에 코드를 작성해주세요.
    answer = 0
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [9, 11, 9, 6, 4, 19]
K = 4
ret = solution(arr, K)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
64.
def solution(n, mix, k):
    answer = 0
    card = [_ for _ in range(1, n+1)]
    while mix != 0:
        mix = mix - 1
        card_a, card_b = [0 for _ in range(n//2)], [0 for _ in range(n//2)]
        for i in range(0, n):
            if i < n//2:
                card_a[i] = card[i]
            else:
                card_b[i] = card[i]
        for i in range(0, n):
            if i % 2 == 0:
                card[i] = card_a[i//2]
            else:
                card[i] = card_b[i//2]
    answer = card[k-1]
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니 위의 코드만 수정하세요.
n = 6
mix = 3
k = 3
ret = solution(n, mix, k)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
65.
def solution(board):
    coins = [[0 for c in range(4)] for r in range(4)]
    for i in range(4):
        for j in range(4):
            if i == 0 and j == 0:
                coins[i][j] = board[i][j]
            elif i == 0 and j != 0:
                coins[i][j] = board[i][j] + coins[i][j-1]
            elif i != 0 and j == 0:
                coins[i][j] = board[i][j] + coins[i-1][j]
            else:
                coins[i][j] = board[i][j] + max(coins[i][j], coins[i-1][j-1])
    answer = coins[3][3]
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으면 위의 코드만 수정하세요.
board = [[6, 7, 1, 2], [3, 5, 3, 9], [6, 4, 5, 2], [7, 3, 2, 6]]
ret = solution(board)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
66.
def solution(grid):
    answer = 0
    for i in range(4):
        for j in range(4):
            for k in range(j + 1, 4, 2):
                answer = max(answer, max(grid[i][j] + grid[j][k], grid[j][k] + grid[k][i]))
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니 위의 코드만 수정하세요.
grid = [[1, 4, 16, 1], [20, 5, 15, 8], [6, 13, 36, 14], [20, 7, 19, 15]]
ret = solution(grid)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
67.
def solution(K, numbers, up_down):
    left = 1
    right = K
    for num, word in zip(numbers, up_down):
        if word == "UP":
            left = @@@
        elif word == "DOWN":
            right = @@@
        elif word == "RIGHT":
            return 1
    return @@@

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
K1 = 10
numbers1 = [4, 9, 6]
up_down1 = ["UP", "DOWN", "UP"]
ret1 = solution(K1, numbers1, up_down1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

K2 = 10
numbers2 = [2, 1, 6]
up_down2 = ["UP", "UP", "DOWN"]
ret2 = solution(K2, numbers2, up_down2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")

K3 = 100
numbers3 = [97, 98]
up_down3 = ["UP", "RIGHT"]
ret3 = solution(K3, numbers3, up_down3)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret3, "입니다.")
68.
INC = 0
DEC = 1

def func_a(arr):
    length = len(arr)
    ret = [0 for _ in range(length)]
    ret[0] = 1
    for i in range(1, length):
        if arr[i] != arr[i-1]:
            ret[i] = ret[i-1] + 1
        else:
            ret[i] = 2
    return ret

def func_b(arr):
    global INC, DEC
    length = len(arr)
    ret = [0 for _ in range(length)]
    ret[0] = -1
    for i in range(1, length):
        if arr[i] > arr[i-1]:
            ret[i] = INC
        elif arr[i] < arr[i-1]:
            ret[i] = DEC
    return ret

def func_c(arr):
    ret = max(arr)
    if ret == 2:
        return 0
    return ret

def solution(S):
    check = func_@@@(@@@)
    dp = func_@@@(@@@)
    answer = func_@@@(@@@)
    return answer


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
S1 = [2, 5, 7, 3, 4, 6, 1, 8, 9]
ret1 = solution(S1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

S2 = [4, 3, 2, 1, 10, 6, 9, 7, 8]
ret2 = solution(S2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")

S3 = [1, 2, 3, 4, 5]
ret3 = solution(S3)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret3, "입니다.")
69.
def func_a(stack):
    return stack.pop()

def func_b(stack1, stack2):
    while not func_@@@(@@@):
        item = func_@@@(@@@)
        stack2.append(item)

def func_c(stack):
    return (len(stack) == 0)

def solution(stack1, stack2):
    if func_@@@(@@@):
        func_@@@(@@@)

    answer = func_@@@(@@@)
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
stack1_1 = [1,2]
stack2_1 = [3,4]
ret1 = solution(stack1_1, stack2_1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

stack1_2 = [1,2,3]
stack2_2 = []
ret2 = solution(stack1_2, stack2_2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")
60(0)
class Job:
	def __init__(self):
		self.salary = 0
	
	def get_salary(self):
		return salary

class PartTimeJob@@@:
	def __init__(self, work_hour, pay_per_hour):
		super().__init__()
		self.work_hour = work_hour
		self.pay_per_hour = pay_per_hour
	
	@@@:
		self.salary = self.work_hour * self.pay_per_hour
		if self.work_hour >= 40:
			self.salary += (self.pay_per_hour * 8)
		return self.salary

class SalesJob@@@:
	def __init__(self, sales_result, pay_per_sale):
		super().__init__()
		self.sales_result = sales_result
		self.pay_per_sale = pay_per_sale

	@@@:
		if self.sales_result > 20:
			self.salary = self.sales_result * self.pay_per_sale * 3
		elif self.sales_result > 10:
			self.salary = self.sales_result * self.pay_per_sale * 2
		else:
			self.salary = self.sales_result * self.pay_per_sale
		return self.salary

def solution(part_time_jobs, sales_jobs):
	answer = 0
	for p in part_time_jobs:
		part_time_job = PartTimeJob(p[0], p[1])
		answer += part_time_job.get_salary()
	for s in sales_jobs:
		sale_job = SalesJob(s[0], s[1])
		answer += sale_job.get_salary()
	return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
part_time_jobs = [[10, 5000], [43, 6800], [5, 12800]]
sales_jobs = [[3, 18000], [12, 8500]]
ret = solution(part_time_jobs, sales_jobs)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")