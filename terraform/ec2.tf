data "aws_ami" "amazon_linux" {

  most_recent = true

  owners = ["amazon"]

  filter {
    name = "name"

    values = [
      "al2023-ami-*-x86_64"
    ]
  }
}

resource "aws_instance" "red_blue_vm" {

  ami = data.aws_ami.amazon_linux.id

  instance_type = "t3.micro"

  vpc_security_group_ids = [
    aws_security_group.red_blue_sg.id
  ]

  tags = merge(
    local.common_tags,
    {
      Name = "RedBlueLab"
    }
  )
}

