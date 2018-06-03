from ftplib import FTP
import gzip
import os.path
import re
import shutil


url = 'ftp.fu-berlin.de/pub/misc/movies/database/frozendata/ratings.list.gz'
site = url.split('/')[0]
print(url)
localfile = url.split('/')[-1]
filename = re.match(r'^([\w]+.[\w]+)', localfile).group()
subdir = re.findall(r'/\S+/', url)[0]
if os.path.exists(localfile):
    print('File is already downloaded.')
else:
    with FTP() as ftp:
        ftp.set_pasv(True)
        ftp.connect(site, timeout=120)
        ftp.login()
        ftp.cwd(subdir)
        with open(localfile, 'wb') as lf:
            ftp.retrbinary('RETR ' + localfile, lf.write)
        with gzip.open(localfile, 'rb') as gfile:
            with open(filename, 'wb') as f_out:
                shutil.copyfileobj(gfile, f_out)
