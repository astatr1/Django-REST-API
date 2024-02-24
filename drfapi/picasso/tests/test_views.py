from django.test import TestCase
from django.utils import timezone

from ..models import File
from ..tasks import upload_file


class TaskFileProcessingTests(TestCase):
    """Задача обработки полученного файла"""

    def test_file_processing(self):
        file = File.objects.create(file='files/%Y/%m/%d/test.txt',
                                   uploaded_at=timezone.now(),
                                   processed=False)
        upload_file(file.id)
        file.refresh_from_db()
        self.assertTrue(file.processed)
