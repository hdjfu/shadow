# 1, 1, 2, 3, 5

def fibonacci(position):#10
    if position >= 3:
        output = fibonacci(position-1) + fibonacci(position -2) #9, 8  | 9 + 8
    else:
        output = 1
    print('out:', output)
    return output


response = fibonacci (6)
print(response)

