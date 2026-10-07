# Our generator
def read_logs(filepath):
    print("Opening file...")

    with open(filepath, "r") as f:

        for line in f:
            yield line.strip()


for log in read_logs("actions.log"):
    print(log)