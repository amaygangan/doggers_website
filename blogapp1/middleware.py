def blogapp1_middleware(get_response):
    print("blogapp1_middleware is executed when the server runs")
    print("Code needs to be executed only once for initialization")

    def my_middleware(request):
        print("Hello before view function is called")
        res=get_response(request)
        print(res)

        print("hello from middleware after view function is been executed")

        return res
    
    
    return my_middleware
    