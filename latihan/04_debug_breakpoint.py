def rata_rata(data):
    if len(data) == 0:
        return 0

    total = sum(data)
    return total / len(data)

print(rata_rata([80, 90, 70]))
print(rata_rata([80, 90]))
print(rata_rata([60, 70, 80, 90]))
print(rata_rata([]))