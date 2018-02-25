
def load(str):
    words = 0;
    chars = 0;
    lines = 0;
    with open(str) as f:
        for line in f:
            lines = lines + 1
            line = line.split()
            words = words + len(line)
            for item in line:
                chars = chars + len(item)
    print(str)
    print("lines ",lines);
    print("words ",words);
    print("chars ",chars);

x = int(input('Enter Value of x\n'))
load("first.txt")
if(x % 2 == 0):
    load("even.txt")
else:
    load("odd.txt")
