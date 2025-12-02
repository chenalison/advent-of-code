import os

if os.path.basename(os.getcwd()).isdigit(): # move up a level
    os.chdir('..')
assert os.path.basename(os.getcwd()), 'advent-of-code'

while True:
    year = input("Enter year as 4 digit (2025, 2026): ")
    if year.isdigit() and len(year) == 4:
        break

while True:
    day = input("Enter day as 2 digit (01, 10): ")
    if day.isdigit():
        day = day.rjust(2, "0")
        break

basepath = os.path.join(year, "day"+day)
os.makedirs(basepath)

files = ['input', 'part1.py', 'part2.py']

for file in files:
    with open(os.path.join(basepath, file), 'a') as f:
        pass

print("Folder and files created for", year, "day", day)