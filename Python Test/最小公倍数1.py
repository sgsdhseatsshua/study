from math import gcd

def lcm(a, b):
    """计算两个数的最小公倍数"""
    return a * b // gcd(a, b)

def find_lcm_of_input():
    """从用户输入中读取数字，计算并返回这些数字的最小公倍数"""
    # 提示用户输入数字，用空格分隔
    input_str = input("请输入一系列数字，用空格分隔：")
    # 将输入的字符串分割成列表，并将每个元素转换为整数
    numbers = list(map(int, input_str.split()))
    
    # 初始化结果为列表的第一个元素
    result = numbers[0]
    
    # 遍历列表中的每个元素，更新结果为当前结果与该元素的最小公倍数
    for number in numbers[1:]:
        result = lcm(result, number)
    
    print("这些数字的最小公倍数是:", result)

# 调用函数
find_lcm_of_input()