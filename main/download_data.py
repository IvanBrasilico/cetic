import os
import requests
import zipfile
from tqdm import tqdm

BASE_URL = 'http://cetic.br/media/microdados/%s/'

DATA = 'ticdom_%s_domicilios_tabelas_ods_v1.0.zip'

urls = ['http://cetic.br/media/microdados/73/ticdom_2015_domicilios_individuos_tabelas_ods.zip',
        'http://cetic.br/media/microdados/130/ticdom_2016_domicilios_individuos_tabelas_ods_v1.1.zip']


def get_with_progress_bar(url):
    destname = os.path.join('.', 'bases', url.split('/')[-1])
    if os.path.exists(destname):
        print(f'Arquivo existente: {destname}')
        return False
    response = requests.get(url, stream=True)
    if response.status_code == 404:
        print(f'NÃO ENCONTROU {url}')
        return False
    print(f'Fazendo download de {url}')
    with open(destname, "wb") as handle:
        for data in tqdm(response.iter_content()):
            handle.write(data)
    return True

def unzip_all():
    for zip_ in os.listdir('bases'):
        zip_file = os.path.join('bases', zip_)
        if zipfile.is_zipfile(zip_file):
            print(zip_file)
            with zipfile.ZipFile(zip_file) as item:
                item.extractall(zip_file[:-4])


def do_downloads():
    for url in urls:
        get_with_progress_bar(url)
    anos = [2017, 2018]
    caminhos = [139, 208]
    for caminho, ano in zip(caminhos, anos):
        url = BASE_URL % caminho + DATA % ano
        get_with_progress_bar(url)
    unzip_all()

if __name__ == '__main__':
    do_downloads()

