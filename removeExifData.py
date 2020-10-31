# coding: utf-8

__author__ = 'zNairy'
__contact__ = '__Nairy__#7181 or https://www.github.com/zNairy/'
__version__ = ''

from exif import Image
from pathlib import Path
from os import listdir, system, uname
from os.path import splitext
from termcolor import colored

class Exif(object):
    def __init__(self, path):
        self.path = path
        self.filesModified = 0
        self.unansweredFiles = 0
        self.total = 0
        self.acceptedExtensions = ['.png', '.jpg', '.jpeg']
        self.clearCommand = {'Linux': 'clear','Windows': 'cls'}

    def ListFiles(self):
        if(Path(self.path).is_dir()):
            return [file for file in listdir(self.path) if Path(f'{self.path}/{file}').is_file() and splitext(file)[1] in self.acceptedExtensions]
        else:
            print(colored(f' Error, {self.path} is not a dir, please pass a dir for listing files.', 'red'))
            exit()

    def RemoveMetaData(self):
        for file in self.ListFiles():
            self.total += 1
            system(self.clearCommand[uname()[0]])
            print(colored(' {*} Checking the file and getting exif data from ['+file+']', 'yellow'))
            data = self.GetExifData(file)
            if(data):
                data.delete_all()
                self.SaveNewFile(file, data)

        print(colored(f' {self.filesModified} files have been modified | {self.unansweredFiles} unanswered files | {self.total} files read.', 'green'))

    def GetExifData(self, file):
        with open(f'{self.path}/{file}', 'rb') as file:
            try:
                tmp = Image(file)
                file.close()

                if tmp.has_exif:
                    return tmp
            
            except Exception:
                self.unansweredFiles += 1
                return False

    def SaveNewFile(self, name, newfile):
        self.filesModified += 1
        with open(f'{self.path}/{name}', 'wb') as file:
            file.write(newfile.get_file())
            file.close()


if __name__ == '__main__':
    arquivos = Exif('your path of photos')
    arquivos.RemoveMetaData()
