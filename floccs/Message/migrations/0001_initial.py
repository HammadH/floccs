# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Thread'
        db.create_table(u'Message_thread', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Projects.Project'], unique=True)),
        ))
        db.send_create_signal(u'Message', ['Thread'])

        # Adding model 'Message'
        db.create_table(u'Message_message', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sender', self.gf('django.db.models.fields.related.ForeignKey')(related_name='messages', to=orm['CustomUser.User'])),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'Message', ['Message'])

        # Adding model 'ThreadedMessage'
        db.create_table(u'Message_threadedmessage', (
            (u'message_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['Message.Message'], unique=True, primary_key=True)),
            ('thread', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Message.Thread'])),
            ('parent_object', self.gf('django.db.models.fields.related.ForeignKey')(related_name='replies', to=orm['Message.ThreadedMessage'])),
            ('is_reply', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'Message', ['ThreadedMessage'])

        # Adding model 'PersonalMessage'
        db.create_table(u'Message_personalmessage', (
            (u'message_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['Message.Message'], unique=True, primary_key=True)),
            ('recipient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['CustomUser.User'])),
            ('notification', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Notifications.Notification'], unique=True)),
        ))
        db.send_create_signal(u'Message', ['PersonalMessage'])


    def backwards(self, orm):
        # Deleting model 'Thread'
        db.delete_table(u'Message_thread')

        # Deleting model 'Message'
        db.delete_table(u'Message_message')

        # Deleting model 'ThreadedMessage'
        db.delete_table(u'Message_threadedmessage')

        # Deleting model 'PersonalMessage'
        db.delete_table(u'Message_personalmessage')


    models = {
        u'CustomUser.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'place_of_stay': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'Message.message': {
            'Meta': {'object_name': 'Message'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'messages'", 'to': u"orm['CustomUser.User']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'Message.personalmessage': {
            'Meta': {'object_name': 'PersonalMessage', '_ormbases': [u'Message.Message']},
            u'message_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['Message.Message']", 'unique': 'True', 'primary_key': 'True'}),
            'notification': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Notifications.Notification']", 'unique': 'True'}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['CustomUser.User']"})
        },
        u'Message.thread': {
            'Meta': {'object_name': 'Thread'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Projects.Project']", 'unique': 'True'})
        },
        u'Message.threadedmessage': {
            'Meta': {'object_name': 'ThreadedMessage', '_ormbases': [u'Message.Message']},
            'is_reply': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'message_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['Message.Message']", 'unique': 'True', 'primary_key': 'True'}),
            'parent_object': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'replies'", 'to': u"orm['Message.ThreadedMessage']"}),
            'thread': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Message.Thread']"})
        },
        u'Notifications.notification': {
            'Meta': {'object_name': 'Notification'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'UNREAD'", 'max_length': '20'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['CustomUser.User']"})
        },
        u'Projects.project': {
            'Meta': {'object_name': 'Project'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'followers': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'following_ideas'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['CustomUser.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['CustomUser.User']"}),
            'project_status': ('django.db.models.fields.CharField', [], {'default': "'OPEN'", 'max_length': '10'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['Message']