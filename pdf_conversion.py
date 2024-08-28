import os, subprocess

target = "C:\\Users\\fotip\\OneDrive - Seneca\\Documents\\DPA101\\input"
os.chdir(target)
print(os.getcwd())

for root, directories, filenames in os.walk(target):
    for file in filenames:
        if file.endswith('jpg'):
            prefix,suffix = file.split('.')
            #input and processed are subdirectories of DPA101
            #checking if prefix.pdf file exists in processed directory
            if os.path.isfile('..\\processed\\'+prefix+'.pdf'):
                print("File " + prefix + ".jpg already converted, skipping...")
            else: 
                print("Converting file " + prefix + '.jpg')
                cmd_string = 'tesseract ' + file + ' ' + '..\\processed\\' + prefix + ' PDF'
                rtrn = subprocess.call(cmd_string)
                if rtrn != 0:
                    #tested with error.jpg file in input folder
                    print('Warning, error converting file ' + prefix + '.jpg')
                else:
                    print(rtrn) #will print 0 only when convertion is sucessful