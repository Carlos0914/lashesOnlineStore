from storages.backends.s3boto3 import S3Boto3Storage
import uuid


class MediaStorage(S3Boto3Storage):
    def _save(self, name, content):
        new_name = name.split('.')
        extention = ''.join([new_name[0], '_', str(uuid.uuid4
                                                   ().hex[:12]) + '.'+str(new_name[-1]), ])
        return super()._save(extention, content=content)
    bucket_name = 'lashes-and-nails-app-assets'
    location = 'media'


class StaticStorage(S3Boto3Storage):
    bucket_name = 'lashes-and-nails-app-assets'
    location = 'static'
