# Generated by Django 3.0.5 on 2020-04-17 14:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import easy_thumbnails.fields
import userena.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('primary_contact', models.ForeignKey(help_text='Contact for org.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('name', 'primary_contact')},
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mugshot', easy_thumbnails.fields.ThumbnailerImageField(blank=True, help_text='A personal image displayed in your profile.', upload_to=userena.models.upload_to_mugshot, verbose_name='mugshot')),
                ('privacy', models.CharField(choices=[('open', 'Open'), ('registered', 'Registered'), ('closed', 'Closed')], default='registered', help_text='Designates who can view your profile.', max_length=15, verbose_name='privacy')),
                ('email', models.CharField(blank=True, max_length=250, null=True)),
                ('score', models.IntegerField(default=1)),
                ('last_activity', models.DateTimeField(auto_now_add=True)),
                ('openbadge_id', models.CharField(blank=True, max_length=250, null=True)),
                ('organization', models.ForeignKey(blank=True, help_text="If '------', no Organization records share the email domain.", null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.Organization')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'permissions': (('view_profile', 'Can view profile'),),
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete'),
            },
        ),
        migrations.CreateModel(
            name='UserAuthorization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorized', models.BooleanField(help_text='Check this to approve member access.')),
                ('permission_granted_on', models.DateTimeField(auto_now_add=True)),
                ('user_accepted_terms_on', models.DateTimeField(blank=True, null=True)),
                ('permissions_granted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='permissions_granted_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='EmailDomain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_domain', models.CharField(max_length=50)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.Organization')),
            ],
        ),
    ]
