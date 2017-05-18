# XFileBlame
A script to check whether unwanted file types / sizes are stored in a specified location.
XFileBlame can be used to find a movie you've lost or even to keep track of unwanted files stored on your server.

Usage :   //--help

By default, it searches for movies contained in / without repeating or email warning.
With:
-e you send an email with that you are contacted when a searched file was found
To use this feature, you must complete e-mail credentials (the XFileBlame email should send you the data)
In the XFileBlameMaster.py
-i Set the interval (in seconds) in which a search is repeated

Type the type of arguments:
-m sets the file types to movies
-p sets the file types to programs
-mp searches both
-s is looking for hungry files
The minimum file size in mb can be given after all

To search in a non-standard place, just write the place in the arguments

Example:
Python run.py / home / -i 300 -e foo@bar.com -s 1000

Note :
I am not responsible for illegal acts you do with this program
