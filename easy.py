import sys

def add_str_to_lines(f_name, str_to_add_start, str_to_add_end):
    with open(f_name, "r") as f:
        lines = f.readlines()
        for index, line in enumerate(lines):
            value = line.strip()
            lines[index] = str_to_add_start + value + str_to_add_end + value + ".log" +"\n"

    with open(f_name, "w") as f:
        for line in lines:
            f.write(line)

if __name__ == "__main__":
    print(sys.argv[1])
    str_to_add_start = "grep "
    str_to_add_end = " " + sys.argv[1] + "*>"
    f_name = "test.txt"
    add_str_to_lines(f_name=f_name, str_to_add_start=str_to_add_start, str_to_add_end=str_to_add_end)
