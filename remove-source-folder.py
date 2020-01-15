import os, shutil


targetFolder = r'G:\My Drive\Clients\AAAS\sample content\without source- entire issue\science.2019.365.issue-6460'
os.chdir(targetFolder)
folderList  = [item for item in os.listdir(targetFolder)]
for folder in folderList:
    insideList = [item for item in os.listdir(folder)]
    for item in insideList:
        if item == 'source':
            print('deleting: '+ folder+ '/'+ item)
            shutil.rmtree(folder + '/' + item)


