import requests
from core.rest_client import RestClient


class ApiUtil(RestClient):
    def __init__(self):
        super().__init__()

    def post_login(self, **kwargs):
        r = self.post("/jsp/admin/login/doLogin.jsp", **kwargs)
        return r
