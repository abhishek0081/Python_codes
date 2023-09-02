import paramiko


def get_disk_utilization(server_ip, username, password):
    """Gets disk utilization information on the target server."""
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(server_ip, username=username, password=password)
    except paramiko.AuthenticationException as auth_error:
        print(f"Authentication failed: {auth_error}")
        return None
    except paramiko.SSHException as ssh_error:
        print(f"SSH connection error: {ssh_error}")
        return None

    try:
        # Run the 'df' command to get disk utilization
        command = "df -h"  # -h option for human-readable output
        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode()

        # Split the output into lines and extract relevant information
        lines = output.strip().split('\n')

        # The first line contains column headers, so skip it
        lines = lines[1:]

        disk_utilization = []

        for line in lines:
            # Split each line into columns (fields)
            columns = line.split()

            # Extract relevant information (e.g., Filesystem, Size, Used, Avail, Use%)
            filesystem = columns[0]
            size = columns[1]
            used = columns[2]
            available = columns[3]
            use_percentage = columns[4]

            # Append the information to the disk_utilization list
            disk_utilization.append({
                "Filesystem": filesystem,
                "Size": size,
                "Used": used,
                "Available": available,
                "Use%": use_percentage,
            })

        return disk_utilization

    except Exception as e:
        print(f"Error retrieving disk utilization: {e}")
        return None
    finally:
        ssh.close()


if __name__ == "__main__":
    server_ip = "servera"
    username = "student"
    password = "student"

    disk_info = get_disk_utilization(server_ip, username, password)

    if disk_info:
        for item in disk_info:
            print(item)
    else:
        print("Unable to retrieve disk utilization.")