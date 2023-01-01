import os
class Tomcat:
    def tomcat_details(self,server_xml):
        #global tcf,th
        self.tcf=server_xml
        self.th=os.path.dirname(os.path.dirname(server_xml))
        return None

    def display(self):
        print(f"config file is : {self.tcf}\nHome is : {self.th}")
        return None

def main():
    tomcat7=Tomcat()
    tomcat9=Tomcat()
    
    tomcat7.tomcat_details("/home/Automation/tomcat7/conf/server.xml")
   
    tomcat9.tomcat_details("/home/Automation/tomcat9/conf/server.xml")
    tomcat9.display()
    tomcat7.display()
    




if __name__=='__main__':
    main()
   