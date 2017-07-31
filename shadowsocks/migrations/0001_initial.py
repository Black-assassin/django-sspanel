# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-30 07:31
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import shadowsocks.tools


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('balance', models.DecimalField(blank=True, decimal_places=2, default=0, editable=False, max_digits=10, null=True, verbose_name='余额')),
                ('invitecode', models.CharField(max_length=40, verbose_name='邀请码')),
                ('level', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(9), django.core.validators.MinValueValidator(0)], verbose_name='用户等级')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Aliveip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='用户名')),
                ('ip_address', models.GenericIPAddressField(verbose_name='在线ip')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='时间')),
            ],
            options={
                'verbose_name_plural': '在线ip',
                'ordering': ('-time',),
            },
        ),
        migrations.CreateModel(
            name='Donate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='捐赠时间')),
                ('money', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='捐赠金额')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '捐赠',
                'ordering': ('-time',),
            },
        ),
        migrations.CreateModel(
            name='InviteCode',
            fields=[
                ('code', models.CharField(blank=True, default=shadowsocks.tools.get_long_random_string, max_length=40, primary_key=True, serialize=False, verbose_name='邀请码')),
                ('time_created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name_plural': '邀请码',
                'ordering': ('-time_created',),
            },
        ),
        migrations.CreateModel(
            name='MoneyCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=128, null=True, verbose_name='用户名')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='捐赠时间')),
                ('code', models.CharField(blank=True, default=shadowsocks.tools.get_long_random_string, max_length=40, unique=True, verbose_name='充值码')),
                ('number', models.DecimalField(blank=True, decimal_places=2, default=10, max_digits=10, null=True, verbose_name='捐赠金额')),
                ('isused', models.BooleanField(default=False, verbose_name='是否使用')),
            ],
            options={
                'verbose_name_plural': '充值码',
                'ordering': ('isused',),
            },
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('name', models.CharField(max_length=32, verbose_name='名字')),
                ('server', models.CharField(max_length=128, verbose_name='服务器IP')),
                ('method', models.CharField(choices=[('aes-256-cfb', 'aes-256-cfb'), ('rc4-md5', 'rc4-md5'), ('salsa20', 'salsa20'), ('aes-128-ctr', 'aes-128-ctr')], default='aes-256-cfb', max_length=32, verbose_name='加密类型')),
                ('protocol', models.CharField(choices=[('auth_sha1_v4', 'auth_sha1_v4'), ('auth_aes128_md5', 'auth_aes128_md5'), ('auth_aes128_sha1', 'auth_aes128_sha1'), ('auth_chain_a', 'auth_chain_a'), ('origin', 'origin')], default='origin', max_length=32, verbose_name='协议')),
                ('obfs', models.CharField(choices=[('plain', 'plain'), ('http_simple', 'http_simple'), ('http_post', 'http_post'), ('tls1.2_ticket_auth', 'tls1.2_ticket_auth')], default='plain', max_length=32, verbose_name='混淆')),
                ('info', models.CharField(blank=True, max_length=1024, null=True, verbose_name='节点说明')),
                ('status', models.CharField(choices=[('ok', '好用'), ('slow', '不好用'), ('fail', '坏了')], default='ok', max_length=32, verbose_name='状态')),
                ('node_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='节点id')),
                ('level', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(9), django.core.validators.MinValueValidator(0)], verbose_name='节点等级')),
            ],
            options={
                'verbose_name_plural': '节点',
                'ordering': ['node_id'],
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='商品描述')),
                ('transfer', models.BigIntegerField(default=1073741824, verbose_name='增加的流量')),
                ('money', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='金额')),
            ],
            options={
                'verbose_name_plural': '商品',
            },
        ),
        migrations.AddField(
            model_name='aliveip',
            name='node_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alive_node_id', to='shadowsocks.Node'),
        ),
    ]
