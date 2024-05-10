import os,requests
def login(request):
    auth=request.authorization
    if not auth:
        return None,("missing credentials",401)
    
    basicauth=(auth.username,auth.password)
    response=requests.post(
        f"http://{os.environ.get('AUTH_SVC_ADDRESS')}/login",
        auth=basicauth
    )

    if response.status_code == 200:
        return response.txt, None
    else:
        return(response.text,response.status_code)
