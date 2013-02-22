# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Location'
        db.create_table(u'library_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.TextField')(unique=True)),
        ))
        db.send_create_signal(u'library', ['Location'])

        # Adding model 'Author'
        db.create_table(u'library_author', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.TextField')(unique=True)),
        ))
        db.send_create_signal(u'library', ['Author'])

        # Adding model 'Book'
        db.create_table(u'library_book', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('origkey', self.gf('django.db.models.fields.CharField')(max_length=36, null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('sortkey', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('year_published', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['library.Location'], null=True, blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'library', ['Book'])

        # Adding M2M table for field authors on 'Book'
        db.create_table(u'library_book_authors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm[u'library.book'], null=False)),
            ('author', models.ForeignKey(orm[u'library.author'], null=False))
        ))
        db.create_unique(u'library_book_authors', ['book_id', 'author_id'])


    def backwards(self, orm):
        # Deleting model 'Location'
        db.delete_table(u'library_location')

        # Deleting model 'Author'
        db.delete_table(u'library_author')

        # Deleting model 'Book'
        db.delete_table(u'library_book')

        # Removing M2M table for field authors on 'Book'
        db.delete_table('library_book_authors')


    models = {
        u'library.author': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Author'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'unique': 'True'})
        },
        u'library.book': {
            'Meta': {'ordering': "('sortkey', 'year_published', 'title')", 'object_name': 'Book'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['library.Author']", 'symmetrical': 'False'}),
            'comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['library.Location']", 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'origkey': ('django.db.models.fields.CharField', [], {'max_length': '36', 'null': 'True', 'blank': 'True'}),
            'sortkey': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {}),
            'year_published': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'library.location': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Location'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'unique': 'True'})
        }
    }

    complete_apps = ['library']