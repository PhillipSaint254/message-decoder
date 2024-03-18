def read_pattern(message_file):  # Speration of pattern reading function
    dictionary = dict()

    with open(message_file, 'r') as file:
        file_lines = file.readlines()

        for line in file_lines:
            # keep first part of each line as key
            key = line.strip().split(" ")[0]
            # keep second part of each line as value
            value = line.strip().split(" ")[1]
            dictionary[key] = value.strip()

        return dictionary  # return a dictionary of all keys and values


def decode(message_file):
    dictionary = read_pattern(message_file)

    sorted_values = sorted(dictionary.keys())

    pyramid = create_pyramid(sorted_values)

    display_pyramid(pyramid)

    message = ""

    for line in pyramid:
        message += dictionary[line[-1]] + ' '

    return message


def create_pyramid(numbers):
    pyramid = []
    row_length = 1
    current_index = 0
    while current_index < len(numbers):
        row = [str(numbers[current_index])]
        current_index += 1
        for j in range(1, row_length):
            if current_index < len(numbers):
                row.append(str(numbers[current_index]))
                current_index += 1
            else:
                break
        pyramid.append(row)
        row_length += 1
    return pyramid


def display_pyramid(pyramid):
    for row in pyramid:
        print(" ".join(row).center(len(pyramid[-1]) * 2))


print(f"Decoded message: {decode('pattern.txt')}")
