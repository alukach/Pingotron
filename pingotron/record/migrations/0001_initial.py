# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PlayerProfile'
        db.create_table('record_playerprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('alias', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('avatar', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('quote', self.gf('django.db.models.fields.CharField')(max_length=240, blank=True)),
        ))
        db.send_create_signal('record', ['PlayerProfile'])

        # Adding model 'Game'
        db.create_table('record_game', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('winner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='win', to=orm['auth.User'])),
            ('winnerScore', self.gf('django.db.models.fields.IntegerField')()),
            ('loser', self.gf('django.db.models.fields.related.ForeignKey')(related_name='loss', to=orm['auth.User'])),
            ('loserScore', self.gf('django.db.models.fields.IntegerField')()),
            ('targetScore', self.gf('django.db.models.fields.IntegerField')(default='11')),
            ('gameDateTime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 12, 1, 0, 0), blank=True)),
            ('dateCreated', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 12, 1, 0, 0), auto_now_add=True, blank=True)),
            ('createdBy', self.gf('django.db.models.fields.related.ForeignKey')(related_name='createdrecord_game_related', to=orm['auth.User'])),
            ('lastModified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('modifiedBy', self.gf('django.db.models.fields.related.ForeignKey')(related_name='modifiedrecord_game_related', to=orm['auth.User'])),
            ('stakeValue', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('stakeUnit', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
        ))
        db.send_create_signal('record', ['Game'])


    def backwards(self, orm):
        # Deleting model 'PlayerProfile'
        db.delete_table('record_playerprofile')

        # Deleting model 'Game'
        db.delete_table('record_game')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'record.game': {
            'Meta': {'object_name': 'Game'},
            'createdBy': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'createdrecord_game_related'", 'to': "orm['auth.User']"}),
            'dateCreated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 12, 1, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'gameDateTime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 12, 1, 0, 0)', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastModified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'loser': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'loss'", 'to': "orm['auth.User']"}),
            'loserScore': ('django.db.models.fields.IntegerField', [], {}),
            'modifiedBy': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'modifiedrecord_game_related'", 'to': "orm['auth.User']"}),
            'stakeUnit': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'stakeValue': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'targetScore': ('django.db.models.fields.IntegerField', [], {'default': "'11'"}),
            'winner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'win'", 'to': "orm['auth.User']"}),
            'winnerScore': ('django.db.models.fields.IntegerField', [], {})
        },
        'record.playerprofile': {
            'Meta': {'object_name': 'PlayerProfile'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quote': ('django.db.models.fields.CharField', [], {'max_length': '240', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['record']