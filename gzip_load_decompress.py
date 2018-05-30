from ftplib import FTP
import gzip
import shutil


with FTP() as ftp:
    ftp.set_pasv(True)
    ftp.connect('ftp.fu-berlin.de', timeout=120)
    ftp.login()
    ftp.cwd('/pub/misc/movies/database/frozendata/')
    filename = 'ratings.list.gz'
    with open(filename, 'wb') as lf:
        ftp.retrbinary('RETR ' + filename, lf.write)
        with gzip.open(filename, 'rb') as gfile:
            with open('ratings.list', 'wb') as f_out:
                shutil.copyfileobj(gfile, f_out)
