import os
import time
from django.conf import settings
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Clears expired file-based cache entries."

    def handle(self, *args, **kwargs):
        cache_backend = settings.CACHES['default']['BACKEND']
        if 'FileBasedCache' not in cache_backend:
            self.stdout.write("Default cache is not file-based. No action taken.")
            return

        cache_dir = settings.CACHES['default']['LOCATION']
        now = time.time()

        expired_files = 0
        for root, dirs, files in os.walk(cache_dir):
            for filename in files:
                file_path = os.path.join(root, filename)
                try:
                    # Get file's last modification time
                    if os.path.getmtime(file_path)+settings.CACHE_TIMEOUT < now:
                        os.remove(file_path)
                        expired_files += 1
                except Exception as e:
                    self.stderr.write(f"Error deleting {file_path}: {e}")

        self.stdout.write(f"Deleted {expired_files} expired cache files.")
