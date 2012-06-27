from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^ilendit/$',
        login_required(TemplateView.as_view(
            template_name='not_implemented.html')
        ),
        name='ilendyou_itemlists_lent'
    ),
    url(r'^ioweit/$',
        login_required(TemplateView.as_view(
            template_name='not_implemented.html')
        ),
        name='ilendyou_itemlists_borrowed'
    ),
    url(r'^ihaveit/$',
        login_required(TemplateView.as_view(
            template_name='not_implemented.html')
        ),
        name='ilendyou_itemlists_offered'
    ),
    url(r'^iwantit/$',
        login_required(TemplateView.as_view(
            template_name='not_implemented.html')
        ),
        name='ilendyou_itemlists_wanted'
    ),
)