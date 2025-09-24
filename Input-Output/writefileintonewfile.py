with open("I/O Excercises/test.txt", 'r') as fp:
    lines = fp.readlines()

with open("I/O Excercises/new_file.txt", 'w') as fp:
    count = 0

    for line in lines:

        if count == 4:
            count += 1
            continue
        else:
            fp.write(line)
        count += 1