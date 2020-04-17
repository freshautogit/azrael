from django.db import models


class FullRights(models.Model):
    class Meta:
        permissions = (
            ('full_search', 'Can use full search'),
            ('add_person', 'Can add new persons to the DB'),
            ('add_info', 'Can add new info to the DB'),
            ('can_delete', 'Can delete persons from the DB'),
            ('can_edit', 'Can edit info in the DB'),
        )


class News(models.Model):
    id = models.AutoField(primary_key=True)
    post_type = models.CharField(max_length=50, null=True)
    post_subject = models.CharField(max_length=50, null=True)
    post_text = models.TextField(null=True)
