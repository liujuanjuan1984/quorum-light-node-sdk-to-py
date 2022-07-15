import json
import os
import re
import urllib.parse

groupId = "8136923b-8203-4e08-bfe7-50eb3b558e2c"
privateKey = "0x8ec0b306e7e3358b7c41d46e46d389e5cfb804d45e3e1cc0b51d0f8347b2489a"
cipherKey = "055aee9fb94a7eea86777eb37b383e0443f5d6e7ec990c11894910a47333a44b"

contents = [
    "正常文本",
    "有 空格 的 文本",
    """有
换行
符
的文本""",
]


def get_trxitem(output):

    rlts = re.findall(r"""TrxItem: ['"](.*?)['"]\n""", output)
    if rlts:
        return rlts[0]


for content in contents:
    content = json.dumps(content, ensure_ascii=False)
    cmd = "node createTrxItem.js {0} {1} {2} {3}".format(groupId, privateKey, cipherKey, content)
    nodejs = os.popen(cmd)
    output = nodejs.read()
    nodejs.close()

    item = get_trxitem(output)
    if item:
        item = {"TrxItem": item}
        print(item)
    else:
        print(output)
