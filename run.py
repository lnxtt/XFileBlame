import XFileBlameMaster
import sys
import os

rootDir = '/'
interval = ''
emailContact = ''
suspiciousSize = 0
extensionType = 1
outputLevel = 1

help = """
You're using XFileBlame by Marvin Plum.
This program searches for files with a specific attribute (file-extension or size) and tells you their location.
By default, it searches for movies contained in / without repeating or email warning.
With:
  -e you set an email with that you are contacted when a searched file was found
     To use this feature, you must complete e-mail credentials (the  email XFileBlame should send you the data from)
     in the XFileBlameMaster.py
  -i you set the interval (in seconds) in which a search will be repeated
  -o XfileBlame will show you live output(Currently analysed directory/Last found file) - You will still see if a
     search begins or ends(all found files will be printed if that happens)
     After -0 you can give the arguments[0,1,2]
        0 = only errors 
        1 = 0 + minimum output(search begin,end,results)
        2 = all output
     1 is default

Type giving arguments:
  -m sets the file types to movies
  -p sets the file types to programs
  -mp searches both
  -s is looking for storage hungry files
  The minimum file size in mb can be given after all

To search in a non-standard directory, just write the directory path into the arguments.

Example:
python3 run.py / home / -i 300 -e foo@bar.com -s 1000 -o 2

Note :
I am not responsible for illegal acts you do with this program.

"""

for i in range(0, len(sys.argv)):#checks the input
    arg = sys.argv[i]
    val = ''
    if i < (len(sys.argv) - 1):#used to check if an value is given behind an argument
        val = str(sys.argv[i + 1])
    if arg == '-e':
        try:
            if val != '':
                emailContact = val
            else:
                print('No Email input after -e')
                sys.exit(0)
        except Exception:
            print('unable to set the E-Mail contact address - abort')
            sys.exit(0)
    if os.path.isdir(arg):
        rootDir = arg
    if arg == '-m':
        extensionType = 1
    if arg == '-p':
        extensionType = 2
    if arg == '-mp':
        extensionType = 3
    if arg == '-s':
        extensionType = 4
    if str.isdigit(val):
        if arg == '-i':
            if int(val) > 0:
                try:
                    interval = val
                except Exception:
                    print('unable to set the interval - Going on without it')
            else:
                print('Input of a valid interval not found (Did you inserted 0 ?)')
                sys.exit(0)
        if int(val) >= 0:
            if arg == '-m' or arg == '-p' or arg == '-mp' or arg == '-s':
                try:
                    suspiciousSize = val
                except Exception:
                    print('unable to set the suspicious file size - Going on with 0 mb')
            if arg == '-o':
                try:
                    if int(val) <= 2:
                        outputLevel = val
                    else:
                        print(val + ' is not a valid output level[0,1,2] - use --help to learn more')
                except Exception:
                    print('unable to set the output level - Going on with level 1')
    if arg == '-help' or arg == '--help' or arg == '-?':
        print(help)
        sys.exit(0)

if not os.path.isdir(str(rootDir)):
    print('The Directory: ' + rootDir + ' does not exist')
    sys.exit(0)

try:
    XFB = XFileBlameMaster.XFileBlameMa(rootDir, interval, emailContact, suspiciousSize, extensionType, outputLevel)
    XFB.blameFiles()
except Exception as error:
    print('unable to call XFileBlameMaster - abort | error : ' + str(error))
    sys.exit(0)
