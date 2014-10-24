# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Event'
        db.create_table(u'Event_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='event', unique=True, to=orm['CustomUser.User'])),
            ('expiry_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'Event', ['Event'])

        # Adding M2M table for field messages on 'Event'
        m2m_table_name = db.shorten_name(u'Event_event_messages')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm[u'Event.event'], null=False)),
            ('message', models.ForeignKey(orm[u'Message.message'], null=False))
        ))
        db.create_unique(m2m_table_name, ['event_id', 'message_id'])

        # Adding M2M table for field followers on 'Event'
        m2m_table_name = db.shorten_name(u'Event_event_followers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm[u'Event.event'], null=False)),
            ('user', models.ForeignKey(orm[u'CustomUser.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['event_id', 'user_id'])


    def backwards(self, orm):
        # Deleting model 'Event'
        db.delete_table(u'Event_event')

        # Removing M2M table for field messages on 'Event'
        db.delete_table(db.shorten_name(u'Event_event_messages'))

        # Removing M2M table for field followers on 'Event'
        db.delete_table(db.shorten_name(u'Event_event_followers'))


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
        u'Event.event': {
            'Meta': {'object_name': 'Event'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'event'", 'unique': 'True', 'to': u"orm['CustomUser.User']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {}),
            'followers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'events'", 'blank': 'True', 'to': u"orm['CustomUser.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'messages': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'event'", 'blank': 'True', 'to': u"orm['Message.Message']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'Message.message': {
            'Meta': {'object_name': 'Message'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'messages'", 'to': u"orm['CustomUser.User']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
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

    complete_apps = ['Event']