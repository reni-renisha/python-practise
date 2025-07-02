arr = []

n = int(input("Enter number of elements: "))

print("Enter the elements:")
for i in range(n):
    num = int(input())
    arr.append(num)

target = int(input("Enter target sum: "))

found = False

for i in range(n):
    for j in range(i + 1, n):
        if arr[i] + arr[j] == target:
            print(f"Pair found: {arr[i]} + {arr[j]} = {target}")
            found = True
            break
    if found:
        break

if not found:
    print("No pair found.")
