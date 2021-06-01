from Envgenefunc import PPP,dpp
import matplotlib.pyplot as plt
import server
import utile
import client
import math


# define network, including servers, connections
def init_network(lambda_si,lambda_se):
    si =[]
    se =[]
    loc_sc =(0,0)
    loc_si = PPP(lambda_si)
    loc_se = PPP(lambda_se)
    sc= server.server()
    sc.loc = loc_sc
    for i in range(len(loc_si)):
        s = server.server()
        s.loc = loc_si[i]
        s.up = sc
        s.updis = utile.disance(s.loc,sc.loc)
        si.append(s)
    sc.down = si
    for i in range(len(loc_se[0])):
        d = []
        s = server.server()
        s.loc = [loc_se[0][i],loc_se[1][i]]
        for i in range(len(loc_si)):
            d.append(utile.disance(s.loc,si[i].loc))
        s.up = si[d.index(min(d))]
        s.updis = min(d)
        si[d.index(min(d))].down = s
        se.append(s)
    return sc,si,se

# define the name of functions
def init_func(Numfunc):
    func = []
    for i in range(Numfunc):
        func.append('f' + str(i + 1))
    return func

# define clients, including location and requested functions
def new_client(func,Nclient,Numfunc):
    clt=[]
    loc_client = dpp(Nclient,1000,2)
    for i in range(Nclient):
        fc = utile.zipf(Numfunc, 1.4, func)
        clt.append(client.client(loc_client[i],fc))
    return clt


def processing(clt,sc,si,se,func,Tpc,Tpi,Tpe):
    sc.func = func
    T = []
    for i in range(len(clt)):
        d=[]
        for j in range(len(se)):
            d.append(utile.disance(se[j].loc,clt[i].loc))
        clt[i].access= se[d.index(min(d))]
        clt[i].due = min(d) # define access by edge
#       request arrives edge
        se[d.index(min(d))].history.append(clt[i].func)
        if clt[i].func[0] in clt[i].access.func:
            t = Tpe + pathdelay(clt[i].due)
        else:
            intermediate = clt[i].access.up
            intermediate.history.append((clt[i].func))
            if clt[i].func[0] in intermediate.func:
                t = Tpi + pathdelay(clt[i].due) + pathdelay(clt[i].access.updis)
            else:
                #       request arrives inter
                t = Tpc + pathdelay(clt[i].due) + pathdelay(clt[i].access.updis) + pathdelay(utile.disance(sc.loc,intermediate.loc))
        clt[i].latency = t
        T.append(t)
    return clt,T, sc, si, se










def pathdelay(d):
    return 2*math.exp(d)