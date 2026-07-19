resource "random_id" "bucket" {
  byte_length = 4
}

resource "aws_s3_bucket" "cloudtrail_logs" {
  bucket = "${var.project_name}-logs-${random_id.bucket.hex}"

  tags = local.common_tags
}