"""
实验二 Python基本数据类型
  实验目的：
  1、  熟悉Python基本数据类型
  2、  掌握Python数据类型转换、运算符与表达式
"""

# 实验内容：
# 1、计算2的100次方，并观察是否溢出。
result1 = 2**100
print(f"2的100次方: {result1}")

# 2、输入两个整数，输出它们的平均数（浮点数）。(使用input函数，在控制台接收用户输入)。
num1 = int(input("请输入第一个整数: "))
num2 = int(input("请输入第二个整数: "))
average = (num1 + num2) / 2
print(f"平均数: {average}")

# 3、对于字符串"你好,python",使用索引获取该字符串最后一个元素。
str3 = "你好,python"
last_element = str3[-1]
print(f"字符串 '{str3}' 的最后一个元素: {last_element}")

# 4、分别用+和*实现字符串"你好,python"的拼接和复制(拼接自身，复制10次)。
str4 = "你好,python"
concatenated_str = str4 + str4
print(f"拼接后的字符串: {concatenated_str}")
copied_str = str4 * 10
print(f"复制10次的字符串: {copied_str}")

# 5、对于字符串"在1做2基3本4数5据6类7型8的9实0验",使用切片获取索引为偶数的所有元素。
str5 = "在1做2基3本4数5据6类7型8的9实0验"
even_index_elements = str5[::2]
print(f"索引为偶数的元素: {even_index_elements}")

# 6、查看print(1+"2")的运行结果，并使用强制类型转换完成字符串的拼接。
# print(1+"2")  # 这行代码会报错，因为不能将整数和字符串直接相加
str6_1 = str(1) + "2"
print(f"强制类型转换后的字符串拼接结果: {str6_1}")

# 7、有字符串"https://zjj.jsu.edu.cn/r/cms/www/default/images/logo.png"
# 使用分割和索引获取该图片的图片名和类型(logo.png)。
str7 = "https://zjj.jsu.edu.cn/r/cms/www/default/images/logo.png"
image_name = str7.split("/")[-1]
print(f"图片名和类型: {image_name}")

# 8、观察以下代码在Python中的运行结果：
i = 1
# y = i++  # Python中没有i++运算符
i += 1
y = i
print(f"i = 1; i += 1; y = i; print(y) 的结果: {y}")

# 9、观察以下代码在Python中的运行结果：
print(f"bool(-1): {bool(-1)}")
print(f"bool(0): {bool(0)}")
print(f"bool(1): {bool(1)}")
print(f"bool(''): {bool('')}")
print(f"bool('1'): {bool('1')}")
print(f"bool('0'): {bool('0')}")
print(f"bool(None): {bool(None)}")

# 10、使用成员运算符，判断字符串"a"是否不在"abc"中。
str10 = "abc"
result10 = "a" not in str10
print(f"'a' 是否不在 '{str10}' 中: {result10}")

# 11、逆序输出字符串"Python"。
str11 = "Python"
reversed_str = str11[::-1]
print(f"字符串 '{str11}' 的逆序: {reversed_str}")

# 12、观察以下程序运行结果：
n = int(input("请输入一个整数："))
print(f"10 <= n <= 50 的结果: {10 <= n <= 50}")

# 13、观察以下程序结果(注意and和or的优先级)：
result13 = True or False and False
print(f"结果是：{result13}")

# 14、替换字符串'晴天,阴天，晴天，雨天'的所有’晴天’为’雪’。
str14 = "晴天,阴天，晴天，雨天"
replaced_str = str14.replace("晴天", "雪")
print(f"替换后的字符串: {replaced_str}")

# 15、使用BeautifulSoup库获取<h1>标签里的文本内容,<a>标签的href属性内容，所有<p>标签的文本内容。
from bs4 import BeautifulSoup

html_doc = """
<html>
<head><title>示例网页</title></head>
<body>
<div class="content">
  <h1 id="main-title">欢迎学习BeautifulSoup</h1>
  <p class="text">第一段文本</p>
  <p class="text">第二段文本</p>
  <p class="title">第三段文本</p>
  <a href="https://example.com">示例链接</a>
  <a title='888'>示例链接</a>
</div>
</body>
</html>
"""
soup = BeautifulSoup(html_doc, "html.parser")

h1_text = soup.find("h1").text
print(f"h1 标签的文本内容: {h1_text}")

a_href = soup.find("a")["href"]
print(f"第一个 a 标签的 href 属性内容: {a_href}")

p_tags = soup.find_all("p")
p_texts = [p.text for p in p_tags]
print(f"所有 p 标签的文本内容: {p_texts}")
