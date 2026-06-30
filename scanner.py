import socket 
import sys
from datetime import datetime
import mysql.connector as mysql

try:
    db_connection = mysql.connect(
        host="localhost",
        user="scanner_user",
        password= "your_passward",
        database= "network_security_db"
    )
    cursor = db_connection.cursor()
    print("[+] Successfully connected to the MySQL Database.")
except mysql.Error as err:
    print(f"[-] Database connection failed :{err} ")
    sys.exit(1)
TARGET_IP="127.0.0.1"
PORT_TO_SCAN=[ 21,22,80,135,443,3306,8080]

print(f"\n[*] Starting security scan on target:{TARGET_IP}")
print(f"[*]Scanning started at : {str(datetime.now())}\n")

for port in PORT_TO_SCAN:
    sock=socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    sock.settimeout(1.0)
    result=sock.connect_ex((TARGET_IP,port))

    if result==0:
        print(f"[!] Warning: Port {port} is OPEN on {TARGET_IP}!")
        try:

            insert_query="""
            INSERT INTO scan_logs(target_ip, port_number, port_status)
            VALUES (%s,%s,%s)
            """
            cursor.execute(insert_query,(TARGET_IP,port,"OPEN"))
            db_connection.commit()
            print(f"[->]Succesfully logged port{port} to MySQL.")
        except mysql.Error as err:
            print(f"    [-] Failed to write to log table: {err}")
    else:
        print(f"[-]Port {port} is closed.")
        sock.close()
cursor.close()
db_connection.close()
print("\n[*] Scan complete. Target database handles safely closed.")
        
