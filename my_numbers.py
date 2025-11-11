numbers = [12,5,8,3,15]

# ascending (returns a new list)
numbers_asc = sorted(numbers)
print("Ascending:", numbers_asc)  # Output: [3, 5, 8, 12, 15]

# descending (returns a new list)
numbers_desc = sorted(numbers, reverse=True)
print("Descending:", numbers_desc)  # Output: [15, 12, 8, 5, 3]

# in-place sort (modifies original list)
numbers.sort()               # ascending in-place
print("In-place ascending:", numbers)
numbers.sort(reverse=True)   # descending in-place
print("In-place descending:", numbers)