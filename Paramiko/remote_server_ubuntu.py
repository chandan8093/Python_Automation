import paramiko
#C:\\Users\\Admin\\Desktop\\ELK Stack\\elk-stack\\elk-stack-key
#Craete a ssh client
ssh=paramiko.SSHClient()
#automatically conncet to server 
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#To coonect to your server
ssh.connect(hostname="3.15.149.59",username="ubuntu",key_filename="C:\\Users\\Admin\\Desktop\\ELK Stack\\elk-stack\\elk-stack-key.pem",port=22)
stdin, stdout, stderr=ssh.exec_command("cd root")

print(f"The list {stdout.readlines()}")
print(f'Error : {stderr.readlines()}')

ssh.close()
