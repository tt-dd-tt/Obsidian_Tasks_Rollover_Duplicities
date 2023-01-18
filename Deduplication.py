import sys

if len(sys.argv) < 2:
    print("Please provide a file name as an argument.")
    sys.exit()

file_name = sys.argv[1]

duplicates = []
lines = []

with open(file_name, 'r') as f:
    for line in f:
        if line.startswith('-[]') and line.strip() not in lines:
            lines.append(line.strip())
        elif line.startswith('-[]') and line.strip() in lines:
            duplicates.append(line.strip())

if duplicates:
    with open(file_name, 'r') as f:
        content = f.read()
    for duplicate in duplicates:
        content = content.replace(duplicate, '')
    with open(file_name, 'w') as f:
        f.write(content)
    print("Duplicates removed:")
    for duplicate in duplicates:
        print(duplicate)
else:
    print("No duplicates found.")
