import os
import time
import datetime
import smtplib
import sys


class XFileBlameMa:

    rootDirectory = ''
    timetw = ''
    oldFiles = []
    files_found = []
    results = ''
    emailContact = ''
    suspiciousSize = 350000
    fileExtensions = []
    extensionType = 1
    timesChecked = 0
    errorAccorded = False

    smtpServer = 'mail.yourprovider.net'
    smtpport = 587
    loginEmail = 'foo@bar.com'
    loginPassword = 'yourpassword!!'

    def __init__(self, rootDirectory, timetw, emailContact, suspiciousSize,extensionType):
        self.rootDirectory = rootDirectory
        self.timetw = timetw
        self.extensionType = extensionType
        self.emailContact = emailContact
        self.suspiciousSize = int(suspiciousSize) * 1000000
        if extensionType == 1:
            self.fileExtensions = ['.mp4', '.avi', '.mkv', '.wmv', '.ts']
        elif extensionType == 2:
            self.fileExtensions = ['.exe', '.bat', '.vbs', '.reg', '.vb']
        elif extensionType == 3:
            self.fileExtensions = ['.mp4', '.avi', '.mkv', '.wmv', '.ts', '.exe', '.bat', '.vbs', '.reg', '.vb']


    def blameFiles(self):
        print('looking for files in with extension: ' + str(tuple(self.fileExtensions)) + 'in ' + self.rootDirectory + ' time: ' + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))
        try:
            for dirpath, dirnames, files in os.walk(self.rootDirectory):  # goes to every directory in the given location and checks for searched files
                for f in files:
                    if os.path.join(dirpath, f) in self.oldFiles:
                        pass
                    else:
                        change = False
                        filePath = os.path.join(dirpath, f)
                        try:
                            if os.path.getsize(filePath) > self.suspiciousSize:
                                if not self.extensionType == 4:
                                    if f.endswith(tuple(self.fileExtensions)):
                                        change = True
                                else:
                                    change = True
                            if change:  # prints live output of found files and adds them to result
                                self.files_found.append(filePath)
                                erg = (str(filePath) + ' ' + str(os.path.getsize(filePath) >> 20) + 'mb')
                                print('file found: ' + erg)
                                self.results += erg + '\n'
                        except Exception:
                            pass    # e.g. Files to which the user has no right to check the size are omitted
        except Exception:
            print('An Error accorded in search number: ' + str(self.timesChecked))
            if not self.errorAccorded:
                self.errorAccorded = True
                self.sendEmail('An Error accorded in search number: ' + str(self.timesChecked), 'Error in XFileBlame while searching')

        self.timesChecked += 1
        if not self.files_found:  # then no file was found
            self.blameAgain()
        else:
            self.oldFiles.extend(self.files_found)
            self.files_found = []
            self.sendEmail(self.results, 'XFileBlame has found new searched files')

    def blameAgain(self):
        if self.timetw != '':  # checks if a search should be repeat
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
        except Exception:
            print('failed to send Email')
        self.blameAgain()
