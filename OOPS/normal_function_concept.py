import os
def tomcat_details(server_xml):
    global tcf,th
    tcf=server_xml
    th=os.path.dirname(os.path.dirname(server_xml))
    return None

def display():
    print(f"config file is : {tcf}\nHome is : {th}")
    return None

def main():
    tomcat7="/home/Automation/tomcat7/conf/server.xml"
    tomcat9="/home/Automation/tomcat9/conf/server.xml"
    tomcat_details(tomcat7)
    tomcat_details(tomcat9)

    display()




if __name__=='__main__':
    main()
   