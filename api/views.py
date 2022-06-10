from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_Data(request):
    book = {'title':'boook1', 'author':'routput', 'course':'test_course','some_Stuff':'stuff'}
    return Response(book)