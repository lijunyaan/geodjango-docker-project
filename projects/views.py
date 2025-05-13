from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from django.core.serializers import serialize
from django.http import JsonResponse
from .models import Project

class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.GET.get('status')
        if status:
            queryset = queryset.filter(status=status)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_choices'] = Project._meta.get_field('status').choices
        return context

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'

class ProjectMapView(TemplateView):
    template_name = 'projects/project_map.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        return context

def project_geojson(request):
    """返回项目的GeoJSON数据"""
    projects = Project.objects.all()
    geojson = serialize('geojson', projects,
                        geometry_field='location',
                        fields=('name', 'code', 'status', 'pk'))
    return JsonResponse(geojson, safe=False)
