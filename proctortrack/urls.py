om __future__ import absolute_import

from django.conf.urls import url
from . import views

urlpatterns = [

url(
        r'^courses/{}/proctortrack$'.format(
                settings.COURSE_ID_PATTERN,
        ),
           views.proctortrack,
           name='proctortrack',
        ),
]