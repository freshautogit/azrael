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
