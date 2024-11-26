resource "aws_subnet" "public" {
  count                  = length(var.public_subnets)
  vpc_id                = aws_vpc.main.id
  cidr_block            = var.public_subnets[count.index]
  availability_zone     = var.availability_zones[count.index]
  map_public_ip_on_launch = true
  tags                  = merge(var.tags, { "Name" = "Public Subnet ${count.index + 1}" })
}

resource "aws_subnet" "private" {
  count                  = length(var.private_subnets)
  vpc_id                = aws_vpc.main.id
  cidr_block            = var.private_subnets[count.index]
  availability_zone     = var.availability_zones[count.index]
  tags                  = merge(var.tags, { "Name" = "Private Subnet ${count.index + 1}" })
}
