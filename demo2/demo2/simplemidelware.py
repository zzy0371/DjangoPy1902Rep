"""
自定义中间件
    演示中间件如何改变请求，响应

"""

class SimpleMiddleWare():
    def __init__(self, _get_response):
        self.get_response = _get_response

    def __call__(self, request):
        print("截取到的请求",request)
        request.path = "/polls/login/"
        print("更改过的请求", request)
        response = self.get_response(request)
        from django.http import HttpResponse
        print("截取响应",response)
        # return response
        return HttpResponse("处理过的响应")

    def process_view(self,request, view_func, view_args, view_kwargs):
        print(request, view_func, view_args, view_kwargs, '视图信息')

