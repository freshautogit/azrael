from django_hosts import patterns, host
import yellowpages

host_patterns = patterns(
    '',
    host(r'book', yellowpages.views.redirect_to_help, name='book'),
    host(r'help', 'azrael.yp_urls', name='help'),
)
