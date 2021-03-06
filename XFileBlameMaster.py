import os
import time
import datetime
import smtplib
import sys


class XFileBlameMa:

    oldFiles = []
    files_found = []
    fileExtensions = []
    results = ''
    timesChecked = 0
    errorAccorded = False

    smtpServer = 'mail.yourprovider.net'
    smtpport = 587
    loginEmail = 'foo@bar.com'
    loginPassword = 'yourpassword!!'

    def __init__(self, rootDirectory='/', timetw='', emailContact='', suspiciousSize=0, extensionType=1, outputLevel=1, useExtension = False):
        self.rootDirectory = rootDirectory
        self.timetw = timetw
        self.extensionType = extensionType
        self.emailContact = emailContact
        self.suspiciousSize = int(suspiciousSize) * 1000000
        self.outputLevel = int(outputLevel)
        self.useExtension = useExtension
        if extensionType == 1:
            self.fileExtensions = ['.mp4', '.avi', '.mkv', '.wmv', '.ts', '.mpeg', '.flv', '.svi', '.mov']
        elif extensionType == 2:
            self.fileExtensions = ['.exe', '.bat', '.vbs', '.reg', '.vb', '.jar', '.pif', '.msi', '.com', '.cmd', '.ws', '.vbe']
        elif extensionType == 3:
            self.fileExtensions = ['.mp4', '.avi', '.mkv', '.wmv', '.ts', '.mpeg', '.flv', '.svi', '.mov', '.exe', '.bat', '.vbs', '.reg', '.vb', '.jar', '.pif', '.msi', '.com', '.cmd', '.ws', '.vbe']


    def blameFiles(self):
        if self.outputLevel >= 1:  # 0=only errors / 1=0+minimum output(search begin,end,results) / 2=all output
            print('looking for files in with extension: ' + str(tuple(self.fileExtensions)) + 'in ' + self.rootDirectory + ' time: ' + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        try:  # begin of the search itself
            for dirpath, dirnames, files in os.walk(self.rootDirectory):  # goes to every directory in the given location and checks for searched files
                for f in files:
                    filepath = os.path.join(dirpath, f)
                    if filepath in self.oldFiles:
                        pass
                    else:
                        change = False
                        if self.outputLevel >= 2:
                            print('checking directory: ' + str(filepath)[:35], end="\r"),
                        try:
                            if os.path.getsize(filepath) > self.suspiciousSize:
                                if not self.extensionType == 4:
                                    if f.endswith(tuple(self.fileExtensions)):
                                        change = True
                                else:
                                    change = True
                        except Exception:  # e.g. Files to which the user has no right to check the size are omitted
                            pass
                        if change:  # prints live output of found files and adds them to result
                            self.files_found.append(filepath)
                            erg = (str(filepath) + ' ' + str(os.path.getsize(filepath) >> 20) + 'mb')
                            if self.outputLevel >= 2:
                                print('file found: ' + erg)
                            self.results += erg + '\n'

        except Exception as error:  # handel's errors in search
            print('An Error accorded in search number: ' + str(self.timesChecked) + ' : ' + str(error))
            if not self.errorAccorded:
                self.errorAccorded = True
                if self.useExtension:  # extensions have to decide if they send mails themselves
                    return 'error'
                else:
                    self.sendEmail('An Error accorded in search number: ' + str(self.timesChecked) + ' : ' + str(error), 'Error in XFileBlame while searching')

        if self.outputLevel >= 1:
            print(' '*56, end="\r")  # to protect the following from output of level2
            print('Search finished ' + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            print('results: \n' + self.results)

        if self.useExtension:
            return self.files_found
        else:
            if not self.files_found:  # then no file was found
                self.blameAgain()
            else:
                self.oldFiles.extend(self.files_found)
                self.files_found = []
                self.sendEmail(self.results, 'XFileBlame has found new searched files')

    def blameAgain(self):
        if self.timetw != '':  # checks if a search should be repeated
            if self.timesChecked >= (43200/int(self.timetw)):  # clears the known list of files (oldfiles) every 30 days
                self.timesChecked = 0
                self.oldFiles = []
                self.results = ''
                self.errorAccorded = False  # if an error accorded the admin gets reminded
            time.sleep(int(self.timetw))
            self.blameFiles()
        else:
            sys.exit(0)

    def sendEmail(self, message, title):
        try:
            if self.emailContact != '':
                if not self.smtpServer == '' or self.smtpport == 0 or self.loginEmail == '' or self.loginPassword == '':
                    server = smtplib.SMTP(self.smtpServer, self.smtpport)
                    server.starttls()
                    server.login(self.loginEmail, self.loginPassword)
                    msg = 'Subject: {}\n\n{}'.format(title, title + ': \n' + message)
                    server.sendmail(self.loginEmail, str(self.emailContact), msg)
                    server.quit()
                else:
                    print('The given E-Mail credentials are incomplete')
                    sys.exit(0)
            else:
                self.blameAgain()
        except Exception as error:
            print('failed to send Email ' + str(error))
        if not self.useExtension:
            self.blameAgain()
