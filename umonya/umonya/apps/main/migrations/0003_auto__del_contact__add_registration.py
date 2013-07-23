# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Contact'
        db.delete_table(u'main_contact')

        # Adding model 'Registration'
        db.create_table(u'main_registration', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('form_code', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal(u'main', ['Registration'])


    def backwards(self, orm):
        # Adding model 'Contact'
        db.create_table(u'main_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'main', ['Contact'])

        # Deleting model 'Registration'
        db.delete_table(u'main_registration')


    models = {
        u'main.about': {
            'Meta': {'object_name': 'About'},
            'bios': ('django.db.models.fields.TextField', [], {}),
            'bios_photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'main.announcement': {
            'Meta': {'ordering': "['-pub_date']", 'object_name': 'Announcement'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'event_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 7, 23, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 7, 23, 0, 0)'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'venue': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'})
        },
        u'main.dynamic_section': {
            'Meta': {'object_name': 'Dynamic_Section'},
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'section': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'main.page': {
            'Meta': {'object_name': 'Page'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'main.registration': {
            'Meta': {'object_name': 'Registration'},
            'form_code': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['main']