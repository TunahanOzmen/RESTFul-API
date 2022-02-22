import GET_funcs as get
import POST_funcs as post
import json

#url ile gelen sorguyu dict haline getirir
def jsonToDict(query):
    attributes = query.split("&")
    dict = {}
    attributes[0] = attributes[0].replace("?", "").replace("/", "");
    for attr in attributes:
        key, value = attr.split("=")
        dict[key] = value
    return dict

#bu iki fonksiyon : istenen fonksiyona dogru formatta veri gonderilmesini, gelen verinin response formatini almasini saglar
def handleGetRequests(headers):
    query = headers[0].split()[1]
    dict = jsonToDict(query)
    classMethod = getattr(get, dict['func'])
    dict = classMethod(dict)
    jsonData = json.dumps(dict, indent=4, ensure_ascii=False)
    return jsonData

def handlePostRequests(headers):
    query = headers[0].split()[1]
    dict = jsonToDict(query)
    classMethod = getattr(post, dict['func'])
    dict = classMethod(dict)
    jsonData = json.dumps(dict, indent=4, ensure_ascii=False)
    return jsonData