n = "123456789"

left, right = 0, len(n) - 1

iterations = 0

while iterations < len(n):
    if left == right:
        print(2*left*" " + n[left])
    elif left < right:
        print(2*left*" " + n[left] + (2*(len(n[left+1: right])) + 1)*" " + n[right])
    elif left > right:
        print(2*right*" " + n[right] + (2*(len(n[right+1: left])) + 1)*" " + n[left])
    left += 1
    right -= 1
    iterations += 1