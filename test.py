from it4u_http_request import HttpRequest, Url, default_cache_key_calculator, proxies
from reactivex import operators as ops
import re

import logging
logging.basicConfig(level=logging.INFO)

import socket
import requests
requests.packages.urllib3.util.connection.HAS_IPV6 = False
    
if __name__ == '__main__':
    request = HttpRequest(cache_key_calculator=default_cache_key_calculator)
    urls = ['https://masothue.com/1201670888-cong-ty-tnhh-mtv-dung-lien',
            'https://masothue.com/0317690352-cong-ty-tnhh-thuong-mai-va-dich-vu-sm-group',
            'https://masothue.com/0317690666-cong-ty-tnhh-thuong-mai-xe-may-nhap-khau-duy-hung',
            'https://masothue.com/0317690987-cong-ty-tnhh-phan-long-laser',
            'https://masothue.com/0317689237-cong-ty-tnhh-phan-mem-thuan-phat',
            'https://masothue.com/0317689068-cong-ty-tnhh-coolera',
            'https://masothue.com/0110256660-cong-ty-tnhh-tm-va-dv-cong-nghe-phuong-anh',
            'https://masothue.com/0110256646-cong-ty-tnhh-suneva-viet-nam',
            'https://masothue.com/0110256639-cong-ty-tnhh-thuong-mai-dich-vu-an-phong-khanh',
            'https://masothue.com/0317691518-cong-ty-tnhh-mimisa-beauty-226-clinic']

    for url in urls:
        request.get_response_stream(Url(url), pipes=[
            ops.do_action(lambda res: print(re.search(r'<title>(.+)<\/title>', res).group(1)))
        ])

    request.get_response_stream(Url("https://ipconfig.io"), pipes=[
            ops.do_action(print)
        ], headers={'Accept': 'application/json'}, proxy_builder=lambda: proxies[1])