from zk import ZK, const
from import sys
nam=sys.argv[1]
thang=sys.argv[2]
ngay=sys.argv[3]
gio=sys.argv[4]
phut=sys.argv[5]
giay=sys.argv[6]

print (nam)
print (thang)
print (ngay)
print (gio)
print (phut)
print (giay)

conn = None
# create ZK instance
zk = ZK('192.168.1.201', port=4370, timeout=5, password=0, force_udp=False, ommit_ping=False)
try:
    # connect to device
    conn = zk.connect()
    # disable device, this method ensures no activity on the device while the process is run
    conn.disable_device()
    # another commands will be here!
    # Example: Get All Users
    # Test connection
    zktime = conn.get_time()
    print (zktime)
    firm = conn.get_firmware_version()
    print (firm)
    serial = conn.get_serialnumber()
    print (serial)
    
except Exception as e:
    print ("Process terminate : {}".format(e))
finally:
    if conn:
        conn.disconnect()
