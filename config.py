import json
from typing import List

from utils import fail


class Config:
    def __init__(self):
        self.username = '33620211153775'
        self.password = 'gege602255925!!!'
        self.password_vpn = 'gege602255925!!!'
        self.email = '602255925@qq.com'
        self.district = '思明区'
        self.inschool = '在校'
        self.campus = '思明校区'
        self.building = '思明海韵16'
        self.room = '0307'


def make_configs(json_str: str) -> List[Config]:
    try:
        dicts = json.loads(json_str)["config"]
        cfgs = []
        for d in dicts:
            c = Config()
            for key in c.__dict__.keys():
                setattr(c, key, d[key])
            cfgs.append(c)
        return cfgs
    except Exception as e:
        print(json_str)
        fail("配置读取失败，请检查配置", "配置错误", e=e, shutdown=True)
