import random

from django.conf import settings
from django.core.cache import cache

from blog.models import Blog
from mailing.models import Settings


def get_cashe_blog_list_and_mailing_count():
    if settings.CACHE_ENABLED:
        key1 = 'blog_list'
        key2 = 'mailing_count'
        blog_list = cache.get(key1)
        mailing_count = cache.get(key2)
        if blog_list or mailing_count is None:
            blog_list = list(Blog.objects.all())
            random.shuffle(blog_list)
            cache.set(key1, blog_list)
            mailing_count = Settings.objects.all().count()
            cache.set(key2, blog_list)
    else:
        blog_list = list(Blog.objects.all())
        random.shuffle(blog_list)
        mailing_count = Settings.objects.all().count()

    return blog_list[:3], mailing_count
