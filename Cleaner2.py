from Tkinter import *
import tkFileDialog
import re

def main():
        
        fileOpen = Tk()
        fileOpen.withdraw() #hiding tkinter window

        file_path = tkFileDialog.askopenfilename(
        title="Open file", filetypes=[("txt file",".txt")])

        if file_path != "":
            print "you chose file with path:", file_path

        else:
            print "you didn't open anything!"

        fin = open(file_path)
        fout = open("URL Cleaned12.txt", "wt")
        for line in fin.readlines(): 
                editor = (line.replace('[.]', '.')
                .replace('[dot]', '.')
                .replace('hxxp://www.', '')
                .replace('hxxp://', '')
                .replace('www.', '')
                .replace('http://www.', '')
                .replace('http://', ''))
                fout.write(re.sub(r'/.*', '', editor))
                        
if __name__ == '__main__':
        main()
