import psutil
import time
import sys
import datetime

if __name__=='__main__':
    assert len(sys.argv)>2
    fout=open('%s.monitor_info.data'%(sys.argv[1]),'w')
    try:
        p=psutil.Popen(sys.argv[2:])
        fout.write('#Name: %s\n'%p.name())
        fout.write('#Pid : %s\n'%p.pid)
        print(p.pid)
        fout.write('#User: %s\n'%p.username())
        while 1:
            status=p.status()
            if status=='zombie':
                break
            print(status)
            mem=p.memory_info()
            now=datetime.datetime.fromtimestamp(p.create_time()).strftime("%Y-%m-%d %H:%M:%S")
            fout.write('%s %s %d %d\n'%(now, status, mem.rss, mem.vms))
            time.sleep(1)
    except Exception as e:
        print(e)
        print('User terminate')
        p.terminate()

