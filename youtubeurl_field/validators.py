#-*- coding: utf-8 -*-
import re
import urllib2
from django.utils.translation import ugettext_lazy as _
from django import forms


def validate_youtube_url(value):
    '''El patron lo saque de http://stackoverflow.com/questions/2964678/jquery-youtube-url-validation-with-regex'''
    pattern = r'^http(s)?:\/\/(?:www\.)?youtube.com\/watch\?(?=.*v=\w+)(?:\S+)?$'
    
    if not value.is_empty():
        try:
            con = urllib2.urlopen(value.value)
        except ValueError:
            raise forms.ValidationError(_(u'Not a valid URL'))
        if con.code != 200:
            raise forms.ValidationError(_(u'Not a valid Youtube URL'))
        if value.value[:16] == 'http://youtu.be/':
            if re.match(r'\w+', value.value[16:]) is None:
                raise forms.ValidationError(_(u'Not a valid Youtube URL'))
        elif re.match(pattern, value.value) is None:
            raise forms.ValidationError(_(u'Not a valid Youtube URL'))
