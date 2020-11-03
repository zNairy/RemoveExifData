# coding: utf-8

__author__ = 'zNairy'
__contact__ = '__Nairy__#7181 or https://www.github.com/zNairy/'
__version__ = ''

from exif import Image
from pathlib import Path
from termcolor import colored
from os.path import splitext
from json import dumps

def openFile(path):
    with open(path, 'rb') as file:
        tmṕ = Image(file)
        file.close()
        return tmṕ

def showMetaData(namefile, file):
    log = {"name file": namefile}
    if file.has_exif:
        for tag in dir(file):
            try:
                print(f' {tag}: {colored(file.__getitem__(tag), "red")}')
                log.update({tag: str(file.__getitem__(tag))})
            except Exception:
                pass

        return log

def saveDataLog(namefile, log):
    with open(f'{namefile}.json', 'w') as file:
        file.write(dumps(log))
        file.close()

def main(path):
    namefile = lambda p: splitext(p)[0].split('/')[len(splitext(p)[0].split('/'))-1]
    acceptedExtensions = ['.jpeg', '.jpg', '.png']
    if Path(path).is_file() and splitext(path)[1] in acceptedExtensions:
        saveDataLog(namefile(path), showMetaData(namefile(path), openFile(path)))

if __name__ == '__main__':
    main('your path of photo')