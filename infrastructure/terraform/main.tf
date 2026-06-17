# Terraform — Infraestructura como código (PLANTILLA DE EJEMPLO).
#
# Este archivo es ilustrativo. Define UNA instancia de servidor en AWS
# donde correría la app. NO lo apliques hasta tener una cuenta de AWS
# configurada y entender los costos.
#
# Para empezar con CI/CD, ignora esta carpeta y usa solo GitHub Actions.

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

resource "aws_instance" "taskflow_server" {
  ami           = var.ami_id
  instance_type = var.instance_type

  tags = {
    Name        = "taskflow-server"
    Environment = var.environment
  }
}
