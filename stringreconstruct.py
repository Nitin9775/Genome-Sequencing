def StringConstruct(kmers):
    Required_string = [kmers[0]]
    n = len(kmers)
    for i in range(1,n):
        Required_string.append(kmers[i][-1])
    return Required_string

with open(r"C:\Users\LENOVO\Downloads\dataset_30182_3 (1).txt", "r") as file:
    content = file.read()             # Read entire content
    kmers = content.strip().split()
print("".join(StringConstruct(kmers)))

