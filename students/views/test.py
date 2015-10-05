#-*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, Http404

from ..models import Test
from ..utils import paginate, get_current_group

def test_view(request):
	
	group = get_current_group(request)

	if group:
		test = Test.objects.filter(group = group)
	else:
		test = Test.objects.all()

	#making sorting for tests

	if request.path == 'test/':
		test = test.order_by('title')
	order_by=request.GET.get('order_by', '')
	if order_by in ('title', 'teacher', 'id', 'date', 'group'): #order by title, teacher, id, date, group
		test = test.order_by(order_by)
		if request.GET.get('reverse', '') == '1':
			test = test.reverse()

	context= {}
	context = paginate(test, 4, request, context, var_name = 'test')
	return render(request, 'students/tests_list.html', {'test':context['page_obj'], 'is_paginated':context['is_paginated'],
		'paginator': context['paginator'], 'context':context})


