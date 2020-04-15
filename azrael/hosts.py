from django_hosts import patterns, host
import yellowpages

host_patterns = patterns(
    '',
    host(r'book', 'azrael.redirect', name='book'),
    host(r'help', 'azrael.yp_urls', name='help'),
    host(r'www', 'azrael.urls', name='www'),
)
