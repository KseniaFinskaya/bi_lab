import argparse
import urllib.request as urlrq
import certifi
import os.path


parser = argparse.ArgumentParser()


parser.add_argument('--input', action='store',
                    default='https://www.kaggle.com/PromptCloudHQ/imdb-data/downloads/'
                            'imdb-data-from-2006-to-2016.zip')


args = parser.parse_args()
url = args.input

print(url)
localfile = url.split('/')[-1]
file_ext = url.split('.')[-1]


if file_ext not in ('json', 'csv', 'xml', 'yaml'):
    raise argparse.ArgumentTypeError('Don\'t support this file extension')


if os.path.exists(localfile):
    print('File is already downloaded.')
else:
    source = urlrq.urlopen(url, cafile=certifi.where())
    outputfile = open(localfile, 'wb')
    outputfile.write = (source.read())
    outputfile.close()
