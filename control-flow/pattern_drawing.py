def draw_square_pattern(size):
    row_counter = 0
    while row_counter < size:
        for _ in range(size):
            print("*", end="")
        print()
        row_counter += 1

# Prompt the user for input
try:
    pattern_size = int(input("Enter the size of the pattern:"))
    if pattern_size > 0:
        draw_square_pattern(pattern_size)
    else:
        print("Please enter a positive integer.")
except ValueError:
    print("Invalid input. Please enter an integer.")

