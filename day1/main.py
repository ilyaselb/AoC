count = 0
pointer = 50

with open("input.txt", "r") as f:
    for line in f:
        rotation = line[0]
        duration = int(line.strip()[1:])
        
        count += duration // 100
        
        remainder = duration % 100
        
        if rotation == "R":
            if pointer + remainder >= 100:
                count += 1
            pointer = (pointer + remainder) % 100
            
        else:
            if pointer > 0 and pointer - remainder <= 0:
                count += 1
            pointer = (pointer - remainder) % 100

print(count)