# SUMMARY: This script contains two functions:
# 1. sum_numbers: Reads numbers from input file and creates output file with sums
# 2. count_num_in_file: Counts occurrences of a specific number in the input file


def sum_numbers(filename):
    """
    Reads pairs of numbers from input file and creates output file with their sums.

    Parameters:
        filename (str): Name of the input file to read

    Output:
        Creates output.txt file with sums and original number pairs
    """
    print("\nQuestion 1 Results (Creating output.txt):")
    print("-" * 40)

    output_lines = []
    # Read input file line by line
    with open(filename, 'r') as infile:
        for line in infile:
            # Strip whitespace and split by comma
            nums = line.strip().split(',')
            # Convert to integers and calculate sum
            num1, num2 = int(nums[0]), int(nums[1])
            sum_nums = num1 + num2
            # Format the output line
            output_line = f"sum: {sum_nums} | {num1},{num2}"
            output_lines.append(output_line)
            # Print to console
            print(output_line)

    # Write all lines to output file
    with open('output.txt', 'w') as outfile:
        outfile.write('\n'.join(output_lines))
        outfile.write('\n')


def count_num_in_file(filename, target):
    """
    Counts how many times a specific number appears in the input file.

    Parameters:
        filename (str): Name of the input file to read
        target (int): Number to count occurrences of

    Returns:
        int: Count of how many times target number appears in file
    """
    count = 0
    # Open and read input file
    with open(filename, 'r') as infile:
        for line in infile:
            # Strip whitespace and split by comma
            nums = line.strip().split(',')
            # Check each number in the pair
            if int(nums[0]) == target:
                count += 1
            if int(nums[1]) == target:
                count += 1
    return count


# Driver code
if __name__ == "__main__":
    # Question 1 - Create output.txt file
    sum_numbers("input-1.txt")

    # Question 2 - Count occurrences of specific numbers
    print("\nQuestion 2 Results (Counting numbers):")
    print("-" * 40)
    print(f"Number of 6's in file: {count_num_in_file('input-1.txt', 6)}")  # Should print 3
    print(f"Number of 8's in file: {count_num_in_file('input-1.txt', 8)}")  # Should print 2
