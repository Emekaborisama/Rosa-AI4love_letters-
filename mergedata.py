


filenames = ['file1.txt', 'file2.txt', ...]
with open('./data/', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
