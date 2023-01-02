import sys, os, re, shutil
# The given file Path
print(f'hi: {sys.argv[0]}')


# Checking where we are
cwd = os.getcwd()
items = os.listdir()
print(cwd)
print(items)

#Regex for file types
ExtentionRe = re.compile(r'\.\w+$')

# So it doesnt throw errors about making files
def TryMakeFiles(path):
  try:
    os.mkdir(path)
  except FileExistsError:
    print(f'{path} exists')


path = os.path.join(cwd,'Sorted_Files')
TryMakeFiles(path)

fileTypes = []



# Check all file extentions
for i in items:
  result = re.search(ExtentionRe,str(i))
  # Get all file types
  if result:
      print(result.group())
      if result.group() not in fileTypes:
        fileTypes.append(result.group())
  # If a folder
  else:
    print('no Match')

extentionDirs = []

# Make subfolders based on each file
for i in fileTypes:
  newFolder = os.path.join(path,i)
  TryMakeFiles(newFolder)
  extentionDirs.append(newFolder)

print(extentionDirs)

# Place each file by type and add it to the folder. Probably a less convoluted way to do this but who cares
for i in items:
  extention = re.search(ExtentionRe,str(i))
  if extention:
    print(extention.group())
    for j in enumerate(extentionDirs):
      if extention.group() in j[1]:
        print(f'{extention.group()} is in {j[1]}')
        shutil.move(i,j[1])
        #print(f'{j[1]} and {i}')