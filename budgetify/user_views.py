from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .firebase import db

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_data(request, uid):
    try:
        user_ref = db.collection('users').document(uid)
        user_doc = user_ref.get()

        if not user_doc.exists:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        return Response(user_doc.to_dict(), status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)