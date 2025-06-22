import time, csv, math

class Stack:
    def __init__(self, stack=[]):
        self.stack = stack
    def push(self, n):
        self.stack.append(n)
    def pop(self):
        return self.stack.pop()

def scientific_notation(n):
    if n == 0: return "0e0"
    sign  = "-" if n < 0 else ""
    power = int(math.log10(abs(n)))
    coeff = abs(n) / (10 ** power)
    coeff = round(coeff, 2)
    if int(coeff) == coeff: coeff = int(coeff)
    return f"{sign}{coeff}e{power}"

prev1 = 0
prev2 = 1
stack = Stack()
n = 3
total_time = 0

with open("logs.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows([
        ["n", "value", "time_taken"],
        [1, scientific_notation(0), 0],
        [2, scientific_notation(1), 0],
    ])
    while total_time < 1:
        # compute fibo
        start_time = time.time()
        cur = prev1 + prev2
        prev1, prev2 = prev2, cur
        end_time = time.time()

        # compute time taken
        time_taken = end_time - start_time
        total_time += time_taken
        total_time = round(total_time, 3)

        # update logs
        writer.writerow([n, scientific_notation(cur), total_time])
        stack.push(cur)
        n += 1

print(f"{n-1}th number {scientific_notation(stack.pop())} took {total_time} seconds")
