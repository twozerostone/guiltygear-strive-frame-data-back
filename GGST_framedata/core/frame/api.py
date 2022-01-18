from ninja import Router

router = Router()


@router.get('/')
def hello_world(request):
    return {
        "message": "hello world"
    }
