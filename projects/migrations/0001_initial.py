# Generated by Django 2.0.1 on 2018-01-09 16:48

from django.db import migrations, models
import django.db.models.deletion
import projects.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Enter a client name (e.g. TACC, Database Management Course etc.)', max_length=200)),
                ('client_info', models.TextField(blank=True, help_text='Enter a brief description of the client', max_length=1000)),
                ('client_url', models.URLField(blank=True, help_text='Enter a website link of the client')),
            ],
        ),
        migrations.CreateModel(
            name='ContactRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField(max_length=2000)),
                ('sent_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Enter a file name (e.g. screenshot, image1 etc.)', max_length=200)),
                ('image', models.ImageField(blank=True, upload_to=projects.models.File.project_file_path)),
                ('description', models.TextField(blank=True, help_text='Enter a brief description of the file', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField(blank=True, help_text='Enter a one sentence description of the project', max_length=200)),
                ('description', models.TextField(blank=True, help_text='Enter a brief description of the project', max_length=1000)),
                ('cover_pic', models.ImageField(blank=True, upload_to=projects.models.Project.project_cover_pic_path)),
                ('status', models.IntegerField(choices=[(0, 'Developing'), (1, 'Published')], default=0)),
                ('category', models.IntegerField(choices=[(0, 'Uncategorized'), (1, 'Business Analysis'), (2, 'Data Modeling'), (3, 'Website Developing')], default=0)),
                ('num_view', models.IntegerField(default=0)),
                ('demo_url', models.URLField(blank=True, help_text='Insert an internal link for this project if there is any')),
                ('creation_date', models.CharField(blank=True, help_text='Enter month and year', max_length=20)),
                ('team_size', models.IntegerField(default=1, help_text='Enter the size of the team for the project')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter your role (e.g. Full Stack Developer, Data Analyst etc.)', max_length=200)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='roles', to='projects.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a technical skill (e.g. Python, PHP etc.)', max_length=200)),
                ('level', models.IntegerField(choices=[(0, ''), (1, 'Beginner'), (2, 'Intermediate'), (3, 'Advanced')], default=0)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='skills', to='projects.Project')),
            ],
        ),
        migrations.CreateModel(
            name='ViewCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
                ('date', models.DateTimeField()),
                ('project', models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.Project')),
            ],
        ),
        migrations.AddField(
            model_name='file',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='files', to='projects.Project'),
        ),
        migrations.AddField(
            model_name='client',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clients', to='projects.Project'),
        ),
    ]