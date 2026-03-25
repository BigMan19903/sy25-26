
import glob

files = glob.glob("server_dump/*.txt")

status_counts = {'OK': 0, 'WARN': 0, 'ERROR': 0}
status_files = {'OK': [], 'WARN': [], 'ERROR': []}

for file in files:
    with open(file) as f:
        content = f.read()
    
        for status in status_counts.keys():
           if status in content:
                status_counts[status] += 1
                status_files[status].append(file)

print("Status counts:")
for status, count in status_counts.items():
    print(f"{status}: {count}")

for status in status_counts.keys():
    response = input(f"Do you want to see the files with status '{status}'? (yes/no): ").strip().lower()
    if response == 'yes':
        print(f"Files with status '{status}':")
        for fname in status_files[status]:
            print(f" - {fname}")