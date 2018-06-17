import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
					  't_w_d_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
	python_pages = [
		{"title": "Official Python Tutorial",
		 "url": "http://docs.python.org/2/tutorial/"},
		{"title": "How to Think like a Computer Scientist",
		 "url": "http://www.greenteapress.com/thinkpython/"},
		{"title": "Lear Python in 10 Minutes",
		 "url": "http://www.korokithakis.net/tutorials/python/"}
	]

	django_pages = [
		{"title": "Official Django Tutorial",
		 "url": "https://docs.djangoproject.com/en/1.9/intro/tutorial01/"},
		{"title": "Django Rocks",
		 "url": "http://www.djangorocks.com/"},
		{"title": "How to Tango with Django",
		 "url": "http://www.tangowithdjango.com/"}
	]

	other_pages = [
		{"title": "Bottle",
		 "url": "http://bottlepy.org/docs/dev/"},
		{"title": "Flask",
		 "url": "http://flask.pocoo.org"}
	]

	new_cats = [
		{"name": "Python",
		 "views": 128,
		 "likes": 64,
		 "pages": python_pages},
		{"name": "Django",
		 "views": 64,
		 "likes": 32,
		 "pages": django_pages},
		{"name": "Other Frameworks",
		 "views": 32,
		 "likes": 16,
		 "pages": other_pages}
	] 
	
	#cats = {"Python": {"pages": python_pages},
	#		"Django": {"pages": django_pages},
	#		"Other Frameworks": {"pages": other_pages}
	#}

	#Now we add the categories and their respective pages
	#for cat, cat_data in cats.items():
	#	c = add_cat(cat)
	#	for p in cat_data['pages']:
	#		add_page(c, p['title'], p['url'])
	for cat in new_cats:
		c = add_cat(cat['name'], cat['views'], cat['likes'])
		for p in cat['pages']:
			add_page(c, p['title'], p['url'])



	#we print to verify each categorie we add
	for c in Category.objects.all():
		for p in Page.objects.filter(category=c):
			print("- {0} - {1}".format(str(c), str(p)))

def add_cat(name, views, likes):
	c = Category.objects.get_or_create(name=name)[0]
	c.views=views
	c.likes=likes
	c.save()
	return c

def add_page(cat, title, url, views=0):
	p = Page.objects.get_or_create(category=cat, title=title)[0]
	p.url=url
	p.views=views
	p.save()
	return p

#execution
if __name__ == '__main__':
	print("Starting Rango population scipt...")
	populate()