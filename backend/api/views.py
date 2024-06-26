import csv
from django.db.models import Q
from io import TextIOWrapper
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.views import APIView
from .models import Company, Employee, RoleHistory
from .serializers import CompanySerializer, EmployeeSerializer, RoleHistorySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def bulk_put(self, request):
        file = request.FILES.get('file')

        if not file:
            return Response({'error': 'File not provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Assuming CSV file format
            decoded_file = TextIOWrapper(file, encoding='utf-8')
            reader = csv.reader(decoded_file)

            next(reader)  # Skip header row if exists
            for row in reader:
                employee_id = row[0]
                name = row[1]
                department = row[2]

                try:
                    employee = Employee.objects.get(pk=employee_id)
                    request.data = {'name': name, 'department': department}  # Prepare data for individual update
                    response = self.put(request, pk=employee_id)  # Call default put() method
                    if response.status_code != status.HTTP_200_OK:
                        return response  # Return response immediately if update fails
                except Employee.DoesNotExist:
                    pass  # Handle non-existing employee as needed

            return Response({'message': 'Bulk update completed'})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class EmployeeSearchAPIView(APIView):
    def get(self, request):
        name = request.query_params.get('name')
        company = request.query_params.get('company')
        role = request.query_params.get('role')
        department = request.query_params.get('department')
        date_started = request.query_params.get('date_started')
        date_left = request.query_params.get('date_left')

        # Start with all employees
        queryset = Employee.objects.all()

        # Apply filters based on query parameters
        if name:
            queryset = queryset.filter(name__icontains=name)
        if company:
            queryset = queryset.filter(company__name__icontains=company)
        if role:
            queryset = queryset.filter(rolehistory__role__icontains=role)
        if department:
            queryset = queryset.filter(department__icontains=department)
        if date_started:
            queryset = queryset.filter(rolehistory__date_started__year=date_started)
        if date_left:
            queryset = queryset.filter(
                Q(rolehistory__date_left__year=date_left) | Q(rolehistory__date_left=None)
            )

        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data)


class RoleHistoryViewSet(viewsets.ModelViewSet):
    queryset = RoleHistory.objects.all()
    serializer_class = RoleHistorySerializer


