# XFileBlame
A script to check whether unwanted file types / sizes are stored in a specified location.
XFileBlame can be used to find a movie you've lost or even to keep track of unwanted files stored on your server.

Usage :   //--help

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
# Extensions
you can easily use XFileBlameMaster for your own project.

Example:

    import XFileBlameMaster
    XFB = XFileBlameMaster.XFileBlameMa(rootDirectory='/', extensionType=2, outputLevel=0, useExtension=True)
    xfiles = XFB.blameFiles()
    print(str(xfiles))
To use this the XFileBlameMaster.py must be in the same folder as your python file

Note :

I am not responsible for illegal acts you do with this program.
