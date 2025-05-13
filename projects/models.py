from django.contrib.gis.db import models
from django.urls import reverse

class Project(models.Model):
    """项目信息模型"""
    name = models.CharField('项目名称', max_length=100)
    code = models.CharField('项目编号', max_length=50, unique=True)
    description = models.TextField('项目描述', blank=True, null=True)
    budget = models.DecimalField('项目预算', max_digits=12, decimal_places=2, blank=True, null=True)
    start_date = models.DateField('开始日期', blank=True, null=True)
    end_date = models.DateField('结束日期', blank=True, null=True)
    location = models.PointField('项目位置', geography=True)
    address = models.CharField('地址', max_length=200, blank=True, null=True)
    status = models.CharField('项目状态', max_length=20, choices=[
        ('planning', '规划中'),
        ('in_progress', '进行中'),
        ('completed', '已完成'),
        ('suspended', '已暂停'),
        ('cancelled', '已取消'),
    ], default='planning')
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        verbose_name = '项目'
        verbose_name_plural = '项目'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.code})"

    def get_absolute_url(self):
        return reverse('projects:project_detail', args=[self.pk])

    @property
    def latitude(self):
        return self.location.y if self.location else None

    @property
    def longitude(self):
        return self.location.x if self.location else None
