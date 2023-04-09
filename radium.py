import logging
import os
import asyncio
import hashlib


logging.basicConfig(level=logging.INFO, filename='py_log.log', filemode='w')


# загружает файлы с github


async def download():
    if os.path.exists(r'D:\Temp\project-configuration'):
        print('папка скачана')
    else:
        url ='https://gitea.radium.group/radium/project-configuration.git'
        cmd = f'git clone {url}'
        os.system(cmd)
    return 0             

# создает дирректрию если не существует


async def go_to_temp():
    path = r'D:\Temp'
    if os.path.exists(path):
        os.chdir(path)
    else:
        os.mkdir(path)

    return 0
 

# считает хэш сумму файлов


def hash(name):
    path = r'D:\Temp'
    os.chdir(path)
    for root, dirs, files in os.walk(path):
        for names in files:
            names = os.path.join(root, names)
            names = hashlib.sha256(open(names, 'rb').read()).hexdigest()
            name.append(names)
    return name

# вывод хэшей


def print_hash(name):
    for hash in name:
        print(hash)


async def go():
    await go_to_temp()
    await download()

asyncio.run(go())
name = []
hash(name)
print_hash(name)
