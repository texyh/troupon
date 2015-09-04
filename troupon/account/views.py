from django.shortcuts import render
from account.forms import MySignupForm
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf

# Create your views here.
class UserSignupreq(View):

    def post(self,request):
        form_data = {'username' :request.POST.get('username',''),
                'email' :request.POST.get('email',''),
                'first_name':request.POST.get('first_name',''),
                'last_name' :request.POST.get('last_name',''),
                'password1':request.POST.get('password1',''),
                'password2': request.POST.get('password1',''),
         'csrfmiddlewaretoken': request.POST.get('csrfmiddlewaretoken',''),
                        }

        mysignupform = MySignupForm(form_data)
        if mysignupform.is_valid():
            print form is valid
            mysignupform.save()

            return HttpResponseRedirect('/auth/confirm/')

        else:
          return HttpResponseRedirect('/auth/signup/')
 
class UserSignupView(TemplateView):
  template_name = 'account/signup.html'

  def get_context_data(self, **kwargs):
        auth_token = unicode(csrf(self.request)['csrf_token'])
        context = super(UserSignupView, self).get_context_data(**kwargs)
        context['csrf_token'] = auth_token
        return context

class Userconfirm(TemplateView):
    template_name = 'account/confirm.html'


    