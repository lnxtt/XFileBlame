# XFileBlame
A script to check if non wanted file types/sizes getting stored in a speciffic location.
XFileBlame can be used to find a movie you lost or even to constantly check for non wanted files stored on your server.

Usage :   //--help

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
