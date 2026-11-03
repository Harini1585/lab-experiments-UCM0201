
print("TOWER OF HANOI")
print("----------------")

# 1. Accept number of disks
n = int(input("Enter the number of disks: "))

# Initialize move count
count = 0

# 2. Recursive function
def tower_of_hanoi(n, source, auxiliary, destination):

    global count

    if n == 1:
        count += 1
        print("Move disk 1 from", source, "to", destination)
        return

    # Move n-1 disks to auxiliary tower
    tower_of_hanoi(n - 1, source, destination, auxiliary)

    # Move largest disk to destination
    count += 1
    print("Move disk", n, "from", source, "to", destination)

    # Move n-1 disks to destination tower
    tower_of_hanoi(n - 1, auxiliary, source, destination)


# 3. Solve Tower of Hanoi
if n > 0:
    tower_of_hanoi(n, 'A', 'B', 'C')

    # 4. Display total moves
    print("\nTotal number of moves:", count)

    # 5. Verify minimum moves
    minimum = 2**n - 1
    print("Minimum number of moves:", minimum)

    if count == minimum:
        print("Verification Successful!")
    else:
        print("Verification Failed!")
else:
    print("Enter a positive number of disks.")
