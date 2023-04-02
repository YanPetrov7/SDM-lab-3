from fastapi import APIRouter

router = APIRouter()


@router.get('')
def hello_world() -> dict:
    return {
        'msg': 'Hello, World!',
        'name': 'Yan',
        'surname': 'Petrov',
        'height': '190',
        'weight': '80'
        }