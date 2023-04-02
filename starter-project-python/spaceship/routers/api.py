from fastapi import APIRouter
import numpy as numpy

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

@router.get('/matrix')
def matrix() -> dict:
    matrix_a = numpy.random.rand(10, 10)
    matrix_b = numpy.random.rand(10, 10)
    
    product = numpy.dot(matrix_a, matrix_b)

    return {
        "matrix A": matrix_a.tolist(),
        "matrix B": matrix_b.tolist(),
        "result": product.tolist()
    }