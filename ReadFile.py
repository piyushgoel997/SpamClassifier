import os


def read_files(path):
    """
    :param path: path of the directory where the files will be searched, recursively.
    :return: dictionary of files{path,boolean} -> True if file is a spam, False otherwise.
    """
    files = {}
    for dirPath, dirNames, fileNames in os.walk(path):
        for fileName in [f for f in fileNames if f.endswith(".txt")]:
            if fileName.startswith("spmsga"):
                files[os.path.join(dirPath, fileName)] = True
            else:
                files[os.path.join(dirPath, fileName)] = False
    return files
