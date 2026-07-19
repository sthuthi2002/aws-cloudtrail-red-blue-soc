resource "aws_cloudtrail" "red_blue_trail" {

  name = "${var.project_name}-trail"

  s3_bucket_name = aws_s3_bucket.cloudtrail_logs.id

  include_global_service_events = true

  is_multi_region_trail = true

  enable_logging = true

  depends_on = [
    aws_s3_bucket_policy.cloudtrail
  ]

  tags = local.common_tags
}