# -*- coding: utf-8 -*-
from django.db import models

#test model

class Test(models.Model):

	class Meta(object):
		verbose_name = u"Тест"
		verbose_name_plural = u"Тест"
	
	title = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u"Назва іспиту")
	
	group = models.ForeignKey('Group',
		verbose_name=u"Група",
		blank=False)
	

	date = models.DateField(
		blank=False,
		verbose_name=u'Дата іспиту',
		null=True)

	teacher = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u"Викладач")
	
	def __unicode__(self):
		return u"%s" % (self.title)