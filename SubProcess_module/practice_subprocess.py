import subprocess
cmd="bash --version".split()
print(f'{cmd}-->command after spilit function\n')
sp=subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
print("Waiting For CMD to Store")
rc=sp.wait()
out,err=sp.communicate()
if rc==0:
    for i in out.splitlines():
        if "version" in i and "release" in i:
            print(i)
else:
    print(f"Error: {err}")
