# -*- coding: utf-8 -*-
from utils.read import base_data
import pytest
import requests
import math
import sys


def test_accoult():
    ini = base_data.read_ini()
    print("*******")
    print(ini)
    # sys.stdout.flush()
    params = base_data.read_data()
    # for p in params:
    #     print(p)
    r = requests.get(ini['host']['api_test_url'] + "/jsp/admin/login/doLogin.jsp",
                     params['login_user']['person1'])  # x-www-form如何传
    # print(r.json())


if __name__ == '__main__':
    test_accoult()
