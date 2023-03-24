resource "aws_s3_bucket" "this" {
bucket_prefix = "mvws9-leigh-e"
force_destroy = true
tags = {
Name = "multiverse"
}
}
resource "aws_s3_bucket_acl" "this" {
bucket = aws_s3_bucket.this.id
acl = "private"
}
resource "aws_s3_object" "this" {
bucket = aws_s3_bucket.this.id
key = "results.csv"
source = "${path.module}/results.csv"
etag = filemd5("${path.module}/results.csv")
}
