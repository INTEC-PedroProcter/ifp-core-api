from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class ReactAdminPagination(PageNumberPagination):
    def paginate_queryset(self, queryset, request, view=None):
        self.range = request.query_params.get("range")
        return super().paginate_queryset(queryset, request, view)
    
    def get_paginated_response(self, data):
        if self.range:
            start, end = self.range.strip("[]").split(",")
            start, end = int(start), int(end)
        else:
            start = 0
            end = len(data) -1

        
        return Response(
            data, 
            headers = {
                "Content-Range": f"{self.request.path} {start}-{end}/{self.page.paginator.count}"
            }
        )
