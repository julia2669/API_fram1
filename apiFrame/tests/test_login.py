import  pytest
from base.method import Requests
from utils.operationYaml import OperationYaml
import  json

obj=Requests()
objYaml=OperationYaml()

@pytest.mark.parametrize('datas',objYaml.readYaml())
def test_login(datas):
	r=obj.post(
		url=datas['url'],
		json=datas['data'])
	assert  datas['expect'] in json.dumps(r.json(),ensure_ascii=False)

if __name__ == '__main__':
    pytest.main(["-s","-v","test_login.py"])