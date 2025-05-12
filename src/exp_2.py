"""
实验三 Python程序控制结构
实验目的：
   1. 掌握Python选择结构和循环结构及其语法格式
   2. 掌握break和continue的使用方法,推导式的使用方法
学号: 2422040116
姓名：李潞
"""

# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
count = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and i != k and j != k:
                count += 1
                print(i * 100 + j * 10 + k, end=" ")
print(f"\n总共有{count}个互不相同且无重复数字的三位数")

# 使用for循环打印1~100之间所有的偶数
print("\n1~100之间的偶数：")
for num in range(2, 101, 2):
    print(num, end=" ")

# 输入三角形三边长度，判断能否构成三角形
print("\n\n判断能否构成三角形")
a = float(input("请输入三角形的第一边长："))
b = float(input("请输入三角形的第二边长："))
c = float(input("请输入三角形的第三边长："))
if a + b > c and a + c > b and b + c > a:
    print("可以构成三角形")
else:
    print("不能构成三角形")

# 输入一个整数，判断它是否在[10, 100]之间
print("\n判断整数是否在[10, 100]之间")
num = int(input("请输入一个整数："))
if 10 <= num <= 100:
    print("该整数在[10, 100]之间")
else:
    print("该整数不在[10, 100]之间")

# 输入成绩，输出对应等级（90以上A，80-89B，70-79C，60-69D，60以下E）
print("\n根据成绩输出等级")
score = int(input("请输入成绩："))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("E")

# 输出 9*9 乘法口诀表，分行与列考虑，共9行9列，i控制行，j控制列
print("\n9*9乘法口诀表：")
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}×{i}={i * j}", end=" ")
    print()

# 判断101-200之间有多少个素数，并输出所有素数
print("\n101-200之间的素数：")
prime_count = 0
for num in range(101, 201):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_count += 1
        print(num, end=" ")
print(f"\n101-200之间有{prime_count}个素数")

# 一只公鸡值5元，一只母鸡值3元，而1元可买3只小鸡。现有100元钱，要求把钱花完正好买到100只鸡。请问可买公鸡、母鸡、小鸡各几只？
print("\n公鸡、母鸡、小鸡的购买方案：")
for x in range(20):  # 公鸡数量
    for y in range(33):  # 母鸡数量
        z = 100 - x - y  # 小鸡数量
        if 5 * x + 3 * y + z / 3 == 100:
            print(f"公鸡{x}只，母鸡{y}只，小鸡{z}只")

# 打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
print("\n水仙花数：")
for num in range(100, 1000):
    hundreds = num // 100
    tens = (num % 100) // 10
    ones = num % 10
    if hundreds**3 + tens**3 + ones**3 == num:
        print(num, end=" ")

# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
print("\n\n小球落地问题")
height = 100
total_distance = 0
for i in range(10):
    total_distance += height
    height /= 2
    if i != 9:
        total_distance += height
print(f"第10次落地时，共经过{total_distance}米，第10次反弹高度为{height}米")

# 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
print("\n分数序列前20项之和")
a, b = 2, 1
sum_series = 0
for _ in range(20):
    sum_series += a / b
    a, b = a + b, a
print(f"前20项之和为{sum_series}")

# 给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
print("\n正整数位数及逆序打印")
num = int(input("请输入一个不多于5位的正整数："))
digits = []
while num > 0:
    digits.append(num % 10)
    num //= 10
print(f"该数是{len(digits)}位数，逆序打印为：{''.join(map(str, digits))}")

# 输入一个整数，判断它是否是回文数（如121, 1331）
print("\n判断是否为回文数")
num = int(input("请输入一个整数："))
str_num = str(num)
if str_num == str_num[::-1]:
    print("该数是回文数")
else:
    print("该数不是回文数")

# 输入一个年份，判断它是否为闰年，（闰年规则：能被4整除但不能被100整除，或能被400整除）
print("\n判断是否为闰年")
year = int(input("请输入一个年份："))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("该年是闰年")
else:
    print("该年不是闰年")

# 使用推导式从列表[-5, 3, 0, -2, 9, 7]中筛选出所有非负数
print("\n筛选非负数")
numbers = [-5, 3, 0, -2, 9, 7]
non_negative_numbers = [num for num in numbers if num >= 0]
print(non_negative_numbers)

# 使用推导式将字符串列表words = ["apple", "banana", "cherry"]中的所有单词转为大写
print("\n单词转大写")
words = ["apple", "banana", "cherry"]
uppercase_words = [word.upper() for word in words]
print(uppercase_words)

# 编写程序，找出前 N 个既是质数又是回文数的整数（例如 2, 3, 5, 7, 11, 101...）
print("\n前N个既是质数又是回文数的整数")


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_palindrome(n):
    return str(n) == str(n)[::-1]


n = int(input("请输入N的值："))
count = 0
num = 2
prime_palindromes = []
while count < n:
    if is_prime(num) and is_palindrome(num):
        prime_palindromes.append(num)
        count += 1
    num += 1
print(prime_palindromes)

# 计算n为10时，1 + 11 + 111 + 1111 + ... + 第 n 项 的值
print("\n计算特定序列的和")
n = 10
sum_sequence = 0
term = 0
for i in range(1, n + 1):
    term = term * 10 + 1
    sum_sequence += term
print(f"当n为10时，序列的和为{sum_sequence}")
