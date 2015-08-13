from django.test import TestCase

# Create your tests here.
def application(env,start_response):
    start_response('200 ok',[('content_type','text/html')])
    return 'hello world'
