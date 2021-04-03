# Generated by Django 3.1.7 on 2021-04-03 19:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book_copies', '0002_bookcopy_available'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BookRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('n', 'New'), ('a', 'Accepted'), ('r', 'Rejected'), ('i', 'In Progress'), ('r', 'Returned'), ('c', 'Complete'), ('o', 'Overdue')], max_length=4)),
                ('original_due_date', models.DateField()),
                ('due_date', models.DateField()),
                ('book_copy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_copies.bookcopy')),
                ('borrower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
