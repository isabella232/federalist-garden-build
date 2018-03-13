import boto3

from moto import mock_s3

from invoke import MockContext

from tasks import publish


class TestPublish():
    @mock_s3
    def test_it_is_callable(self, monkeypatch):
        monkeypatch.setenv('AWS_ACCESS_KEY_ID', 'fake-access-key')
        monkeypatch.setenv('AWS_SECRET_ACCESS_KEY', 'fake-secret-key')

        ctx = MockContext()

        aws_region = 'region'
        bucket = 'bucket'

        conn = boto3.resource('s3', region_name=aws_region)

        # We need to create the bucket since this is all in
        # Moto's 'virtual' AWS account
        conn.create_bucket(Bucket=bucket)

        publish(ctx, base_url='/site/prefix', site_prefix='site/prefix',
                bucket=bucket, cache_control='max-age: boop',
                aws_region=aws_region, dry_run=False)
