import urllib.request
import json
import auth
import ogg_items

data = ogg_items.data.short_speech

params = "&".join([
    "topic=general",
    "folderId=%s" % auth.FOLDER_ID,
    "lang=ru-RU"
])

url = urllib.request.Request("https://stt.api.cloud.yandex.net/speech/v1/stt:recognize?%s" % params, data=data)
url.add_header("Authorization", "Bearer %s" % auth.IAM_TOKEN)

responseData = urllib.request.urlopen(url).read().decode('UTF-8')
decodedData = json.loads(responseData)

if decodedData.get("error_code") is None:
    print(decodedData.get("result"))
