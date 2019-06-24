# coding:utf-8

import os


def dirlist(path):
    try:
        filelist = os.listdir(path)

        for filename in filelist:
            filepath = os.path.join(path, filename)
            if os.path.isdir(filepath):
                dirlist(filepath)
            else:
                if filename == "_desktop.ini":
                    os.remove(filepath)
                    print filepath, "delete"
    except Exception as e:
        print path
        print repr(e)


win_dir = raw_input("please input clean dir:")
print dirlist(win_dir)
