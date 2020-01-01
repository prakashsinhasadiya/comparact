from __future__ import absolute_import

from django.utils.translation import ugettext as _
from django.utils.translation import ugettext_noop

from xmodule.tabs import CourseTab

class ProctorTrackCourseTab(CourseTab):
    """
    The course info view.
    """
    type = 'proctortrack'
    title = ugettext_noop('ProctorTrack')
    view_name = 'proctortrack'
    is_default = True

    @classmethod
    def is_enabled(cls, course, user=None):
        return True
