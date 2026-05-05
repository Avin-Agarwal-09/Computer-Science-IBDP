NAMES = ["Jane", "Smith", "Rafael", "Uysal", "Ishmael", "Ahmed", "Sara", "Jonsonn"]

first_names = []
surnames = []

for i in range(0, len(NAMES), 2):
    first_names.append(NAMES[i])
    surnames.append(NAMES[i + 1])

print("First Names:", first_names)
print("Surnames:   ", surnames)

n = len(surnames)

for pass_num in range(n - 1):
    for i in range(n - 1 - pass_num):
        if surnames[i] > surnames[i + 1]:
            surnames[i], surnames[i + 1] = surnames[i + 1], surnames[i]
            first_names[i], first_names[i + 1] = first_names[i + 1], first_names[i]

print("Sorted Surnames:   ", surnames)
print("Sorted First Names:", first_names)

def binary_search(surnames, target):
    low = 0
    high = len(surnames) - 1

    while low <= high:
        mid = (low + high) // 2

        if surnames[mid] == target:
            return mid                 
        elif surnames[mid] < target:
            low = mid + 1             
        else:
            high = mid - 1           

    return -1                       



target = input("Enter surname to search for: ")
result = binary_search(surnames, target)

if result != -1:
    print(f"Found! {surnames[result]}, {first_names[result]} is at index {result}")
else:
    print(f"Surname '{target}' not found in the list")