# Copyright 2015 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.shortcuts import render, redirect
from django.views import generic
# from django.utils import timezone
# Create your views here.

from .models import Project, File, ViewCount, Skill, Role, Client
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from .misc import get_client_ip

import datetime

def home(request):
    """
    View function for home page of site.
    """
    list_of_projects = Project.objects.filter(status = 1)
    list_of_categories = Project._meta.get_field('category').choices
    categories = [category[1] for category in list_of_categories][1:] #exclude the uncategorized
    # Render the HTML template index.html with the data in the context variable
    

    context={
        'projects' : list_of_projects,
        'categories': categories,
    }

    return render(request, 'home.html', context)

    # return HttpResponse("Hello, world. You're at the polls index.")

def project_detail(request,pk):
    list_of_projects = Project.objects.filter(status = 1)
    related_project = Project.objects.filter(status = 1).exclude(pk=pk)[:3]
    
    selected_project=Project.objects.get(pk=pk)    
    files = File.objects.filter(project=selected_project)
    
    skills = Skill.objects.filter(project=selected_project)
    skill_list = [s.name for s in skills]
    
    clients= Client.objects.filter(project=selected_project)
    client_list = [c.name for c in clients]
    
    roles = Role.objects.filter(project=selected_project)
    role_list = [r.name for r in roles]

    count = ViewCount(project = selected_project, ip=get_client_ip(request), date=datetime.datetime.today())
    count.save()
    selected_project.num_view = ViewCount.objects.filter(project=selected_project).count()
    selected_project.save()

    context={
        'projects' : list_of_projects,
        'selected_project':selected_project, 
        'related_project': related_project,
        'files': files,
        'skills': ', '.join(skill_list),
        'clients': ', '.join(client_list),
        'roles': ', '.join(role_list),

    }


    return render(request, 'project_detail.html', context)



def contact(request):
    list_of_projects = Project.objects.filter(status = 1)
    list_of_categories = Project._meta.get_field('category').choices
    categories = [category[1] for category in list_of_categories][1:] #exclude the uncategorized

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            email_record = form.save(commit=False)
            email_record.sent_date = datetime.datetime.today()
            email_record.save()
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['linli.ding6@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('thanks')
            # return HTTPResponseRedirect()
    else:
        form = ContactForm()

    context={
        'projects' : list_of_projects,
        'categories': categories,
        'form': form,
    }

    return render(request, 'contact.html', context)

def thanks(request):
    list_of_projects = Project.objects.filter(status = 1)
    list_of_categories = Project._meta.get_field('category').choices
    categories = [category[1] for category in list_of_categories][1:] #exclude the uncategorized

    context={'projects' : list_of_projects,
        'categories': categories,

    }
    return render(request, 'thanks.html', context)
