def open_poem():
    text = open('dane/poem.txt').readlines()


    poem_lines = []

    for line in text:
        line = line.strip()
        poem_lines.append(line)
    return poem_lines

poem = open_poem()
for l in poem:
    print(l)