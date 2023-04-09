import pytest
from  radium import *
import requests

#создает дирректрию если не существует
def test_go_to_temp():
    path = r'D:\Temp'
    result= os.path.exists(r'D:\Temp\project-configuration')
    assert path == r'D:\Temp'
    assert  result == True

def test_type_error_go_to_temp():
    with pytest.raises(TypeError):
        path = 5
    assert path == str(path)


#загружает файлы с github
def test_dowland():
    path=os.path.exists(r'D:\Temp\project-configuration')
    url ='https://gitea.radium.group/radium/project-configuration.git'
    cmd = f'git clone {url}'
    os.system(cmd)
    assert path==True
    assert url==str(url)
    assert os.path.exists(r'D:\Temp\project-configuration')!=''

# считает хэш сумму файлов   
def test_hush():
    
   
    path = r'D:\Temp'
    
    for root, dirs, files in os.walk(path):
        for name in files:
            name = os.path.join(root, name)
            print(hashlib.md5(open(name, 'rb').read()).hexdigest())
    assert os.walk(path) == tuple(os.walk(path))
    assert hash(name) == type([])

if __name__ == "__main__":
    pytest.main()