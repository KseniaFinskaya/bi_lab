import argparse
import certifi
import os.path
import urllib.request as urlrq


parser = argparse.ArgumentParser()
parser.add_argument('--input', action='store',
                    default='https://www.kaggle.com'
                    '/PromptCloudHQ/imdb-data/downloads/'
                            'imdb-data-from-2006-to-2016.zip')
args = parser.parse_args()

url = args.input
print(url)
localfile = url.split('/')[-1]

if os.path.exists(localfile):
    print('File is already downloaded.')
else:
    source = urlrq.urlopen(url, cafile=certifi.where())
    outputfile = open(localfile, 'wb')
    outputfile.write = (source.read())
    outputfile.close()