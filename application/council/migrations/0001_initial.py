# Generated by Django 4.2.1 on 2025-01-31 16:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('ai_summary', models.TextField()),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('POTHOLE', 'Pothole'), ('STREET_LIGHTING', 'Street Lighting'), ('GRAFFITI', 'Graffiti'), ('ASB', 'Anti-Social Behaviour'), ('FLY_TIPPING', 'Fly-Tipping'), ('BLOCKED_DRAIN', 'Blocked Drains'), ('OTHER', 'Other')], default='OTHER', max_length=50)),
                ('reporter', models.EmailField(max_length=254)),
                ('status', models.CharField(choices=[('OPEN', 'Open'), ('IN_PROGRESS', 'In Progress'), ('RESOLVED', 'Resolved'), ('CLOSED', 'Closed')], default='OPEN', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('closed_at', models.DateTimeField(blank=True, null=True)),
                ('assigned_to', models.ForeignKey(blank=True, help_text='Assign a staff user to resolve this issue.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_issues', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
