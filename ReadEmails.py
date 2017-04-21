import os


def read_emails(path):
    emails = []
    for dirPath, dirNames, fileNames in os.walk(path):
        for fileName in [f for f in fileNames if f.endswith(".txt")]:
            if fileName.startswith("spmsga"):
                emails.append(Email(os.path.join(dirPath, fileName), 1))
            else:
                emails.append(Email(os.path.join(dirPath, fileName), 0))
    return emails


class Email:

    def __init__(self, path, is_spam):
        self.path = path
        self.is_spam = is_spam


# emails = read_emails(r"Resources\lingspam_public\bare\part1")
# print(12)
