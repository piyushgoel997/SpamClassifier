import os


def read_files(path):
    """
    :param path: path of the directory where the files will be searched, recursively.
    :return: dictionary of files{path,int} -> 1 if file is a spam, 0 otherwise.
    """
    files = {}
    for dirPath, dirNames, fileNames in os.walk(path):
        for fileName in [f for f in fileNames if f.endswith(".txt")]:
            if fileName.startswith("spmsga"):
                files[os.path.join(dirPath, fileName)] = 1
            else:
                files[os.path.join(dirPath, fileName)] = 0
    return files
