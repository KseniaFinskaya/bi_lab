import argparse
import codecs
import csv
from ftplib import FTP
import gzip
import re
import shutil
# import json
# import yaml


parser = argparse.ArgumentParser()
parser.add_argument('--url', help='Input url to load file', action='store',
                    default='ftp.fu-berlin.de/pub/misc/movies/database'
                            '/frozendata/ratings.list.gz')
parser.add_argument('--format', nargs='?',
                    help='Choose store format: json, xml, csv, yaml')
args = parser.parse_args()

url = args.url
store_format = args.format
print(url)
site = url.split('/')[0]
localfile = url.split('/')[-1]
filename = re.match(r'^([\w]+.[\w]+)', localfile).group()
subdir = re.findall(r'/\S+/', url)[0]
fname = re.match(r'([\w]+)', filename).group()

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

f = codecs.open(filename, 'rb', 'cp1252')
str_in = f.readlines()
p = []
for index in range(0, len(str_in)):
    datalist = str_in[index].split('  ')
    p.append(datalist)

if store_format == 'csv':
    csv_out = csv.writer(open(fname + '.csv', 'w'), lineterminator=',')
    for row in p:
        csv_out.writerow(row)
# if store_format == 'json':
#    with open(fname + '.json', 'wb') as js_out:
#        json.dump(p, js_out)
# if store_format == 'yaml':
#    with open(fname + 'yml', 'wb') as y_out:
#        yaml.dump(p, y_out)
