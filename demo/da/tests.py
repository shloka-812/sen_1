# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from django.urls import reverse,resolve

class TestUrls(TestCase):

	def test_index_url(self):
		path = reverse('index')
		assert resolve(path).view_name == 'index'

	def test_prediction_url(self):
		path = reverse('da:prediction')
		assert resolve(path).view_name == 'da:prediction'

	def test_register_url(self):
		path = reverse('da:register')
		assert resolve(path).view_name == 'da:register'

	def test_register_h_url(self):
		path = reverse('da:register_h')
		assert resolve(path).view_name == 'da:register_h'

	def test_register_p_url(self):
		path = reverse('da:register_p')
		assert resolve(path).view_name == 'da:register_p'

	def test_login_url(self):
		path = reverse('da:user_login')
		assert resolve(path).view_name == 'da:user_login'

	def test_help_url(self):
		path = reverse('da:help')
		assert resolve(path).view_name == 'da:help'

	def test_aboutus_url(self):
		path = reverse('da:aboutus')
		assert resolve(path).view_name == 'da:aboutus'

	def test_keyfacts_url(self):
		path = reverse('da:keyfacts')
		assert resolve(path).view_name == 'da:keyfacts'

	def test_newsfeed_url(self):
		path = reverse('da:newsfeed')
		assert resolve(path).view_name == 'da:newsfeed'

	def test_feeddata_url(self):
		path = reverse('da:feeddata')
		assert resolve(path).view_name == 'da:feeddata'

	def test_outbreaks_url(self):
		path = reverse('da:outbreaks')
		assert resolve(path).view_name == 'da:outbreaks'

	def test_outbreaks_s_url(self):
		path = reverse('da:outbreak_submission')
		assert resolve(path).view_name == 'da:outbreak_submission'

	def test_logout_url(self):
		path = reverse('logout')
		assert resolve(path).view_name == 'logout'




# Create your tests here.
