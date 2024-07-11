from api  import api
from utils.read import base_data

iniconfig = base_data.read_ini()


def test_login():
    params = base_data.read_data()['login_user']['person1']
    r = api.login(params)
    print(r)
