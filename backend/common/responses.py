from django.http import JsonResponse

def success_response(data=None, message="Success", status_code=200):
    return JsonResponse(
        {
            "success": True,
            "message": message,
            "data": data,
        },
        status=status_code,
    )
    
def unavailable_response(data=None, message="Service currently unavailable, please try later", status_code=503):
    return JsonResponse(
        {
            "success": False,
            "message": message,
            "data": data,
        },
        status=status_code,
    )
    
def unauthorized_response(data=None, message="It isn't possible to verify your identity, please log in or contact support", status_code=401):
    return JsonResponse(
        {
            "success": False,
            "message": message,
            "data": data,
        },
        status=status_code,
    )
    
def forbidden_response(data=None, message="You don't have authorization to access this resource", status_code=403):
    return JsonResponse(
        {
            "success": False,
            "message": message,
            "data": data,
        },
        status=status_code,
    )