import threading
import time
import sys
import mechanize

def getResult(universityName,url,userName,password):
    if(len(userName)==0):
        return
    logLevel=0 #by default no log
    UniversityStatusPrint=True #if get type=1 make it false
    if(len(sys.argv)>1):
        logLevel=int(sys.argv[1])
    if(len(sys.argv)>2):
        getType=int(sys.argv[2])

    b = mechanize.Browser()
    b.set_handle_robots(False)
    
    r1 = b.open(url)

    if(universityName=="Purdue"):
        b.select_form(name="frmApplicantConnectLogin")
        b["UserID"]=userName
        b["Password"]=password
    elif(universityName=="NEU"):
        b.select_form(name="Form1")
        b["txtUserName"]=userName
        b["txtPassword"]=password
        UniversityStatusPrint=False
    elif(universityName=="ASU" or universityName=="TAMU" or universityName=="UFL"):
        b.select_form(nr=0)
        b["username"]=userName
        b["password"]=password
    elif(universityName=="SUNYSB"):
        b.select_form(nr=0)
        b["UserID"]=userName
        b["Password"]=password
    elif(universityName=="vtech"):
        b.select_form(name="loginForm")
        b["txtUserID"]=userName
        b["txtPassword"]=password
    elif(universityName=="TAMU"):
        result= s[s.find('class="highlight">')+18:s.find(" </span>\r\n")-3]
    elif(universityName=="UCSD"):
        b.select_form(nr=1)
        b["aemail"]=userName
        b["apass"]=password
    elif(universityName=="USC" or universityName=="UNC"):
        b.select_form(nr=0)
        b["UserID"]=userName
        b["Password"]=password
    elif(universityName=="UCI"):
        b.select_form(nr=0)
        b["login[email]"]=userName
        b["login[password]"]=password
	
    if(logLevel>=1):
        print universityName,"login in progress..."
    r2 = b.submit()

    if(logLevel>=1):
        print "logged in successfully..."
    
    s=r2.read()

    if(logLevel==2):
        name1=''.join((universityName,'1.html'))
        name2=''.join((universityName,'2.html'))

        Html_file= open(name1,"w")
        Html_file.write(r1.read())
        Html_file.close()

        Html_file= open(name2,"w")
        Html_file.write(r2.read())
        Html_file.close()



    result="failed to get result."
    
    if(universityName=="Purdue"):
        result=s[s.find("<li><h4>")+1:s.find("</h4></li>")]
        result=result[7:]
    elif(universityName=="ASU"):
        result=s[s.find('app-status">')+12:s.find('app-status">')+21]
    elif(universityName=="SUNYSB"):
        result= s[s.find("Status")+1:s.find(" <img")]
        result=result[7:]
    elif(universityName=="vtech"):
        result= s[s.find('tableBottomBorder">')+1:s.find('<br><div class="info">')]
        result=result[-9:]
    elif(universityName=="USC" or universityName=="UNC"):
        result= s[s.find("Status")+1:s.find(" <img")]
        result=result[7:]
    elif(universityName=="NEU"):
        result= s[s.find("Status")+1:s.find(" <img")]
        result=result[7:]
        processNEUResult(result)
    elif(universityName=="TAMU"):
        result= s[s.find('class="highlight">')+18:s.find(" </span>\r\n")-3]
    elif(universityName=="UCSD"):
        result= s[s.find('<span class="value"><span class="Good">')+1:s.find("</span></span>")]
        result=result[38:]
    elif(universityName=="UFL"):
        result=s[s.find('Admission Decision</span>: </td><td style="border: 0; width: 60%">')+66:s.find('Admission Decision</span>: </td><td style="border: 0; width: 60%">')+81]
    elif(universityName=="UCI"):
        result_start_index = s.find('Your application status is: ')+31
        result_start = s[result_start_index:]
        result_end_index = result_start.find('</b>')
        result= result_start[:result_end_index]

    if(UniversityStatusPrint):
        print universityName,"Status :",result
    print "----x----"

    
def processNEUResult(result) :
    if not "<span class=\"green\"> Application Submitted</span>" in result:
        print "Application Submitted: False"
    else:
        print "Application Submitted: True"
        
    if not "<span class=\"green\"> App Materials Received</span>" in result:
        print "Application Materials Received: False"
    else:
        print "Application Materials Received: True"
    
    if not "<span class=\"green\"> My Decision Is Ready</span>" in result:
        print "Decision Ready: False"
    else:
        print "Decision Ready: True"
   

# Fill details of the universities of which you want to check status. Keep the rest as it is. 

purdueUserName=""
purduePass=""

asuUserName=""
asuPass=""

sunySBUserName=""
sunySBPass=""

vtechUserName=""
vtechPass=""

neuUserName=""
neuPass=""

tamuUserName=""
tamuPass=""

ucsdUserName=""
ucsdPass=""

uscUserName=""
uscPass=""

uflUserName=""
uflPass=""

#UCI gats tracker email and password
uciUserName=""
uciPass=""

#UNC pin and password
uncUserName=""
uncPass=""


class myThread (threading.Thread):
    def __init__(self, threadID, universityName, url, userName, password):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.universityName = universityName
        self.url = url
        self.userName = userName
        self.password = password
    def run(self):
        getResult(self.universityName,self.url,self.userName,self.password)

# Create new threads
thread1 = myThread(1,"Purdue","https://app.applyyourself.com/AYApplicantLogin/fl_ApplicantConnectLogin.asp?id=purduegrad",purdueUserName,purduePass)
thread2 = myThread(2, "ASU","https://webapp4.asu.edu/myasu/",asuUserName,asuPass)
thread3 = myThread(3,"SUNYSB","https://app.applyyourself.com/ayapplicantlogin/fl_ApplicantLogin.asp?ID=sunysb-gs#tab2",sunySBUserName,sunySBPass)
thread4 = myThread(4,"vtech","https://gradapp.stl.vt.edu/pages/login.php",vtechUserName,vtechPass)
thread5 = myThread(5,"NEU","https://neugrad.askadmissions.net/vip/Default.aspx",neuUserName,neuPass)
thread6 = myThread(6,"TAMU","https://cas.tamu.edu/cas/login?service=https://applicant.tamu.edu/Account/Login",tamuUserName,tamuPass)
thread7 = myThread(7,"UCSD","https://gradapply.ucsd.edu/account/index.php?node=d56b699830e77ba53855679cb1d252da",ucsdUserName,ucsdPass)
thread8 = myThread(8,"USC","https://app.applyyourself.com/AYApplicantLogin/fl_ApplicantLogin.asp?id=usc-grad",uscUserName,uscPass)
thread9 = myThread(9,"UFL","https://www.cise.ufl.edu/academics/grad/prospective/gait/index.php",uflUserName,uflPass)
thread10 = myThread(10,"UCI","https://gats.ics.uci.edu/tracker/",uciUserName,uciPass)
thread11 = myThread(11,"UNC","https://app.applyyourself.com/AYApplicantLogin/fl_ApplicantLogin.asp?id=unc-ch",uncUserName,uncPass)

# Start new Threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
thread7.start()
thread8.start()
thread9.start()
thread10.start()
thread11.start()
