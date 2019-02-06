from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from .models import Log
from .serializers import LogSerializer


class LogView(APIView):
    
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'log/index.html'
    
    
    def get(self, request):
        logs = Log.objects.all()   #.order_by('date')

        serializer = LogSerializer(logs, many=True)
        return Response({"logs": serializer.data})

    def post(self, request):
        log = request.data.get('log')

        serializer=LogSerializer(data=log)
        if serializer.is_valid(raise_exception=True):
            log_saved = serializer.save()
        return Response({"success": "Log '{}' created successfully".format(log_saved.title)})


    def put(self, request, pk):
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
        return Response({"message": "Log with id '{}' has been deleted.".format(pk)}, status=204)
