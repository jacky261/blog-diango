from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings
from django.conf.urls.static import static
from app01.views import category,index,detail,sub_comment,login,acc_login,logout_view,add_pub
from app01.views import add_sub,Persode,register,acc_register
admin.autodiscover()
urlpatterns = patterns('',
 
    url(r'^adm/', admin.site.urls),
    url(r'^index/',index),
    url(r'^$', index),
    url(r'^detail/(\d+)/$',detail,name='detail'),
    url(r'^sub_comment/$',sub_comment),
    url(r'^account/login/$','django.contrib.auth.views.login',{'template_name':'login.html'}),
    url(r'^login/$',login),
    url(r'^acc_login/$',acc_login),
    url(r'^logout/',logout_view),
    url(r'^add_pub/',add_pub),
    url(r'^add_sub/',add_sub),
    url(r'^category/(\d+)/$',category, name='category'),
    url(r'^Persode/',Persode),
    url(r'^register/$',register),
    url(r'^acc_register/$',acc_register),
   
       
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
