coding: utf-8 -*-
from __future__ import unicode_literals
import logging
import json

from util.json_request import JsonResponse
from util.views import ensure_valid_course_key
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.template.backends.utils import csrf_token_lazy
from django.utils.translation import ugettext as _
from django.http import HttpResponseRedirect
from django.urls import reverse

from openedx.features.enterprise_support.api import data_sharing_consent_required
from lms.djangoapps.courseware.courses import get_course_with_access
from edxmako.shortcuts import render_to_response, render_to_string
from opaque_keys.edx.keys import CourseKey

log = logging.getLogger("edx.courseware")

# Create your views here.
@ensure_csrf_cookie
@ensure_valid_course_key
@data_sharing_consent_required
@login_required
def proctortrack(request, course_id):
    """
    Lists all assignments for students
    """
    course_key = CourseKey.from_string(course_id)
    course = get_course_with_access(request.user, 'load', course_key)
    context = {
        'course': course,
    }
    return render_to_response('proctortrack/proctortrack.html',context)