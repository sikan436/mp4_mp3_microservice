import os, requests


def login(request):
    print ("inside access file login method")
    auth = request.authorization
    if not auth:
        return None, ("missing credentials", 401)

    basicAuth = (auth.username, auth.password)
    print (auth.username,auth.password)
    print("###########")
    print("###########")
    print(f"http://{os.environ.get('AUTH_SVC_ADDRESS')}/login")
    response = requests.post(
        f"http://{os.environ.get('AUTH_SVC_ADDRESS')}/login", auth=basicAuth
    )

    if response.status_code == 200:
        return response.text, None
    else:
        return None, (response.text, response.status_code)

# import os,requests
# def login(request):
#     auth=request.authorization
#     if not auth:
#         return None,("missing credentials",401)
    
#     basicauth=(auth.username,auth.password)
#     response=requests.post(
#         f"http://{os.environ.get('AUTH_SVC_ADDRESS')}/login",
#         auth=basicauth
#     )

#     if response.status_code == 200:
#         return response.text, None
#     else:
#         return(response.text,response.status_code)
