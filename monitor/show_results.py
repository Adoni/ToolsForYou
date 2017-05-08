from matplotlib import pyplot as plt
import sys

def show_results(file_name):
    with open(file_name) as f:
        print(f.readline())
        print(f.readline())
        print(f.readline())
        y1=[]
        y2=[]
        for i,line in enumerate(f):
            line=line.strip().split(' ')
            y1.append(line[3])
            y2.append(line[4])
        x=range(len(y1))
    plt.plot(x,y1,label='rss')
    plt.plot(x,y2,label='vms')
    plt.legend()
    plt.show()


if __name__=='__main__':
    show_results(sys.argv[1])
