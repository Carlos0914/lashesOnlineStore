def getQueryAttribute(request, key):
    if key in request.GET:
        return request.GET[key]
    return ""        