

from django.conf import settings

from core.apps import CoreConfig


def image_upload(type, file, id):
    bucket = settings.AWS_S3_BUCKET_NAME
    file_name = f'{type}/{id}'
    print('file name>>>>', file_name)
    CoreConfig.s3.put_object(
        Bucket=bucket, Key=file_name, Body=file, ContentType="image/png", ACL='public-read')
    location = CoreConfig.s3.get_bucket_location(
        Bucket=bucket)['LocationConstraint']
    url = "https://s3-%s.amazonaws.com/%s/%s" % (location, bucket, file_name)
    return url
