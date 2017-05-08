from matplotlib import pyplot as plt
import sys
import numpy


def line_plot(data_file):
    fontsize = 18
    with open(data_file) as f:
        xlabel = f.readline().strip()
        ylabel = f.readline().strip()
        line1_name = f.readline().strip()
        line2_name = f.readline().strip()
        x = []
        y1 = []
        y2 = []
        for line in f:
            line = line.strip().split('\t')
            print(line)
            x.append(float(line[0]))
            y1.append(float(line[1]))
            y2.append(float(line[2]))
        plt.plot(x, y1, label=line1_name)
        plt.plot(x, y2, label=line2_name)
        plt.xlabel(xlabel, fontsize=fontsize)
        plt.ylabel(ylabel, fontsize=fontsize)
        plt.legend(loc='center right', fontsize=fontsize)
        plt.tick_params(axis='x', labelsize=fontsize)
        plt.tick_params(axis='y', labelsize=fontsize)
        plt.tight_layout(pad=0.1)
        plt.savefig('%s.png' % (data_file))
        # plt.show()


def bar_plot(data_file):
    fontsize = 18
    width = 0.35  # the width of the bars: can also be len(x) sequence

    with open(data_file) as f:
        xlabel = f.readline().strip()
        ylabel = f.readline().strip()
        line1_name = f.readline().strip()
        name = []
        y1 = []
        for line in f:
            line = line.strip().split('\t')
            print(line)
            name.append(line[0])
            y1.append(float(line[1]))
        x = numpy.arange(len(y1))
        y1 = numpy.array(y1)
        p1 = plt.bar(x, y1, width,label=line1_name)

        plt.xlabel(xlabel, fontsize=fontsize)
        plt.ylabel(ylabel, fontsize=fontsize)

        plt.tick_params(axis='x', labelsize=fontsize)
        plt.tick_params(axis='y', labelsize=fontsize)
        plt.legend(loc='upper left', fontsize=fontsize)
        xlabels = plt.xticks(x, name, rotation=30, horizontalalignment='right')
        plt.tight_layout(pad=0.1)
        plt.savefig('%s.png' % (data_file))
        plt.show()


def stack_bar_plot(data_file):
    fontsize = 18
    width = 0.35  # the width of the bars: can also be len(x) sequence

    with open(data_file) as f:
        xlabel = f.readline().strip()
        ylabel = f.readline().strip()
        line1_name = f.readline().strip()
        line2_name = f.readline().strip()
        #line3_name = f.readline().strip()
        name = []
        y1 = []
        y2 = []
        #y3 = []
        for line in f:
            line = line.strip().split('\t')
            print(line)
            name.append(line[0])
            y1.append(float(line[1]))
            y2.append(float(line[2]))
            #y3.append(float(line[3]))
        x = numpy.arange(len(y1))
        y1 = numpy.array(y1)
        y2 = numpy.array(y2)
        #y3 = numpy.array(y3)
        p1 = plt.bar(x, y1, width,)
        p2 = plt.bar(x, y2, width, bottom=y1)
        #p3 = plt.bar(x, y3, width, bottom=y1 + y2)

        plt.xlabel(xlabel, fontsize=fontsize)
        plt.ylabel(ylabel, fontsize=fontsize)

        plt.tick_params(axis='x', labelsize=fontsize)
        plt.tick_params(axis='y', labelsize=fontsize)
        #plt.legend((p1[0], p2[0], p3[0]), (line1_name, line2_name, line3_name))
        plt.legend((p1[0], p2[0]), (line1_name, line2_name), loc='left', fontsize=fontsize)
        #plt.legend(loc='center right', fontsize=fontsize)
        xlabels = plt.xticks(x, name, rotation=30, horizontalalignment='right')
        plt.tight_layout(pad=0.1)
        plt.savefig('%s.png' % (data_file))
        plt.show()


def stack_line_plot(data_file):
    fontsize = 18
    width = 0.35  # the width of the bars: can also be len(x) sequence

    with open(data_file) as f:
        xlabel = f.readline().strip()
        ylabel = f.readline().strip()
        line1_name = f.readline().strip()
        line2_name = f.readline().strip()
        line3_name = f.readline().strip()
        name = []
        y1 = []
        y2 = []
        y3 = []
        for line in f:
            line = line.strip().split('\t')
            print(line)
            name.append(line[0])
            y1.append(float(line[1]))
            y2.append(float(line[2]))
            y3.append(float(line[3]))
        x = numpy.arange(len(y1))
        y1 = numpy.array(y1)
        y2 = numpy.array(y2)
        y3 = numpy.array(y3)
        # plt.stackplot(x, y1, y2, y3)

        p1 = plt.fill_between(x, 0, y1)
        p2 = plt.plot(x, y1, y2)
        p3 = plt.plot(x, y2, y3)

        plt.xlabel(xlabel, fontsize=fontsize)
        plt.ylabel(ylabel, fontsize=fontsize)

        plt.legend(loc='center right', fontsize=fontsize)
        plt.tick_params(axis='x', labelsize=fontsize)
        plt.tick_params(axis='y', labelsize=fontsize)
        plt.legend((p1[0], p2[0], p3[0]), (line1_name, line2_name, line3_name))
        xlabels = plt.xticks(x, name, rotation=30, horizontalalignment='right')
        # for label in xlabels:
        #     label.set_ro
        plt.tight_layout(pad=0.1)
        plt.savefig('%s.png' % (data_file))
        plt.show()


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Please input data file as a parameter')
        print('Like:')
        print('python plot.py data/toy_data.txt')
        exit(0)
    data_file = sys.argv[1]
    #stack_bar_plot(data_file)
    bar_plot(data_file)
