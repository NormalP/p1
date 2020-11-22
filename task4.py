num = int(input())
max_num = 0
while num > 0:
    new_num = (num % 10)
    if max_num < new_num:
        max_num = new_num
    num = (num // 10)
print(f"biggest digit in number is {max_num}")