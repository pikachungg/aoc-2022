
#Requires manual input [.] on every empty space for input

def create_crates(n):
    return [[] for i in range(n)]

f = open('input.txt')
n = 0

crates = create_crates(9)

for line in f: 
    line = line.strip().split(' ')
    if n < 8:
        for i in range(len(line)): 
            if line[i] != '[.]':
                crates[i].insert(0, line[i][1])
    if n > 9:
        amount = int(line[1])
        from_crate = int(line[3]) - 1
        to_crate = int(line[5]) - 1
        removed_items = []
        while(amount > 0 and len(crates[from_crate]) > 0):
            removed_items.append(crates[from_crate].pop())
            amount -= 1
        crates[to_crate] += (removed_items[::-1])
    n += 1

stro = ""

for i in crates: 
    stro += i[-1]

print(stro)