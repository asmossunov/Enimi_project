# Generated by Django 4.1.6 on 2023-02-10 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('calendarapp', '0008_event_event_format'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberEventRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three'), ('4', 'Four'), ('5', 'Five')], null=True, verbose_name='Оценка')),
                ('comment', models.TextField(blank=True, default='Нет комментария', verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='calendarapp.event', verbose_name='Занятие')),
                ('event_member', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='calendarapp.eventmember', verbose_name='Ученик')),
            ],
            options={
                'verbose_name': 'Оценка',
                'verbose_name_plural': 'Оценки',
            },
        ),
    ]