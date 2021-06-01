import utile
import numpy as np
from EdgeServerless import *
from learning import update_funcdp,get_reward
Tpc = 5
Tpi = 10
Tpe = 15
Cc  = 10
Ci  = 3
Ce  = 2
lambda_si = 2
lambda_se = 4
Numfunc = 5
Nclient = 200

ai = np.ones((lambda_si, Numfunc))
bi = np.ones((lambda_si, Numfunc))
ae = np.ones((lambda_se, Numfunc))
be = np.ones((lambda_se, Numfunc))
Rs =[]
R = -1
sc,si,se = init_network(lambda_si,lambda_se)
func = init_func(Numfunc)
clt = new_client(func,Nclient,Numfunc)
si,se = update_funcdp(ai, bi,  Ci, ae, be, Ce,si,se,func)
clt, T, sc, si, se = processing(clt,sc,si,se,func,Tpc,Tpi,Tpe)
Rs.append(np.mean(T))
for i in range (200):
    clt, T, sc, si, se = processing(clt,sc,si,se,func,Tpc,Tpi,Tpe)
    R = (0.5*np.mean(T)+0.5*(max(Rs)-min(Rs)))/min(Rs)/5
    ai,bi,ae,be = get_reward(ai,bi,ae,be, si, se, func,R)
    si, se = update_funcdp(ai, bi,  Ci, ae, be, Ce,si,se,func)
    Rs.append(np.mean(T))
    if i > 195:
        print('iteration', i )
        for j in range(lambda_si):
            print(si[j].func)
        for j in range(lambda_se):
            print(se[j].func)


fig, ax = plt.subplots()
ax.plot(np.arange(0,len(Rs),1), Rs, alpha=0.5, color = 'blue')
plt.show()








# fig, ax = plt.subplots()
# ax.scatter(sc.loc[0], sc.loc[1], alpha=0.5, color = 'r')
# for i in range(len(si)):
#     ax.scatter(si[i].loc[0], si[i].loc[1], alpha=0.5, color = 'blue')
# for i in range(len(se)):
#     ax.scatter(se[i].loc[0], se[i].loc[1], alpha=0.5, color = 'g')
# for i in range(len(si)):
#     ax.plot([si[i].loc[0],si[i].up.loc[0]],[si[i].loc[1],si[i].up.loc[1]],color = 'lightgray')
# for i in range(len(se)):
#     ax.plot([se[i].loc[0],se[i].up.loc[0]],[se[i].loc[1],se[i].up.loc[1]],color = 'lightgray')
# ax.grid(True)
# fig.tight_layout()
#
# plt.show()