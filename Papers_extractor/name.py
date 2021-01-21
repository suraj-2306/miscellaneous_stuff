#! /usr/bin/python3
from pdfrw import PdfReader
import argparse
import os

def renameFileToPDFTitle(path, fileName):
    fullName = os.path.join(path, fileName)
    # Extract pdf title from pdf file
    newName = PdfReader(fullName).Info.Title
    
    # Remove surrounding brackets that some pdf titles have
    # Some papers have / in their titles so I've replaced / with a space
    newName = newName.replace('/',' ')
    newName = newName.strip('()') + '.pdf'

    newFullName = os.path.join(path, newName)
    os.rename(fullName, newFullName)

def main():


    parser = argparse.ArgumentParser(description='Renamer')
    parser.add_argument('-o','--output',help='path to save pdf',type=str)
    args = parser.parse_args()
    global path
    path = args.output 
    for fileName in os.listdir(path):
        # Rename only pdf files
        fullName = os.path.join(path, fileName)
        if ( fileName.find('?rand')>0 or os.path.splitext(fullName)[1] == '.pdf'):
            # ?rand is a special case for IEEE papers dowloads
            try:
                renameFileToPDFTitle(path, fileName)
            except:
                pass
if __name__ == '__main__':
    main()
