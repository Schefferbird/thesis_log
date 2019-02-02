#from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404, ListCreateAPIView, RetrieveUpdateDestroyAPIView



from .models import Log
from .serializers import LogSerializer


class LogView(ListCreateAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer

    def perform_create(self, serializer):
        author = get_object_or_404('Author', id=self.request.data.get('author_id'))
        return serializer.save(author=author)

    ''' def get(self, request, *args, **kwargs):
        return self.list(request, *args, *kwargs) '''

    
class SingleLogView(RetrieveUpdateDestroyAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer

    ''' def put(self, request, pk):
        saved_log = get_object_or_404(Log.objects.all(), pk=pk)
        data = request.data.get('log')
        serializer = LogSerializer(instance=saved_log, data=data, partial=True)
        if serializer.is_valid(raise_execption=True):
            log_saved = serializer.save()
        return Response({"success": "Log '{}' updated successfully".format(log_saved.title)})

    def delete(self, request, pk):
        # Get object with thid pk
        log = get_object_or_404(Log.objects.all(), pk=pk)
        log.delete()
        return Response({"message": "Log with id '{}' has been deleted.".format(pk)}, status=204) '''
