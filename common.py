# -*- coding: utf-8 -*-

import urllib2
import urlparse

def download1(url):
    """Simple downloader"""
    return urllib2.urlopen(url).read()

def download2(url):
    print 'Downloading:', url
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Download error', e.reason
        html = None
    return

def download3(url, num_retries=2):
    """Download function that also retries 5xx errors"""
    print 'Downloading:', url
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Download error:', e.reason
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                #retry 5xx HTTP errors
                html = download3(url, num_retries-1)
    return html

def download4(url, user_agent='wswp', num_retries=2):
    """Download function that includes user agent support """
    print 'Downloading:', url
    headers = {'User-agent': user_agent}
    request = urllib2.Request(url, headers=headers)
    try:
        html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print 'Download error:', e.reason
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                #retry 5xx HTTP errors
                html = download4(url, user_agent, num_retries-1)
    return html

download = download4

if __name__ == '__main__':
    print download3('http://www.meetup.com/')
