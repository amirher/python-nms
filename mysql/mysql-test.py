#!/usr/bin/env python
import MySQLdb


conn = MySQLdb.connect (host = "localhost",
                        user = "root",
                        passwd = "temporal",
                        db = "dconnect")
cursor = conn.cursor ()
cursor.execute("SELECT host, ip from hosts");
for host,ip in cursor.fetchall(): print ip
cursor.close()
conn.close()
