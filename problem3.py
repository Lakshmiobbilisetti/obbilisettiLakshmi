def generate_conditional_odd_series(a: int):
    limit = a if a % 2 != 0 else a - 1  # Adjust for even input
    result = [2 * i + 1 for i in range(limit)]
    return result
a = int(input("Enter a number: "))
series = generate_conditional_odd_series(a)
print("Output:", ', '.join(map(str, series)))
