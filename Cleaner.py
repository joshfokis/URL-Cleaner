import re
from Tkinter import *
import tkFileDialog
import os
import tkMessageBox

def main():
    fileOpen = Tk()
    fileOpen.withdraw() #hiding tkinter window
    file_path = tkFileDialog.askopenfilename(
    title="Open file", filetypes=[("txt file",".txt")])   
    file = open(file_path)
    ofile = os.path.dirname(os.path.realpath(file_path))
    sfile = os.path.join(ofile, 'URL_CLEANED.txt')
    fout = open(sfile, 'w')
    domains = set()
    # will works for any web like https://www.domain.com/something/somethingmore
    #... , also without www, without https or just for www.domain.org
    matcher= re.compile("(h..ps?://)?(?P<domain>(www\.)?[^/]*)/?.*") 

    for line in file:
        line = (line.replace('[.]', '.')
                .replace('[dot]', '.')
                .replace('hxxp://www.', '')
                .replace('hxxps://www.', '')
                .replace('wxw.', '')
                .replace('hxxps://', '')
                .replace('hxxp://', '')
                .replace('www.', '')
                .replace(' ', '')
                .replace('http://www.', '')
                .replace('https://www.', '')
                .replace('https://', '')
                .replace('http://', ''))
        if line[-1] == '\n': # remove "\n" from end of line if present
            line = line[0:-1]
        match = matcher.search(line)
        if match != None: # If a url has been found
            domains.add(match.group('domain'))
    for lines in sorted(domains):
        fout.writelines(re.sub(r':.*', '', lines) + '\n')
    file.close()
    fout.close()
    tkMessageBox.showinfo(message='    The URLS have been cleaned and the finished file was saved to \n\n\t' + ofile + '\\URL_CLEANED.txt')
main()
