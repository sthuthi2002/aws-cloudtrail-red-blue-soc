output "bucket_name" {
  value = aws_s3_bucket.cloudtrail_logs.bucket
}

output "instance_id" {
  value = aws_instance.red_blue_vm.id
}

output "public_ip" {
  value = aws_instance.red_blue_vm.public_ip
}

output "private_ip" {
  value = aws_instance.red_blue_vm.private_ip
}

output "security_group_id" {
  value = aws_security_group.red_blue_sg.id
}