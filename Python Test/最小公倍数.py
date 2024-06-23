import math

def gcd(a, b):
    """计算两个数的最大公约数"""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """计算两个数的最小公倍数"""
    return a * b // gcd(a, b)

def array_lcm(arr):
    """计算数组中所有元素的最小公倍数"""
    current_lcm = arr[0]
    for num in arr[1:]:
        current_lcm = lcm(current_lcm, num)
    return current_lcm

def main():
    numbers = []
    print("请输入数字，输入 'done' 结束输入:")
    while True:
        user_input = input("请输入一个数字: ")
        if user_input.lower() == 'done':
            break
        try:
            num = int(user_input)
            numbers.append(num)
        except ValueError:
            print("请输入有效的数字。")
    
    if numbers:
        result = array_lcm(numbers)
        print("输入数字的最小公倍数是:", result)
    else:
        print("没有输入有效的数字。")

if __name__ == "__main__":
    main()
