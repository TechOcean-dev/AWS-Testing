from django.shortcuts import render
from django.views import View
from queries_test.models import student
from django.db.models import Q, Sum, Avg, Min, Max
from rest_framework import filters
from rest_framework import viewsets, permissions
from rest_framework import viewsets, mixins
from queries_test.serializers import StudentSerializer
from config.settings import AWS_S3_CUSTOM_DOMAIN


# Create your views here.
class SearchListView(viewsets.GenericViewSet, 
                     mixins.ListModelMixin, 
                     mixins.UpdateModelMixin, 
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):
    
    # Allows authenticated users to have full access, while read-only access is granted to unauthenticated users or get request.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,] 

    # permission_classes = [permissions.AllowAny]      # Allows unrestricted access to the view or viewset
    # permission_classes = [permissions.IsAuthenticated]  # Requires the user to be authenticated to access the view or viewset
    # permission_classes = [permissions.IsAdminUser] # Requires the user to be a staff member or superuser to access the view or viewset
    # permission_classes = [permissions.DjangoModelPermissions]  #Requires the user to have appropriate model-level permissions (e.g., view, add, change, delete) to access the view or viewset.
    # permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    
    serializer_class = StudentSerializer
    queryset = student.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['=name', 'section', 'age', 'address',]  # Specify the fields you want to search on
    ordering_fields = ['name', 'age']
    
class Index(View):   
    def get(self, request):
        search =request.GET.get('search', None)
        if search:
            search = student.objects.filter(
                Q(name__icontains=search) |  # Match field1 containing the query
                Q(section__icontains=search) |  # Match field2 containing the query
                Q(address__icontains=search)     # Match field3 containing the query
            )
        result = student.objects.aggregate(avg_age=(Avg('age')), min_age=(Min('age')), 
                                           max_age=Max('age'), sum_age=Sum('age') )

        Data = {'search': search, 
                'avg_age': result['avg_age'],
                'min_age': result['min_age'],
                'max_age': result['max_age'],
                'sum_age': result['sum_age'],
                }
        return render(request, 'index.html', Data)