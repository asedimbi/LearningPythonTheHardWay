#Generates all possible permutations of an array on non-duplicate elements
n = int(input('Enter n value less than 10\n> '))

class perms:
    def __init__(self, n):
        self.arr = list(range(1, n+1))
        self.out = []

    def swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def permute(self, l):
        if(l == len(self.arr) - 1):
            self.out.append(self.arr[:])
        for i in range(l, len(self.arr)):
            self.swap(i, l)
            if(self.arr[l] % (l + 1) == 0 or (l+1) % self.arr[l] == 0):
                self.permute(l+1)
            self.swap(i, l)

p = perms(n)
p.permute(0)

for i,ar in enumerate(p.out):
    print(i, ar)
    pass

