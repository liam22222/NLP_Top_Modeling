import urllib.request
import json
import auth
import ogg_items

data = ogg_items.data.short_speech

defaultParams = {
    topic: "general",
    lang: "ru-RU"
}

with open("short_speech.ogg", "rb") as f:
    short_speech = f.read()


def short_stt(params, speechFile):
    urlFormatParams = "&".join([
        "topic=" + params.topic,
        "folderId=%s" % auth.FOLDER_ID,
        "lang=" + params.lang
    ])

    url = urllib.request.Request("https://stt.api.cloud.yandex.net/speech/v1/stt:recognize?%s" % urlFormatParams,
                                 data=speechFile)
    url.add_header("Authorization", "Bearer %s" % auth.IAM_TOKEN)

    responseData = urllib.request.urlopen(url).read().decode('UTF-8')
    decodedData = json.loads(responseData)

    if decodedData.get("error_code") is None:
        print(decodedData.get("result"))



