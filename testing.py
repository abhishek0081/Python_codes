import paramiko
from cryptography.hazmat.backends import default_backend
import re

def get_cpu_utilization(server_ip, username, password):
  """Gets the CPU utilization of the target server."""
  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())    
  ssh.connect(server_ip, username=username, password=password)
  command = "top -bn1 | grep 'Cpu(s)'"
  stdin, stdout, stderr = ssh.exec_command(command)
    
  lines = stdout.read().decode().splitlines()
  print(lines)
  cpu_pattern = r"%Cpu\(s\):\s+(\d+\.\d+)\s+us"
  cpu_utilization = -1
  for line in lines:
    check = re.match(cpu_pattern, line)
    if check:
      cpu_utilization = float(check.group(1))
      break
  ssh.close()
  return cpu_utilization

          

if __name__ == "__main__":
    server_ip = "workstation"
    username = "student"
    password = "student"
    cpu_utilization = get_cpu_utilization(server_ip, username, password)  
    print(f"CPU Utilization is : {cpu_utilization}")      
