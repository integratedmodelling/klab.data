"""This code goes inside the production-geoserver
and copies a file into de sistem (data/geoserver_transfer)"""
#command (Windows powershell): ssh bc3@192.168.250.1
#password: Sis-8905
import paramiko
import time

hostname = ''
username = ''
port = None
password = ''

#We set the parameters to create the connection to the server
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.connect(hostname, port, username, password)

commands =['docker exec -it demo_geoserver.1.o3h9jxv7suzw2srtxb29ekzc4 bash', 'cd /opt/geoserver/data_dir/', 'dir'
]

for command in commands:
      print(f"{'#'*10} Executing the Command : {command} {'#'*10}")
      stdin, stdout, stderr = ssh.exec_command(command)
      time.sleep(.5)
      print(stdout.read().decode())


#Execute first command and print the exit
# stdin, stdout, stderr = ssh.exec_command('docker ps')
# # for line in stdout: #(stdout = tupple)
# #   print(line)

# # We go inside the geoserver container
# stdin, stdout, stderr = ssh.exec_command('docker exec -it demo_geoserver.1.o3h9jxv7suzw2srtxb29ekzc4 bash')

# #we go to the dessired folder
# stdin, stdout, stderr = ssh.exec_command('cd /opt/geoserver/data_dir/')

# stdin, stdout, stderr = ssh.exec_command('dir')
# for line in stdout: #(line = string)
#   print(line)

ssh.close()