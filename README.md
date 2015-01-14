# test_cacheops
For the sake of https://github.com/Suor/django-cacheops/issues/125

*Update settings.py for a demo:*
- Database connection
- Redis connection (cacheops)

Output of the subsequent `./manage.py syncdb` calls:
```
➜  test_cacheops  ./manage.py syncdb
Syncing...
Creating tables ...
Creating table django_admin_log
Creating table auth_permission
Creating table auth_group_permissions
Creating table auth_group
Creating table auth_user_groups
Creating table auth_user_user_permissions
Creating table auth_user
Creating table django_content_type
Creating table django_session
Creating table corsheaders_corsmodel
Creating table south_migrationhistory

You just installed Django's auth system, which means you don't have any superusers defined.
Would you like to create one now? (yes/no): yes
Username (leave blank to use 'silver'):
Email address:
Password:
Password (again):
Superuser created successfully.
Installing custom SQL ...
Installing indexes ...
Installed 0 object(s) from 0 fixture(s)

Synced:
 > cacheops
 > django.contrib.admin
 > django.contrib.auth
 > django.contrib.contenttypes
 > django.contrib.sessions
 > django.contrib.messages
 > django.contrib.staticfiles
 > corsheaders
 > south

Not synced (use migrations):
 - problematic
(use ./manage.py migrate to migrate these)
➜  test_cacheops  ./manage.py syncdb
Syncing...
Creating tables ...
Traceback (most recent call last):
  File "./manage.py", line 10, in <module>
    execute_from_command_line(sys.argv)
  File "/Users/Silver/.virtualenvs/test_cacheops/lib/python2.7/site-packages/django/core/management/__init__.py", line 399, in execute_from_command_line
    utility.execute()
  File "/Users/Silver/.virtualenvs/test_cacheops/lib/python2.7/site-packages/django/core/management/__init__.py", line 392, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "/Users/Silver/.virtualenvs/test_cacheops/lib/python2.7/site-packages/django/core/management/base.py", line 242, in run_from_argv
    self.execute(*args, **options.__dict__)
  File "/Users/Silver/.virtualenvs/test_cacheops/lib/python2.7/site-packages/django/core/management/base.py", line 285, in execute
    output = self.handle(*args, **options)
  File "/Users/Silver/.virtualenvs/test_cacheops/lib/python2.7/site-packages/django/core/management/base.py", line 415, in handle
    return self.handle_noargs(**options)
  File "/Users/Silver/.virtualenvs/test_cacheops/lib/python2.7/site-packages/south/management/commands/syncdb.py", line 92, in handle_noargs
    syncdb.Command().execute(**options)
  File "/Users/Silver/.virtualenvs/test_cacheops/lib/python2.7/site-packages/django/core/management/base.py", line 285, in execute
    output = self.handle(*args, **options)
  File "/Users/Silver/.virtualenvs/test_cacheops/lib/python2.7/site-packages/django/core/management/base.py", line 415, in handle
    return self.handle_noargs(**options)
  File "/Users/Silver/.virtualenvs/test_cacheops/lib/python2.7/site-packages/django/core/management/commands/syncdb.py", line 112, in handle_noargs
    emit_post_sync_signal(created_models, verbosity, interactive, db)
  File "/Users/Silver/.virtualenvs/test_cacheops/lib/python2.7/site-packages/django/core/management/sql.py", line 216, in emit_post_sync_signal
    interactive=interactive, db=db)
  File "/Users/Silver/.virtualenvs/test_cacheops/lib/python2.7/site-packages/django/dispatch/dispatcher.py", line 185, in send
    response = receiver(signal=self, sender=sender, **named)
  File "/Users/Silver/.virtualenvs/test_cacheops/lib/python2.7/site-packages/django/contrib/auth/management/__init__.py", line 101, in create_permissions
    auth_app.Permission.objects.using(db).bulk_create(perms)
  File "/Users/Silver/.virtualenvs/test_cacheops/lib/python2.7/site-packages/django/db/models/query.py", line 359, in bulk_create
    self._batched_insert(objs_without_pk, fields, batch_size)
  File "/Users/Silver/.virtualenvs/test_cacheops/lib/python2.7/site-packages/django/db/models/query.py", line 838, in _batched_insert
    using=self.db)
  File "/Users/Silver/.virtualenvs/test_cacheops/lib/python2.7/site-packages/django/db/models/manager.py", line 232, in _insert
    return insert_query(self.model, objs, fields, **kwargs)
  File "/Users/Silver/.virtualenvs/test_cacheops/lib/python2.7/site-packages/django/db/models/query.py", line 1514, in insert_query
    return query.get_compiler(using=using).execute_sql(return_id)
  File "/Users/Silver/.virtualenvs/test_cacheops/lib/python2.7/site-packages/django/db/models/sql/compiler.py", line 903, in execute_sql
    cursor.execute(sql, params)
  File "/Users/Silver/.virtualenvs/test_cacheops/lib/python2.7/site-packages/django/db/backends/util.py", line 69, in execute
    return super(CursorDebugWrapper, self).execute(sql, params)
  File "/Users/Silver/.virtualenvs/test_cacheops/lib/python2.7/site-packages/django/db/backends/util.py", line 53, in execute
    return self.cursor.execute(sql, params)
  File "/Users/Silver/.virtualenvs/test_cacheops/lib/python2.7/site-packages/django/db/utils.py", line 99, in __exit__
    six.reraise(dj_exc_type, dj_exc_value, traceback)
  File "/Users/Silver/.virtualenvs/test_cacheops/lib/python2.7/site-packages/django/db/backends/util.py", line 53, in execute
    return self.cursor.execute(sql, params)
  File "/Users/Silver/.virtualenvs/test_cacheops/lib/python2.7/site-packages/django/db/backends/mysql/base.py", line 124, in execute
    return self.cursor.execute(query, args)
  File "/Users/Silver/.virtualenvs/test_cacheops/lib/python2.7/site-packages/MySQLdb/cursors.py", line 219, in execute
    self.errorhandler(self, exc, value)
  File "/Users/Silver/.virtualenvs/test_cacheops/lib/python2.7/site-packages/MySQLdb/connections.py", line 38, in defaulterrorhandler
    raise errorvalue
django.db.utils.IntegrityError: (1062, "Duplicate entry '1-add_logentry' for key 'content_type_id'")
```
