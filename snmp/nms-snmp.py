#!/usr/bin/env python
import netsnmp

snmp_oids={
    "all": ".1",
    "system" : ".1.3.6.1.2.1.1",
    "uptime" : ".1.3.6.1.2.1.1.3",
    "interfaces" : ".1.3.6.1.2.1.2",
    "load": ".1.3.6.1.4.1.2021.10.1.3",
    "load1": ".1.3.6.1.4.1.2021.10.1.3.1",
    "load5": ".1.3.6.1.4.1.2021.10.1.3.2",
    "load15": ".1.3.6.1.4.1.2021.10.1.3.3",
    "test" : "SNMPv2-MIB::sysUpTime.0"
}

apc_snmp_oids={

}
"""
"cpu_user" : ".1.3.6.1.4.1.2021.11.9.0",
"cpu_system" : ".1.3.6.1.4.1.2021.11.10.0",
"cpu_idle" : ".1.3.6.1.4.1.2021.11.11.0"
raw user cpu time: .1.3.6.1.4.1.2021.11.50.0
raw system cpu time: .1.3.6.1.4.1.2021.11.52.0
raw idle cpu time: .1.3.6.1.4.1.2021.11.53.0
raw nice cpu time: .1.3.6.1.4.1.2021.11.51.0
Memory Statistics
Total Swap Size: .1.3.6.1.4.1.2021.4.3.0
Available Swap Space: .1.3.6.1.4.1.2021.4.4.0
Total RAM in machine: .1.3.6.1.4.1.2021.4.5.0
Total RAM used: .1.3.6.1.4.1.2021.4.6.0
Total RAM Free: .1.3.6.1.4.1.2021.4.11.0
Total RAM Shared: .1.3.6.1.4.1.2021.4.13.0
Total RAM Buffered: .1.3.6.1.4.1.2021.4.14.0
Total Cached Memory: .1.3.6.1.4.1.2021.4.15.0
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
    a = nms_snmp(oid=snmp_oids["all"],DestHost="127.0.0.1")
    data = a.query()
    print data
