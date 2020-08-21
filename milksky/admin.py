from django.contrib import admin
from .models import Tile, Point, Object, Delta, ReportSignup

admin.site.register(Tile)
admin.site.register(Point)
admin.site.register(Object)
admin.site.register(Delta)
admin.site.register(ReportSignup)