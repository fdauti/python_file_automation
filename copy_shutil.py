import os, shutil

course_dir = "C:\\Users\\fotip\\OneDrive - Seneca\\Documents\\DPA101"
if os.path.isdir(course_dir):
    print('DPA101 directory already exists.')
output = course_dir + '\\output'
if os.path.isdir(output):
    print('"output" directory already exists.')
else:
    os.mkdir(output)
processed = course_dir + '\\processed'
if os.path.isdir(processed):
    print('"processed" directory already exists.')
else:
    os.mkdir(processed)

companies = ['ACME', 'FOOBAR', 'BIGCORP']
for company in companies:
    filepath = output + '\\' + company
    if os.path.isdir(filepath):
        print(filepath + ' exists.')
    else:
        os.mkdir(filepath)

for root, directories, filenames in os.walk(processed):
    print('Your current directory is: ' + root)
    # print('The subdirectories of ' + root + ' are:')
    # for directory in directories:
    #     print(directory)
    print('Here are the files: ')
    for file in filenames:
        print(os.path.join(root, file))
        if file.endswith('pdf') and file.startswith('ACME'):
            outpath = os.path.join(output, 'ACME', file)
            if not os.path.isfile(outpath):
                print(file + ' not found at destination, copying it now...')
                shutil.copy(processed+'\\'+file, output+'\\ACME')
        elif file.endswith('pdf') and file.startswith('FOOBAR'):
            outpath = os.path.join(output, 'FOOBAR', file)
            if not os.path.isfile(outpath):
                print(file + ' not found at destination, copying it now...')
                shutil.copy(processed+'\\'+file, output+'\\FOOBAR')
        elif file.endswith('pdf') and file.startswith('BIGCORP'):
            outpath = os.path.join(output, 'BIGCORP', file)
            if not os.path.isfile(outpath):
                print(file + ' not found at destination, copying it now...')
                shutil.copy(processed+'\\'+file, output+'\\BIGCORP')