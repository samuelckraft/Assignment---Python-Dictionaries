def odd_count(n):
    odd_numbers = []
    for num in range(1,n):
        if num % 2 != 0:
            odd_numbers.append(num)
    return len(odd_numbers)
    pass

print(odd_count(340485573))