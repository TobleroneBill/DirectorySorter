import sys, os, re, shutil

# The given file Path
print(f'hi: {sys.argv[0]}')

# Checking where we are
cwd = os.getcwd()
items = os.listdir()
print(cwd)
print(items)

# Regex for file types
ExtentionRe = re.compile(r'\.\w+$')


# So it doesnt throw errors about making files
def TryMakeFiles(path):
    try:
        os.mkdir(path)
    except FileExistsError:
        print(f'{path} exists')


path = os.path.join(cwd, 'Sorted_Files')
TryMakeFiles(path)

fileTypes = []

# Check all file extentions
for i in items:
    if i == 'main.py':
        continue
    result = re.search(ExtentionRe, str(i))
    # Get all file types
    if result:
        print(result.group())
        # Ignore the .bat or main.py file
        if result.group() == '.bat':
            continue
        if result.group() not in fileTypes:
            fileTypes.append(result.group())
    # If a folder
    else:
        print('no Match')

extentionDirs = []

# Make subfolders based on each file
for i in fileTypes:
    newFolder = os.path.join(path, i)
    TryMakeFiles(newFolder)
    extentionDirs.append(newFolder)

print(extentionDirs)

# Place each file by type and add it to the folder. Probably a less convoluted way to do this but who cares
for i in items:
    extention = re.search(ExtentionRe, str(i))
    if extention:
        print(extention.group())
        for j in enumerate(extentionDirs):
            if extention.group() in j[1]:
                print(f'{extention.group()} is in {j[1]}')
                shutil.move(i, j[1])
                print(f'{j[1]} and {i}')
    # if no extetion, this must be a folder
    else:
        # move folder into sorted file.
        try:
            shutil.move(i, path)
        except:  # try except is just there on the off chance it throws some wierd errors (which it has before i added this)
            continue

# Might add a thing so that if run from command line, will save logs into a text file
os.system("pause")
