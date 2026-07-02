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
            "success": True,
            "message": message,
            "data": data,
        },
        status=status_code,
    )