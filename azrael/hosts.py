from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns(
    '',
    host(r'book', 'azrael.yp_urls', name='book'),
    host(r'help', 'azrael.helpapp_urls', name='help'),
    host(r'www', 'azrael.urls', name='www')
)