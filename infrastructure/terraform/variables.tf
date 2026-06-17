# Variables de entrada de la infraestructura.
# Separar las variables del main.tf es una buena práctica:
# permite reutilizar la misma infraestructura con distintos valores.

variable "aws_region" {
  description = "Región de AWS donde se crean los recursos"
  type        = string
  default     = "us-east-1"
}

variable "ami_id" {
  description = "ID de la imagen de máquina (AMI) para el servidor"
  type        = string
  default     = "ami-0c101f26f147fa7fd"
}

variable "instance_type" {
  description = "Tipo de instancia EC2"
  type        = string
  default     = "t2.micro"
}

variable "environment" {
  description = "Entorno de despliegue (dev, staging, prod)"
  type        = string
  default     = "dev"
}
