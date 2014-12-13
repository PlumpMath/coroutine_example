from __future__ import with_statement
from eventlet.green import urllib2
import eventlet
import re


# http://daringfireball.net/2009/11/liberal_regex_for_matching_urls
url_regex = re.compile(r'\b(([\w-]+://?|www[.])[^\s()<>]+(?:\([\w\d]+\)|([^[:punct:]\s]|/)))')


def fetch(url, seen, pool):
    '''Fetch A url, stick any found urls into the seen set,
    and dispatch any new  ones to te pool.'''
    print "fetching", url
    data = ''
    with eventlet.Timeout(5, False):
        data = urllib2.urlopen(url).read()
    for url_match in url_regex.finditer(data):
        new_url = url_match.group(0)
        # Only send requests to eventlet.net so as not to destroy the internet
        if new_url not in seen:  # and 'bbs.byr.cn' in new_url:
            seen.add(new_url)
            # While this seems stack-recursive, it is actually not.
            # Spawned greenthreads start their own stacks
            pool.spawn_n(fetch, new_url, seen, pool)


def crawl(start_url):
    '''Recrusively crawl starting from *start_url*.Return a set of
    urls that were found.
    '''
    pool = eventlet.GreenPool()
    seen = set()
    fetch(start_url, seen, pool)
    pool.waitall()
    return seen

seen = crawl("http://www.muzixing.com")
print "I saw there urls:", seen
# print '\n'.join(seen)
