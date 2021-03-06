""" FileSerializer to serialize FieldFile ***Date, ImageFieldFile, FileField, FieldFile for Json*** """

from datetime import date
from decimal import Decimal
from django.db.models.fields.files import ImageFieldFile, FileField, FieldFile


class BaseSerializer(object):
    def serialize(self, value):
        return value


class DateSerializer(BaseSerializer):
    def serialize(self, value):
        return str(value)


class DecimalSerializer(BaseSerializer):
    def serialize(self, value):
        return str(value)


class FileSerializer(BaseSerializer):
    def serialize(self, value):
        try:
            return value.url
        except:
            return None


def serialize_field(value):
    if isinstance(value, date):
        return DateSerializer().serialize(value)
    if isinstance(value, Decimal):
        return DateSerializer().serialize(value)
    if isinstance(value, ImageFieldFile) or isinstance(value, FileField) or isinstance(value, FieldFile):
        return FileSerializer().serialize(value)
    return value