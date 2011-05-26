#!/usr/bin/env python
import netsnmp
import time

snmp_oids={
    "uptime" : ".1.3.6.1.2.1.1.3",
    "interfaces" : ".1.3.6.1.2.1.2.1",
    "load":   ".1.3.6.1.4.1.2021.10.1.3",
    "load1":  ".1.3.6.1.4.1.2021.10.1.3.1",
    "load5":  ".1.3.6.1.4.1.2021.10.1.3.2",
    "load15": ".1.3.6.1.4.1.2021.10.1.3.3",
    "sysdescr" : ".1.3.6.1.2.1.1.1",
    "sysid": ".1.3.6.1.2.1.1.2",
    "sysname": ".1.3.6.1.2.1.1.5",
    "ifDescr" : ".1.3.6.1.2.1.2.2.1.2",
    "ifPhyAddr" : ".1.3.6.1.2.1.2.2.1.6",
    "ifOperStatus" : ".1.3.6.1.2.1.2.2.1.8",
    "ifInOctets" : ".1.3.6.1.2.1.2.2.1.10",
    "ifOutOctets" : ".1.3.6.1.2.1.2.2.1.16",
    "diskErrorSpace" : ".1.3.6.1.4.1.2021.9.1.101",
    "CpuRawUser" : ".1.3.6.1.4.1.2021.11.50",
    "CpuRawNice" : ".1.3.6.1.4.1.2021.11.51",
    "CpuRawSystem": ".1.3.6.1.4.1.2021.11.52",
    "CpuRawIdle" : ".1.3.6.1.4.1.2021.11.53",
    "CpuRawWait" : ".1.3.6.1.4.1.2021.11.54",
    "CpuRawKernel" :".1.3.6.1.4.1.2021.11.55",
    "CpuRawInterrupt" : ".1.3.6.1.4.1.2021.11.56",
    "CpuUserDeprecated": ".1.3.6.1.4.1.2021.11.9",
    "CpuSystemDeprecated": ".1.3.6.1.4.1.2021.11.10",
    "CpuIdleDeprecated" : ".1.3.6.1.4.1.2021.11.11",
}

apc_snmp_oids={
    "AcutalVoltage" : ".1.3.6.1.4.1.318.1.1.1.2.2.8",
}

"""
    #"all": ".1",

Memory Statistics
Total Swap Size: .1.3.6.1.4.1.2021.4.3.0
Available Swap Space: .1.3.6.1.4.1.2021.4.4.0
Total RAM in machine: .1.3.6.1.4.1.2021.4.5.0
Total RAM used: .1.3.6.1.4.1.2021.4.6.0
Total RAM Free: .1.3.6.1.4.1.2021.4.11.0
Total RAM Shared: .1.3.6.1.4.1.2021.4.13.0
Total RAM Buffered: .1.3.6.1.4.1.2021.4.14.0
Total Cached Memory: .1.3.6.1.4.1.2021.4.15.0

Disks...
Iface ip...

"""

class nms_snmp(object):
    def __init__(self,
                oid="sysDescr.0",
                Version=2,
                DestHost="localhost",
                Community="public"):

        self.oid = oid
        self.Version = Version
        self.DestHost = DestHost
        self.Community = Community


    def query(self):
        """Creates SNMP query session"""
        try:
            result = netsnmp.snmpwalk(self.oid,
                                    Version = self.Version,
                                    DestHost = self.DestHost,
                                    Community = self.Community)
        except:
            import sys
            print sys.exc_info()
            result = None

        return result

if __name__ == "__main__":
    total_raw=[0,0]
    idle_raw=[0,0]
    system_raw=[0,0]
    user_raw=[0,0]
    for i in range (10):
        inc_raw = 0
        for k,v in snmp_oids.iteritems():
            a = nms_snmp(oid=snmp_oids[k],DestHost="193.146.156.54")
            data = a.query()
            if "Raw" in k:
                inc_raw += int(data[0])
                if "CpuRawIdle" in k:
                    inc = int(data[0]) - idle_raw[0]
                    idle_raw[0] = int(data[0])
                    idle_raw[1] = inc
                elif "CpuRawSystem" in k:
                    inc = int(data[0]) - system_raw[0]
                    system_raw[0] = int(data[0])
                    system_raw[1] = inc
                elif "CpuRawUser" in k:
                    inc = int(data[0]) - user_raw[0]
                    user_raw[0] = int(data[0])
                    user_raw[1] = inc
           # print ("%s: %s"% (k, data))
        inc = inc_raw - total_raw[0]
        total_raw[0] = inc_raw
        total_raw[1] = inc

        if inc == inc_raw:
            time.sleep(5)
            continue

        print "Raw:" , str(total_raw[0])
        print "Raw_inc:" , str(total_raw[1])

        print "User:", str(user_raw[0])
        print "User_inc:", str(user_raw[1])
        print "User %:",str(user_raw[1]*100/total_raw[1]) 

        print "System:", str(system_raw[0])
        print "System_inc:", str(system_raw[1])
        print "System %:",str(system_raw[1]*100/total_raw[1])

        print "Idle:", str(idle_raw[0])
        print "Idle_inc:", str(idle_raw[1])
        print "Idle %:",str(idle_raw[1]*100/total_raw[1])
             
        time.sleep(5)
