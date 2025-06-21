import time, csv, os, math

def naive_fib(n):
    if n == 0 or n == 1: return n
    return naive_fib(n - 1) + naive_fib(n - 2)

def fib(n):
    fibs = [0, 1]
    for i in range(2, n+1):
        fibs.append(fibs[i-1] + fibs[i-2])
    return fibs[-1]

def scientific_notation(n):
    if n == 0: return "0e0"
    sign  = "-" if n < 0 else ""
    power = int(math.log10(abs(n)))
    coeff = abs(n) / (10 ** power)
    coeff = round(coeff, 2)
    if int(coeff) == coeff: coeff = int(coeff)
    return f"{sign}{coeff}e{power}"

def get_biggest_fib(seconds, print_every_number=True, log_filename=""):
    n = 0
    
    # start file correctly
    filename = f"{log_filename}.csv"
    if os.path.isfile(filename):
        with open(filename, "r") as file:
            reader = list(csv.reader(file))
            if len(reader) > 1: # resume from next n
                try: n = int(reader[-1][0])
                except ValueError: n = 0
    else:
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["n", "value", "time_taken"])

    while True:
        # compute fib
        start = time.time()
        value = fib(n)
        end = time.time()
        n += 1

        # calculate time
        time_taken = end - start
        if print_every_number:
            print(f"{n} took {round(time_taken, 2)} seconds")

        # update logs
        if len(log_filename) > 0:
            with open(filename, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([n, scientific_notation(value), time_taken])

        # check time
        if time_taken > seconds:
            print("========================")
            print(f"Final answer: {n-1}th number {value}")
            break

if __name__ == "__main__":
    get_biggest_fib(1, log_filename="logs", print_every_number=False)
