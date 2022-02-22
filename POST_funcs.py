import GET_funcs as get
# 1 - Kullanıcının istedigi path olusturulur ve gorseller o path uzerine olusturulur.
#                           gorsel ismi, turu onceden kullanici tarafindan belirlenmis olur.

def changeSettings(params):
    oldPath = get.fullPath
    get.fullPath = params['newPath'];
    get.imgName = params['imgName'];
    get.imgType = params['imgType'];
    dict = {'oldPath':oldPath, 'newPath':get.fullPath, 'imgName':get.imgName, 'imgType':get.imgType}
    return dict

