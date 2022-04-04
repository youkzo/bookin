from django.conf import settings
from django.shortcuts import redirect

from core.apps import CoreConfig


def validation(request):
    if request.method == 'GET':
        bucket = settings.AWS_S3_BUCKET_NAME
        file_name = settings.FILE_NAME

        location = CoreConfig.s3.get_bucket_location(
            Bucket=bucket)['LocationConstraint']
        url = "https://s3-%s.amazonaws.com/%s/%s" % (
            location, bucket, file_name)
        return redirect(url)
