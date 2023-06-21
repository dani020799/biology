import sys

def split_file_by_keyword(input_file, present):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    found_lines = []
    remaining_lines = []
    linesnumber= len(lines)

    i=0
    for line in lines:

        if i < linesnumber*present:
            found_lines.append(line)
        else:
            remaining_lines.append(line)
        i = i+1

    if found_lines:
        with open('training.txt', 'w') as file:
            file.writelines(found_lines)
       # print(f"Lines containing the keyword '{present}' have been saved in 'found_lines.txt'.")

    if remaining_lines:
        with open('testing.txt', 'w') as file:
            file.writelines(remaining_lines)
       # print("Lines without the keyword have been saved in 'remaining_lines.txt'.")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python split_file.py <input_file> <keyword>")
    else:
        input_file = sys.argv[1]
        present = float(sys.argv[2])
        split_file_by_keyword(input_file, present)
