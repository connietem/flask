from bottle import request,post,run,route,template
AQ=[]
M=[]
MC=[]

@route('/')
def index():
    return template('index.html')
@post('/')
def readNums():
    m_minus=0
    q_minus=0
    postdata=request.body.read()
    print(postdata)
    m=request.forms.get("m")
    q=request.forms.get("q")
    if(int(m)<0):
        m=int(int(m)*-1)
        m_minus=1
    if(int(q)<0):
        q=int(int(q)*-1)
        q_minus=1
    global AQ,M,MC
    A=[0,0,0,0]
    AQ=[]
    M=[]
    Q=[]
    MC=[]

    binM="{0:04b}".format(int(m))
    for i in binM:
        M.append(int(i))
    print("M:",M)
    MC=complement(M,3)

    binQ="{0:04b}".format(int(q))
    for i in binQ:
        Q.append(int(i))
    print("Q:",Q)

    if m_minus==1:
        M,MQ=MQ,M
    if q_minus==1:
        Q=complement(Q,3)
    Q.append(0)
    AQ=A+Q
    
    print("AQ:",AQ)
    for i in range(len(M)):
        if AQ[7]==AQ[8]:
            shift()
            print("S:",AQ)
        elif(AQ[7:]==[0,1]):
            add()
            print("Add:",AQ)
            shift()
            print("S:",AQ)
        else:
            sub()
            print("SUB:",AQ)
            shift()
            print("S:",AQ)
    AQ=AQ[:len(AQ)-1]
    print("AQ:",AQ)
    comp=''.join(str(e) for e in AQ)
    if(AQ[0]==1):
        AQ=complement(AQ,7)
    print(AQ)

    binary=''.join(str(e) for e in AQ)
    print(binary)

    if(q_minus^m_minus)==1:
        return "Result in Decimal: -{0} <br> In Binary: {1}".format(int(binary,2),comp)
    return "Result in Decimal: {0} <br> In binary: {1}".format(int(binary,2),binary)

def complement(arr,n):
    arr_com=[]
    for i in arr:
        if int(i)==0:
            arr_com.append(1)
        else:
            arr_com.append(0)
    c=1
    for i in range(n,-1,-1):
        arr_com[i]=arr_com[i]+c
        if arr_com[i]==2:
            arr_com[i]=0
            c=1
        else:
            return(arr_com)

def shift():
    global AQ
    AQ=AQ[:len(AQ)-1]
    AQ.insert(0,AQ[0])

def add():
    global AQ,M
    c=0
    for i in range(3,-1,-1):
        AQ[i]=AQ[i]+M[i]+c
        if(AQ[i]==3):
            AQ[i]=1
            c=1
        elif AQ==2:
            AQ[i]=0
            c=1
        else:
            c=0

def sub():
    global AQ
    c=0
    for i in range(3,-1,-1):
        AQ[i]=AQ[i]+MC[i]+c
        if AQ[i]==3:
            AQ[i]=1
            c=1
        elif AQ[i]==2:
            AQ[i]=0
            c=1
        else:
            c=0

run(host='localhost', port=8080)
            
