import sys

def writting(V, r, tau, t_max):
    original = sys.stdout
    ouf = open('D:\\redmine_svn\\497\\work\\progs\\telemetr_for_errors_bins.txt', 'w')
    sys.stdout = ouf
    for t in range(int(t_max/tau)):
        print r[t][0], r[t][2], V[t][0], V[t][1], V[t][2]
       #ouf.writelines(line)
    # sys.stdout
    ouf.close()