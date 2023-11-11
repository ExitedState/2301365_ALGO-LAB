def read_test_cases_from_txt(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Parse the alphabet set
    alphabet_set = lines[0].strip().split()

    # Parse the lengths of the pattern and the text
    lengths = lines[1].strip().split()
    pattern_length = int(lengths[0])
    text_length = int(lengths[1])

    # Parse the pattern
    pattern = ''.join(lines[2].split())

    # Parse the text
    text = ''.join(lines[3].split())
    return alphabet_set, pattern, text

if __name__ == '__main__':
    alphabet_set, pattern, text = read_test_cases_from_txt('LAB9\Example_LAB9.txt')
    print(alphabet_set)
    print(pattern)
    print(text)