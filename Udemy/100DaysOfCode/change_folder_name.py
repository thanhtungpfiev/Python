import os


def listdirs(rootdir):
    for it in os.scandir(rootdir):
        if it.is_dir():
            if it.name == "Resources":
                new_path = it.path.replace("Resources", "resources")
                os.rename(it.path, new_path)
            listdirs(it)


rootdir = r'C:\PrivateDocuments\CodingPractices\Python\Udemy\100DaysOfCode'

listdirs(rootdir)
