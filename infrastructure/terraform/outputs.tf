# Salidas: valores que Terraform muestra tras crear la infraestructura.
# Útiles para conectar (por ejemplo, la IP pública del servidor).

output "server_public_ip" {
  description = "IP pública del servidor de la app"
  value       = aws_instance.taskflow_server.public_ip
}

output "server_id" {
  description = "ID de la instancia creada"
  value       = aws_instance.taskflow_server.id
}
