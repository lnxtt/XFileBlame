import XFileBlameMaster
import sys
import os

rootDir = '/'
interval = ''
emailContact = ''
suspiciousSize = 0
extensionType = 1

help = """
You're using XFileBlame by Marvin Plum.
This programm searches for files with a specific attribute (file-extension or size) and tells you their location.
By default it searches for movies in / with no repetition or E-Mail warning included.
With :
    -e you insert a E-Mail with that you get contacted if a searched file was found
       To use this feature you must fill E-Mail credentials(the E-Mail XFileBlame should send you the data from)
       in the XFileBlameMaster.py
    -i you set the interval (in Seconds) in which a search gets repeated

File type giving arguments : 
    -m sets the file types to movies 
    -p sets the file types to programmes
    -mp looks for both
    -s looks for Storage hungry files
    The minimum file size in mb can be given behind all

To search in an not default location just write the location into the arguments

Example:
    python run.py /home/ -i 300 -e foo@bar.com -s 1000

Note :
    I'm not responsible for illegal actions you do with this programm
"""

for i in range(0, len(sys.argv)):#checks the input
    arg = sys.argv[i]
    val = ''
    if i < (len(sys.argv) - 1):#used to check if an value is given behind an argument
        val = sys.argv[i + 1]
    if arg == '-e':
        try:
            if val != '':
                emailContact = str(val)
            else:
                print('No Email input after -e')
                sys.exit(0)
        except Exception:
            print('unable to set the E-Mail contact address - abort')
            sys.exit(0)
    if arg == '-i':
            if val != 0 and val != '':
                try:
                    interval = str(val)
                except Exception:
                    print('unable to set the interval - Going on without it')
            else:
                print('0 or '' is not a valid interval')
                sys.exit(0)
    if os.path.isdir(arg):
        rootDir = arg
    if arg == '-m' or arg == '-p' or arg == '-mp' or arg == '-s':
        if val != '':
            try:
                suspiciousSize = str(val)
            except Exception:
                print('unable to set the suspicious file size - Going on without it')
    if arg == '-m':
        extensionType = 1
    if arg == '-p':
        extensionType = 2
    if arg == '-mp':
        extensionType = 3
    if arg == '-s':
        extensionType = 4
    if arg == '-help' or arg == '--help' or arg == '-?':
        print(help)
        sys.exit(0)

if not os.path.isdir(str(rootDir)):
    print('The Directory: ' + rootDir + ' does not exist')
    sys.exit(0)

try:
    XFB = XFileBlameMaster.XFileBlameMa(rootDir, interval, emailContact, suspiciousSize, extensionType)
    XFB.blameFiles()
except Exception:
    print('unable to call XFileBlameMaster - abort')
    sys.exit(0)
