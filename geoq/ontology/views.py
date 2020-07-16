from django.http import HttpResponse, JsonResponse
import requests

def semanticQueryInfo(request):
    if request.method == 'GET':
        #semanticURL
        semanticURL = "http://dummy.restapiexample.com/api/v1/employees"
        #relevant param
        #parameters = {"holder": 32}
        response = requests.get(url = semanticURL)
        data = response.json()
        return JsonResponse(data)

    else:
        return HttpResponse("Request method is not a GET")


def predicateQueryInfo(request)
    if request.method == 'GET':
        #semanticURL
        semanticURL = "holderstring"
        #relevant param
        parameters = {"holder": 32}
        response = requests.get(url = semanticURL, params = parameters)
        data = response.json()
        return JsonResponse(data)

    else:
        return HttpResponse("Request method is not a GET")