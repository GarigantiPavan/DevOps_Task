
aws_region                   = "us-east-1"

vpc_cidr                     = "10.0.0.0/16"

public_subnets               = ["10.0.1.0/24",  "10.0.2.0/24"]

private_subnets              = ["10.0.3.0/24",  "10.0.4.0/24"]

availability_zones           = ["us-east-1a",  "us-east-1b"]

tags                         = { 
  Environment = "Production"
  Project     = "POCProject"
}

ssl_certificate_id = "arn:aws:acm:us-east-1:98549108098:certificate/d3f12042-6279-a90d-2995-6189judef01"


domain_name = "test.com"
