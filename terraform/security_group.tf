resource "aws_security_group" "red_blue_sg" {

  name        = "${var.project_name}-sg"
  description = "Security Group for Red Blue Lab"

  ingress {
    description = "SSH"

    from_port = 22
    to_port   = 22
    protocol  = "tcp"

    cidr_blocks = [
      "0.0.0.0/0"
    ]
  }

  egress {

    from_port = 0
    to_port   = 0
    protocol  = "-1"

    cidr_blocks = [
      "0.0.0.0/0"
    ]
  }

  tags = local.common_tags
}
