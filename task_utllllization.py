import paramiko
import re
import csv

def connect_to_server(server_ip, username, password):
    """Connects to the target server via SSH."""
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(server_ip, username=username, password=password)
        print("Connected to the server.")
        return ssh
    except paramiko.AuthenticationException as auth_error:
        print(f"Authentication failed: {auth_error}")
    except paramiko.SSHException as ssh_error:
        print(f"SSH connection error: {ssh_error}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return None

def get_cpu_utilization(ssh):
    """Gets the CPU utilization of the target server."""
    try:
        command = "top -bn1 | grep 'Cpu(s)'"
        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode()

        cpu_utilization = None
        print(output.splitlines())
        for line in output.splitlines():
            match = re.match(r'%Cpu\(s\):\s+(\d+\.\d+)\s+us', line)
            if match:
                cpu_utilization = float(match.group(1))
                break

        return cpu_utilization
    except Exception as e:
        print(f"Error retrieving CPU utilization: {e}")
        return None

def get_memory_utilization(ssh):
    """Gets the memory utilization of the target server."""
    try:
        command = "free | grep Mem | awk '{print $3/$2 * 100}'"
        stdin, stdout, stderr = ssh.exec_command(command)
        memory_utilization = float(stdout.read().decode().strip())
        return memory_utilization
    except Exception as e:
        print(f"Error retrieving memory utilization: {e}")
        return None

def get_uptime(ssh):
    """Gets the uptime of the target server."""
    try:
        command = "uptime -p"
        stdin, stdout, stderr = ssh.exec_command(command)
        uptime = stdout.read().decode().strip()
        return uptime
    except Exception as e:
        print(f"Error retrieving uptime: {e}")
        return None

def collect_and_append_utilization_data(server_ip, username, password, output_file):
    """Collects utilization data and saves it to a CSV file."""
    ssh = connect_to_server(server_ip, username, password)
    if not ssh:
        print("Unable to connect to the server.")
        return

    cpu_utilization = get_cpu_utilization(ssh)
    memory_utilization = get_memory_utilization(ssh)
    uptime = get_uptime(ssh)

    print(cpu_utilization)
    print(memory_utilization)
    print(uptime)

    ssh.close()

    if cpu_utilization is None or memory_utilization is None or uptime is None:
        print("Unable to retrieve utilization information.")
        return

    # Save the utilization data to a CSV file
    try:
        # Check if the CSV file already exists
        file_exists = False
        try:
            with open(output_file, mode="r") as csv_file:
                csv_reader = csv.reader(csv_file)
                header = next(csv_reader)  # Read the header row
                if header:
                    file_exists = True
        except FileNotFoundError:
            pass

        with open(output_file, mode="a", newline='') as csv_file:
            writer = csv.writer(csv_file)
            if not file_exists:
                # Write the header row only if the file didn't exist previously
                writer.writerow(["Server Name", "CPU Utilization (%)", "Memory Utilization (%)", "Uptime"])
            writer.writerow([server_ip, cpu_utilization, memory_utilization, uptime])

        print(f"Utilization data appended to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    server_ip = "workstation"
    username = "student"
    password = "student"
    output_file = "utilization_report.csv"
    collect_and_append_utilization_data(server_ip, username, password, output_file)