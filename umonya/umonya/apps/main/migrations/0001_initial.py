# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Announcement'
        db.create_table(u'main_announcement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('pub_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 7, 9, 0, 0))),
            ('event_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 7, 9, 0, 0))),
            ('venue', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal(u'main', ['Announcement'])

        # Adding model 'About'
        db.create_table(u'main_about', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('bios', self.gf('django.db.models.fields.TextField')()),
            ('bios_photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'main', ['About'])

        # Adding model 'Page'
        db.create_table(u'main_page', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('page', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'main', ['Page'])

        # Adding model 'Registration'
        db.create_table(u'main_registration', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('field_type', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('priority', self.gf('django.db.models.fields.IntegerField')()),
            ('required', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'main', ['Registration'])

        # Adding model 'Dynamic_Section'
        db.create_table(u'main_dynamic_section', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('section', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'main', ['Dynamic_Section'])

        # Adding model 'Contact'
        db.create_table(u'main_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'main', ['Contact'])


    def backwards(self, orm):
        # Deleting model 'Announcement'
        db.delete_table(u'main_announcement')

        # Deleting model 'About'
        db.delete_table(u'main_about')

        # Deleting model 'Page'
        db.delete_table(u'main_page')

        # Deleting model 'Registration'
        db.delete_table(u'main_registration')

        # Deleting model 'Dynamic_Section'
        db.delete_table(u'main_dynamic_section')

        # Deleting model 'Contact'
        db.delete_table(u'main_contact')


    models = {
        u'main.about': {
            'Meta': {'object_name': 'About'},
            'bios': ('django.db.models.fields.TextField', [], {}),
            'bios_photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'main.announcement': {
            'Meta': {'ordering': "['-pub_date']", 'object_name': 'Announcement'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'event_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 7, 9, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 7, 9, 0, 0)'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'venue': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'})
        },
        u'main.contact': {
            'Meta': {'object_name': 'Contact'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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
            'field_type': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'priority': ('django.db.models.fields.IntegerField', [], {}),
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['main']