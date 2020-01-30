import os

mcounter = 193
vcounter = 278

def rename(counter, src):
    if counter < 1000:
        if counter < 100:
            if counter < 10:
                dst = dirpath + "01-000" + str(counter) + ".wav"
            dst = dirpath + "01-00" + str(counter) + ".wav"
        dst = dirpath + "01-0" + str(counter) + ".wav"
        os.rename(src, dst)

for (dirpath, dirnames, filenames) in os.walk("positief/"):
    for file_name in filenames:
        src = dirpath + file_name
        # if int(file_name[18:-4]) % 2 == 1:
        rename(mcounter, src)
        mcounter+=2
        # else:
        #     rename(vcounter,src)
        #     vcounter+=2
