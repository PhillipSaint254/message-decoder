

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

    dictionary = read_pattern("pattern.txt")

    with open(message_file, 'r') as file:
        file_lines = file.readlines()
        message = ''

        for line in file_lines:
            # take the last number of each line for message decode
            key = line.strip().split(" ")[-1]
            message += dictionary[key] + ' '

        return message


print(f"Decoded message: {decode('test.txt')}")
