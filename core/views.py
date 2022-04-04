from django.conf import settings
from django.shortcuts import redirect

from core.apps import CoreConfig


def validation(request, filename):
    if request.method == 'GET':
        bucket = settings.AWS_S3_BUCKET_NAME

        location = CoreConfig.s3.get_bucket_location(
            Bucket=bucket)['LocationConstraint']
        url = "https://s3-%s.amazonaws.com/%s/static/%s" % (
            location, bucket, filename)
        return redirect(url)


def pki_validation(request, filename):
    if request.method == 'GET':
        bucket = settings.AWS_S3_BUCKET_NAME

        location = CoreConfig.s3.get_bucket_location(
            Bucket=bucket)['LocationConstraint']
        url = "https://s3-%s.amazonaws.com/%s/static/%s" % (
            location, bucket, filename)
        return redirect(url)
