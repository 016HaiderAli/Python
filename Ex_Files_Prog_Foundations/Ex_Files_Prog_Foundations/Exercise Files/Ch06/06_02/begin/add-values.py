# this here opens a file by name values.txt and read it
infile = open('values.txt', 'rt')
# this here creates a variables which opens a file and this wt is for the purpose of writing text in it
outfile = open('values-totaled.txt', 'wt')
print('Processing input')
sum = 0
for line in infile:
    sum += int(line)
    # rstrip is a method which eliminates spaces from the right side, and file is telling us that outfile
    print(line.rstrip(), file=outfile)
print('\nTotal: ' + str(sum), file=outfile)
outfile.close()
print('Output complete')
