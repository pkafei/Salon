from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render


class Landing(TemplateView):
	template_name = "landing.html"

	def get_context_data(self, **kwargs):
		context = super(Landing, self).get_context_data(**kwargs)
		return context


class Contact(TemplateView):
	template_name = "contact.html"

	def get_context_data(self, **kwargs):
		context = super(Contact, self).get_context_data(**kwargs)
		return context

class Services(TemplateView):
	template_name = "services.html"

	def get_context_data(self, **kwargs):
		context = super(Services, self).get_context_data(**kwargs)
		return context