import os, sys, django

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db.models import F, Q, Count
from django.db.models.functions import Substr

from blog.models import Post ,Tweet, User, Amodel, Bmodel


# queryset = Amodel.objects.all().values_list('a','b').union(
#     Bmodel.objects.all().values_list('a','b'), all=True 
# )

# from itertools import chain
# queryset = chain(Amodel.objects.all().values_list('a','b'), 
#     Bmodel.objects.all().values_list('a','b'))

# query_a = Amodel.objects.filter(a__startswith='a').values('a')
# query_b  = Amodel.objects.filter(a__startswith='a').only('a')

# queryset = Amodel.objects.annotate(abc=Substr('a', 1, 1)).filter(a=F('abc')).values()

# queryset = Amodel.objects.filter(Q(a='')|Q(a=None))

# queryset = Post.objects.select_related('author').values()

# queryset = Amodel.objects.all()[1:5]

# queryset = Amodel.objects.values('a').annotate(a_model_count=Count('a')).filter(a_model_count=21)


# queryset = Post.objects.values('author_id').annotate(
#     author_count = Count('author_id')
# ).values('author_count').order_by('-author_count')


# print(queryset.values('author_id'))
# print(str(queryset.query))
# print(len(queryset))