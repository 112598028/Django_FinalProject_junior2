from django.shortcuts import render, redirect
from news import models
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.csrf import ensure_csrf_cookie
from django import template
import math

from django.contrib.auth.decorators import permission_required

# 全域變數
page1 = 1

def news(request, pageindex=None):  #首頁
	global page1
	# 每一頁呈現公告數
	pagesize = 8

	# 讀取資料表，按照自動編號遞減排序
	newsall = models.NewsUnit.objects.all().order_by('-id')
	
	# 總共的公告數量 14
	datasize = len(newsall)
	
	# 總頁數 2 (ceil：取天花板)
	totpage = math.ceil(datasize / pagesize)
	if pageindex==None:
		page1 = 1
		newsunits = models.NewsUnit.objects.filter(enabled=True).order_by('-id')[:pagesize]
	elif pageindex=='1':
		start = (page1-2)*pagesize
		if start >= 0:
			newsunits = models.NewsUnit.objects.filter(enabled=True).order_by('-id')[start:(start+pagesize)]
			page1 -= 1
	elif pageindex=='2':
		start = page1*pagesize
		if start < datasize:
			newsunits = models.NewsUnit.objects.filter(enabled=True).order_by('-id')[start:(start+pagesize)]
			page1 += 1
	elif pageindex=='3':
		start = (page1-1)*pagesize
		newsunits = models.NewsUnit.objects.filter(enabled=True).order_by('-id')[start:(start+pagesize)]
	currentpage = page1
	return render(request, "news/news.html", locals())

def detail(request, detailid=None):  #詳細頁面
	unit = models.NewsUnit.objects.get(id=detailid)
	category = unit.catego
	title = unit.title
	pubtime = unit.pubtime
	nickname = unit.nickname
	message = unit.message
	unit.press += 1
	unit.save()
	return render(request, "news/detail.html", locals())


@permission_required('news.add_newsunit')
def newsadd(request):  #新增資料
	message = ''  #清除訊息
	category = request.POST.get('news_type', '')  #取得輸入的類別
	subject = request.POST.get('news_subject', '')
	editor = request.POST.get('news_editor', '')
	content = request.POST.get('news_content', '')
	ok = request.POST.get('news_ok', '')
	if subject=='' or editor=='' or content=='':  #若有欄位未填就顯示訊息
		message = '每一個欄位都要填寫...'
	else:
		if ok=='yes':  #根據ok值設定enabled欄位
			enabled = True
		else:
			enabled = False
		unit = models.NewsUnit.objects.create(catego=category, nickname=editor, title=subject, message=content, enabled=enabled, press=0)
		unit.save()
		return redirect('/news/')
	return render(request, "news/newsadd.html", locals())

@permission_required('news.change_newsunit')
def newsedit(request, newsid=None, edittype=None):
	unit = models.NewsUnit.objects.get(id=newsid)
	categories = ["公告", "更新", "活動", "其他"]
	if edittype == None:
		type = unit.catego
		subject = unit.title
		editor = unit.nickname
		content = unit.message
		ok = unit.enabled
	elif edittype == '1':
		category = request.POST.get('news_type', '')
		subject = request.POST.get('news_subject', '')
		editor = request.POST.get('news_editor', '')
		content = request.POST.get('news_content', '')
		ok = request.POST.get('news_ok', '')
		if ok == 'yes':
			enabled = True
		else:
			enabled = False
		unit.catego=category
		unit.catego=category
		unit.nickname=editor
		unit.title=subject
		unit.message=content
		unit.enabled=enabled
		unit.save()
		return redirect('/news/')
	return render(request, "news/newsedit.html", locals())

@permission_required('news.delete_newsunit')
def newsdelete(request, newsid=None, deletetype=None):  #刪除資料
	unit = models.NewsUnit.objects.get(id=newsid)  #讀取指定資料
	if deletetype == None:  #進入刪除頁面,顯示原有資料
		type = str(unit.catego.strip())
		subject = unit.title
		editor = unit.nickname
		content = unit.message
		date = unit.pubtime
	elif deletetype == '1':  #按刪除鈕
		unit.delete()
		return redirect('/news/')
	return render(request, "news/newsdelete.html", locals())
