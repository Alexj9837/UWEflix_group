# Generated by Django 4.1.7 on 2023-04-03 00:14

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('clubID', models.AutoField(primary_key=True, serialize=False)),
                ('club_name', models.CharField(max_length=100)),
                ('street_number', models.CharField(max_length=10)),
                ('street', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('post_code', models.CharField(max_length=10)),
                ('landline_number', models.CharField(max_length=20)),
                ('mobile_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(default='default.png', upload_to='pics')),
                ('date', models.DateField()),
                ('duration', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=50)),
                ('rating', models.CharField(max_length=50)),
                ('cast', models.TextField(max_length=100)),
                ('trailer', models.CharField(max_length=100)),
                ('up', models.BooleanField(default=False)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screen_number', models.IntegerField()),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('show_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UWEflix.film')),
                ('screen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UWEflix.screen')),
            ],
        ),
        migrations.CreateModel(
            name='upcomings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(default='default.png', upload_to='pics')),
                ('date', models.DateField()),
                ('duration', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=50)),
                ('rating', models.CharField(max_length=50)),
                ('cast', models.TextField(max_length=100)),
                ('trailer', models.CharField(max_length=100)),
                ('up', models.BooleanField(default=False)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Custom_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(choices=[('Cinema manager', 'Cinema manager'), ('account manager', 'account manager'), ('club rep', 'club rep'), ('student', 'student')], max_length=50)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('showing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UWEflix.show')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity_adult', models.IntegerField()),
                ('quantity_children', models.IntegerField()),
                ('quantity_student', models.IntegerField()),
                ('card_number', models.IntegerField(null=True)),
                ('card_holder', models.CharField(max_length=30, null=True)),
                ('card_expire_year', models.IntegerField(null=True)),
                ('card_expire_month', models.IntegerField(null=True)),
                ('card_cvc', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UWEflix.show')),
            ],
        ),
    ]
