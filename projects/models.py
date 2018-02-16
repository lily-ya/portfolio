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

from django.db import models
from datetime import date
from django.urls import reverse #Used to generate URLs by reversing the URL patterns


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

# Create your models here.


class Skill(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=200, help_text="Enter a technical skill (e.g. Python, PHP etc.)")
    SKILL_LEVEL = [
    (0, '',),
    (1, 'Beginner',),
    (2, 'Intermediate',),
    (3, 'Advanced',),
    ]

    level = models.IntegerField(default=0, choices=SKILL_LEVEL)
    project = models.ForeignKey('Project', on_delete=models.SET_NULL, null=True, blank=True, related_name='skills') 

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
    class Meta:
        ordering = ['name']

class Role(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=200, help_text="Enter your role (e.g. Full Stack Developer, Data Analyst etc.)")
    project = models.ForeignKey('Project', on_delete=models.SET_NULL, null=True, blank=True, related_name='roles') 

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class Client(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=200, help_text="Enter a client name (e.g. TACC, Database Management Course etc.)", blank=True)
    client_info = models.TextField(max_length=1000, help_text="Enter a brief description of the client", blank=True)
    client_url = models.URLField(max_length=200, help_text="Enter a website link of the client", blank=True)
    project = models.ForeignKey('Project', on_delete=models.SET_NULL, null=True, blank=True, related_name='clients') 

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class File(models.Model):
    """
    Model representing a specific copy of a book (i.e. that can be borrowed from the library).
    """
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular file across whole site")
    name = models.CharField(max_length=200, help_text="Enter a file name (e.g. screenshot, image1 etc.)", blank=True)

    def project_file_path(self, filename):
    	return '/'.join(['uploads', str(self.project.id), 'file', filename]);

    image = models.ImageField(upload_to=project_file_path, blank=True)
    description = models.TextField(max_length=1000, help_text="Enter a brief description of the file", blank=True)
    project = models.ForeignKey('Project', on_delete=models.SET_NULL, null=True, blank=True, related_name='files') 
    display_order = models.IntegerField(default=0, null=True, blank=True)


    def __str__(self):
        """
        String for representing the Model object
        """
        return self.name

    class Meta:
        ordering = ['display_order', 'name']

class Project(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=200, help_text="Enter a one sentence description of the project", blank=True)   
    description = models.TextField(max_length=1000, help_text="Enter a brief description of the project", blank=True)
 
    def project_cover_pic_path(self, filename):
    	return '/'.join(['uploads', str(self.id), 'cover_pic', filename]);

    cover_pic = models.ImageField(upload_to=project_cover_pic_path, blank=True)
    
    PUBLICATION_STATUS = [
    (0, 'Developing',),
    (1, 'Published',),
    ]

    status = models.IntegerField(default=0, choices=PUBLICATION_STATUS)

    PROJECT_CATEGORY = [
    (0, 'Uncategorized',),
    (1, 'Data Analysis',),
    (2, 'Database Management',),
    ]

    category = models.IntegerField(default=0, choices=PROJECT_CATEGORY)
    # category = models.ForeignKey(Category, help_text="select a category for this project", on_delete=models.SET_NULL, null=True, blank=True, related_name="categories")
    num_view = models.IntegerField(default=0)
    demo_url = models.URLField(max_length=200, blank=True, help_text="Insert an internal link for this project if there is any")
    demo_name = models.CharField(max_length=100, blank=True, help_text="put the name for demo_url")
    demo_tag = models.CharField(max_length=100, blank=True, help_text="put the name tag for demo_url")
    # skill = models.ForeignKey(Skill, related_name='projects', help_text="Select a skill for this project", on_delete=models.SET_NULL, null=True, blank=True)
    # ManyToManyField used because skill can contain many projects. projects can cover many skills.
    # skill class has already been defined so we can specify the object above.
    creation_date = models.CharField(max_length=20, blank=True, help_text="Enter month and year")
    # role = models.ForeignKey(Role, related_name='projects', help_text="Select your role for this project", on_delete=models.SET_NULL, null=True, blank=True)
    # client = models.ForeignKey(Client, related_name='projects', on_delete=models.SET_NULL, null=True, blank=True)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file.
    team_size = models.IntegerField(default=1, help_text="Enter the size of the team for the project")
    display_order = models.IntegerField(default=0, null=True, blank=True)
    
    class Meta:
    	ordering = ['display_order', 'title']


    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title

    def cover_pic_url(self):
        if self.cover_pic and hasattr(self.cover_pic, 'url'):
            return self.cover_pic.url

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('project-detail', args=[str(self.id)])

    def display_skill(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ' | '.join([ skill.name.split(" ")[0] for skill in self.skills.all()])
        display_skill.short_description = 'Skill'


class ViewCount(models.Model):
    """
    This table would be used to store all the data related to views
    tracking.
    """
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, default = 0, null = True, blank = True)
    ip = models.GenericIPAddressField()
    date = models.DateTimeField()

class ContactRecord(models.Model):
    # from_name 
    name= models.CharField(max_length=100)
    # from_email
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=2000)
    sent_date = models.DateTimeField(blank=True, null=True)

