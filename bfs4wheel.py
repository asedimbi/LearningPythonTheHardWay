#BFS 4 Wheel Lock
def equals(arr1, arr2):
    for a,b in zip(arr1, arr2):
        if a!=b:
            return False
    return True

def next_combos(arr):
    out =[]
    for i in range(len(arr)):
        temp = arr[:]
        temp[i] += 1
        yield temp

target = [9,9,9,9]

start = [0,0,0,0]
FINAL = False
count_steps = 0


seen = {'0000'}

Q = [start]
#print(Q)
cur_len = 1
while(Q and not FINAL):
    next_len = 0
    while(cur_len > 0 and not FINAL):
        combo = Q.pop(0)
        #print(combo)
        cur_len -=1
        count_steps += 1
        if equals(combo, target):
            FINAL = True
            break
        else:
            for temp in next_combos(combo):
                str_temp = ''.join([str(x) for x in temp])
                if str_temp not in seen:
                    seen.add(str_temp)
                    Q.append(temp)
                    next_len += 1
    cur_len = next_len


print(combo, count_steps, target, FINAL)
