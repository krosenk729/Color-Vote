# green-py-noumenalism

#### TL;DR DIY:

1. Run `python manage.py runserver 8000`
1. Visit http://localhost:8000/

#### Click Some Links

+ Django Humanize https://docs.djangoproject.com/en/1.7/ref/contrib/humanize/
+ https://aliteralmind.wordpress.com/2014/09/21/jquery_django_tutorial/
+ https://github.com/quanghuy147/ajax_demo/
+ Django Database https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-DATABASES 
+ Postgres DB as Service https://elephantsql.com/

#### Clear Some Things 

To run shell: `python manage.py shell`
To reset all the things: `python manage.py flush `
If things get real bad: `python manage.py migrate --fake color_vote zero`

```
python manage.py makemmigrations color_vote
python manage.py migrate 
python manage.py createsuperuser
python manage.py runserver
```