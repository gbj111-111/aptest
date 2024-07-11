from core.api_utils import ApiUtil


def login(params):
    au = ApiUtil()
    r = au.post_login(params=params)
    return r
    result = process_response(response)
