#!/usr/bin/env python
import sys;
import os;

def GetPathSize(strPath):
    if not os.path.exists(strPath):
        return 0;

    if os.path.isfile(strPath):
        return os.path.getsize(strPath);

    nTotalSize = 0;
    for strRoot, lsDir, lsFiles in os.walk(strPath):
        #get child directory size
        for strDir in lsDir:
            nTotalSize = nTotalSize + GetPathSize(os.path.join(strRoot, strDir));

        #for child file size
        for strFile in lsFiles:
            nTotalSize = nTotalSize + os.path.getsize(os.path.join(strRoot, strFile));

    return nTotalSize/1024.0/1024.0/1024.0;

if __name__ == '__main__':
    # nFileSize = GetPathSize(sys.argv[1])
    nFileSize = GetPathSize('C:\Users\wangchao\AppData\Local')
    print(nFileSize);