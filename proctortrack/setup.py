"""Setup for proctortrack XBlock."""

from __future__ import absolute_import

import os

from setuptools import setup


def package_data(pkg, roots):
    """Generic function to find package_data.

    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.

    """
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='proctortrack-xblock',
    version='0.1',
    description='proctortrack XBlock',   # TODO: write a better description.
    license='UNKNOWN',          # TODO: choose a license: 'AGPL v3' and 'Apache 2.0' are popular.
    packages=[
        'proctortrack',
    ],
    install_requires=[
        'XBlock',
    ],
    entry_points={

    "openedx.course_tab": [
               "proctortrack = proctortrack.plugins:ProctorTrackCourseTab",
              ]
    },
    package_data=package_data("proctortrack", ["static", "public"]),
)
