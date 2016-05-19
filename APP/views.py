# -*- coding: utf-8 -*-
import urllib
import urllib2

import re
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

import APP
from APP.QSBK import QSBK1
from APP.SegmentfaultQuestionSpider import *
from APP.models import *


def SegmentfaultQuestionSpider1(request):
    Item=SegmentfaultQuestionSpider("1010000002542775")
    Item.save()
    return render_to_response('search_results.html',{'item': Item})

def SegmentfaultTagSpider1(request):
    Items=SegmentfaultTagSpider("微信")
    Items.crawl_all_pages()
    return render_to_response('search_resultsList.html',{'Items': Items})

def CrawlerTestBaiDu(request):
    values = {"username":"1154385001@qq.com","password":"qaz123"}
    data = urllib.urlencode(values)
    url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
    request = urllib2.Request(url,data)
    response = urllib2.urlopen(request)
    return render_to_response('search_resultsList.html', {'Items': response.read()})

def CrawlerGet(request):
    # page = 2
    # url = 'http://www.qiushibaike.com/hot/page/' + str(page)
    # user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    # headers = { 'User-Agent' : user_agent }
    # try:
    #     request = urllib2.Request(url,headers = headers)
    #     response = urllib2.urlopen(request)
    #     a=response.read()
    #     content = response.read().decode('utf-8')
    #     pattern = re.compile('<div.*?class="author.*?>.*?<a.*?</a>.*?<a.*?>(.*?)</a>.*?<div.*?class'+
    #                          '="content".*?title="(.*?)">(.*?)</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
    #     items = re.findall(pattern,content)
    #     for item in items:
    #         haveImg = re.search("img",item[3])
    #         # if not haveImg:
    #         print item[0],item[1],item[2],item[4]
    # except urllib2.URLError, e:
    #     if hasattr(e,"code"):
    #         print e.code
    #     if hasattr(e,"reason"):
    #         print e.reason

    QSBK1().start()
    return render_to_response('search_resultsListQS.html', {'Items': ""})
