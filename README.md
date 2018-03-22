# green-py-noumenalism

## TL;DR DIY:

* You must have python v3.6+ and django 2 installed

1. `git clone https://github.com/krosenk729/green-py-noumenalism.git`
1. cd into cloned folder and run `python3 manage.py makemigrations`
1. run `python3 manage.py migrate`
1. Run `python manage.py runserver 8000`
1. Visit http://localhost:8000/


## Look Before You Clone?
Screenshots of the app

_*Landing page - choose to vote or view results*_

![landing](https://raw.githubusercontent.com/krosenk729/green-py-noumenalism/master/color_vote/static/preview-1.png)

***

_*Vote page - given a random word, choose what color it makes you think of*_

![vote](https://raw.githubusercontent.com/krosenk729/green-py-noumenalism/master/color_vote/static/preview-2.png)

***


_*Results page - for each word, see swatches of votes and an analysis of how much red/green/blue is attributed to that word*_

![results](https://raw.githubusercontent.com/krosenk729/green-py-noumenalism/master/color_vote/static/preview-3.png)



## Clear Some Things 

To run shell: `python manage.py shell`
To reset all the things: `python manage.py flush `
If things get real bad: `python manage.py migrate --fake color_vote zero`

```
python manage.py makemmigrations color_vote
python manage.py migrate 
python manage.py createsuperuser
python manage.py runserver
```


## Click Some Links

+ Django Humanize https://docs.djangoproject.com/en/1.7/ref/contrib/humanize/
+ https://aliteralmind.wordpress.com/2014/09/21/jquery_django_tutorial/
+ https://github.com/quanghuy147/ajax_demo/
+ Django Database https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-DATABASES 
+ Colorful https://github.com/charettes/django-colorful
+ Caching https://docs.djangoproject.com/en/dev/topics/cache/#template-fragment-caching
+ https://coderwall.com/p/97wrya/deployment-of-static-files-in-django