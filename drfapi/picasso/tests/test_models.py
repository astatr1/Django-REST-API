from django.test import TestCase
from django.utils import timezone

from ..models import File


class FileModelTests(TestCase):
    """Проверка создания экземпляра модели File"""
    @classmethod
    def setUpTestData(cls):
        File.objects.create(file='test.txt',
                            uploaded_at=timezone.now(),
                            processed=False)

    def test_file_label(self):
        """Создание модели File, имя поля: file"""
        file = File.objects.get(id=1)
        field_label = file._meta.get_field('file').verbose_name
        self.assertEquals(field_label, 'file')

    def test_uploaded_at_label(self):
        """Создание модели File, имя поля: uploaded_at"""
        file = File.objects.get(id=1)
        field_label = file._meta.get_field('uploaded_at').verbose_name
        self.assertEquals(field_label, 'uploaded at')

    def test_processed_label(self):
        """Создание модели File, имя поля: processed"""
        file = File.objects.get(id=1)
        field_label = file._meta.get_field('processed').verbose_name
        self.assertEquals(field_label, 'processed')

    def test_name_upload_file(self):
        """Имя загруженного файла с расширением"""
        file = File.objects.get(id=1)
        file_name = file.file.name
        self.assertEquals(file_name, 'test.txt')

    def test_upload_to(self):
        """Путь загрузки файлов"""
        file = File.objects.get(id=1)
        self.assertEqual(file.file.field.upload_to, 'files/%Y/%m/%d')

    def test_processed(self):
        """Значение атрибута False при создании объекта"""
        file = File.objects.get(id=1)
        self.assertFalse(file.processed)
