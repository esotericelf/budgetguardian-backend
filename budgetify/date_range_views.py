from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .firebase import db
from datetime import datetime

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_category_sums_by_date_range(request, uid):
    try:
        start_date_str = request.query_params.get('start_date')
        end_date_str = request.query_params.get('end_date')

        if not start_date_str or not end_date_str:
            return Response({'error': 'Start date and end date are required'}, status=status.HTTP_400_BAD_REQUEST)

        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

        user_ref = db.collection('users').document(uid)
        user_doc = user_ref.get()

        if not user_doc.exists:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        user_data = user_doc.to_dict()
        expenses = user_data.get('expenses', [])

        # Filter expenses by date range and calculate sum of amounts by category
        category_sums = {}
        for expense in expenses:
            expense_date = datetime.strptime(expense.get('date'), '%Y-%m-%d')
            if start_date <= expense_date <= end_date:
                category = expense.get('category')
                amount = expense.get('amount', 0)
                if category in category_sums:
                    category_sums[category] += amount
                else:
                    category_sums[category] = amount

        return Response({'category_sums': category_sums}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)