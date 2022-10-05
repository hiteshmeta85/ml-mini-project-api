import wget,os
from config import basepath

ids = ['1IJBNMt2pGmDxTq2e64rpzDjaz4aAauL7']

download_folder = os.path.join(basepath, 'models')

for id in ids:
    os.system(f'gdown {id} -O {download_folder} --folder')
    
print("\nDownloaded all models")
