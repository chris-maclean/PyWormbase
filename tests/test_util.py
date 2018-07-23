def is_dict(obj):
    return type(obj) is dict

def is_status_200(res):
    return res.get('status_code', 0) == 200