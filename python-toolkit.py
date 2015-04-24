#!/usr/bin/env python
import subprocess
import os
def check():
    count=0
    datafile = file('mac.txt')
    for line in datafile:        
        if inpu in line:            
            print li[count]
            found = True
            break
        count=count+1
    return found


print("Enter 1 for Linux Info")
print("Enter 2 for Networking capturing")
print("Enter 3 for Network scanning")
print("Enter 4 for Linux Security\n")
fil=raw_input('Enter the number :')
if fil=='1':
        print("Enter 1 to know linux Hostname")
        print("Enter 2 to know current user's username ")
        print("Enter 3 to see who is currently logged in ")
        print("Enter 4 to see who is currently logged in and what they are doing")
        print("Enter 5 to see list of recent system use")
        print("Enter 6 to find when user logged in")
        print("Enter 7 to list the process in current shell")
        print("Enter 8 to list all the processes of user")
        print("Enter 9 to list processes of PID")
        print("Enter 10 to know command history")
        print("Enter 11 to kill any process")
        print("Enter 12 to Identifies group names and group IDs")
        print("Enter 13 to list shadow passwords for groups")
        print("Enter 14 to list TCP/IP and UDP services and their port assignments")
        print("Enter 15 to list the partitions")
        print("Enter 16 to list the mounted flie system and available space")
        print("Enter 17 to display access log of Apache2")
                
        fil2=raw_input('Enter the number :') 
        if fil2=='1':
            subprocess.call(["hostname"])
        if fil2=='2':
            subprocess.call(["whoami"])
        if fil2=='3':
            subprocess.call(["who"])
        if fil2=='4':
            subprocess.call(["w"])
        if fil2=='5':
            subprocess.call(["last"])
        if fil2=='6':
            u=raw_input("Enter the username :")
            subprocess.call(["last",u])
        if fil2=='7':
            subprocess.call(["ps"])
        if fil2=='8':
            u=raw_input("Enter the username :")
            subprocess.call(["ps","-u",u])
        if fil2=='9':
            u=raw_input("Enter the PID :")
            subprocess.call(["ps","-p",u])
        if fil2=='10':
            subprocess.call(["history"])          
        if fil2=='11':
            f=raw_input("Enter the username :")
            subprocess.call(["ps","-u",f])
            k=raw_input("Enter the PID to kill ")
            subprocess.call(["kill",k])
        if fil2=='12':
            subprocess.call(["sudo","cat","/etc/group"])
        if fil2=='13':
            subprocess.call(["sudo","cat","/etc/gshadow"])
        if fil2=='14':
            subprocess.call(["sudo","cat","/etc/services"])
        if fil2=='15':
            subprocess.call(["sudo","/sbin/fdisk","-l"])
        if fil2=='16':
            subprocess.call(["sudo","df","-h"])
        if fil2=='17':
            subprocess.call(["cat","/var/log/apache2/access.log"])    
           

if fil=='2':
    print("Enter 1 for Display Available Interfaces")
    print("Enter 2 for Capture Packets from Specific Interface")
    print("Enter 3 for Capture Only N Number of Packets")
    print("Enter 4 for Print Captured Packets in ASCII")
    print("Enter 5 for Display Captured Packets in HEX and ASCII")
    print("Enter 6 for Capture Packet from Specific Port")
    print("Enter 7 for Capture Packets from source IP")
    print("Enter 8 for Capture Packets from destination IP")
    print("Enter 9 for Capture IP address Packets")
    print("Enter 10 for Capture only TCP Packets")
    print("Enter 11 for Read Captured Packets File")
    print("Enter 12 for Receive only the packets of a specific protocol type")
    print("Enter 13 for Check vendor of MAC address ")
    print("Enter 14 for Finding out the MAC addresses from the PCAP file ")
        
    fil2=raw_input('Enter the number :')      
    if fil2=='1':
        subprocess.call(["tcpdump","-D"])
    if fil2=='2':
        t=raw_input('Enter the interface :')
        subprocess.call(["tcpdump","-i",t])
    if fil2=='3':
        t=raw_input('Enter the N packets to capture :')
        c=raw_input('Enter the interface :')
        subprocess.call(["tcpdump","-c",t,"-i",c])
    if fil2=='4':
        t=raw_input('Enter the interface :')
        subprocess.call(["tcpdump","-A","-i",t])
    if fil2=='5':
        t=raw_input('Enter the interface :')
        subprocess.call(["tcpdump","-XX","-i",t])
    if fil2=='6':
        t=raw_input('Enter the interface :')
        c=raw_input('Enter the port :')
        subprocess.call(["tcpdump","-i",t,"port",c])
    if fil2=='7':
        t=raw_input('Enter the interface :')
        c=raw_input('Enter the source IP :')
        subprocess.call(["tcpdump","-i",t,"src",c])
    if fil2=='8':
        t=raw_input('Enter the interface :')
        c=raw_input('Enter the source IP :')            
        subprocess.call(["tcpdump","-i",t,"dst",c])
    if fil2=='9':
        t=raw_input('Enter the interface :')
        subprocess.call(["tcpdump","-n","-i",t])
    if fil2=='10':
        t=raw_input('Enter the interface :')
        subprocess.call(["tcpdump","-i",t,"tcp"])
    if fil2=='11':
        t=raw_input('Enter the file name :')
        subprocess.call(["tcpdump","-r",t])
    if fil2=='12':
        t=raw_input('Enter the interface :')
        c=raw_input('Enter the protocol :') 
        subprocess.call(["tcpdump","-i",t,c])
    if fil2=='13':
        inpu=raw_input('Enter the Mac address :')
        li=list() 
        f=open('mac.txt')
        for line in f:
            li.append(line)
            check()                
    if fil2=='14':
        t=raw_input('Enter the PCAP file name :')
        o=subprocess.check_output(["tcpdump","-XX","-r",t])
        io=list()
        ss='0x0000:  '
        tem=o
        cou=0
        u=(len(o)/5000)
        for a in range(u):
            if tem.find(ss):
                y=tem.find(ss)
                print tem[y+9:y+23]
                print tem[y+24:y+39]            
                tem=tem[y+39:]
                io.append(tem[y+9:y+39])
            cou=cou+1
             
if fil=='3':    
    print("\nEnter 1 for TCP SYN Scan")
    print("Enter 2 for TCP connect() Scan")
    print("Enter 3 for FIN Stealth Scan")
    print("Enter 4 for Xmas Tree Stealth Scan")
    print("Enter 5 for Null Stealth Scan")
    print("Enter 6 for Ping Scan")
    print("Enter 7 for Version Detection ")
    print("Enter 8 for UDP Scan ")
    print("Enter 9 for IP Protocol Scan")
    print("Enter 10 for ACK Scan ")
    print("Enter 11 for Window Scan ")
    print("Enter 12 for RPC Scan")
    print("Enter 13 for List Scan")
    print("Enter 14 for Idlescan")
    print("Enter 15 for FTP Bounce Attack")
    print("Enter 16 for OS Fingerprinting")
    print("Enter 17 for Scan all ports Dont Exclude Any Ports")
    print("Enter 18 for Scan specific Port range or Port")
    print("Enter 19 for Perform a script scan\n")
            
    fil2=raw_input('\nEnter -')
    if fil2=='1':
        IP=raw_input('\nEnter the IP :')
        subprocess.call(["sudo","nmap","-sS",IP])        
    if fil2=='2':
        IP=raw_input('\nEnter the IP :')
        subprocess.call(["sudo","nmap","-sT",IP])      
    if fil2=='3':
        IP=raw_input('\nEnter the IP :')
        subprocess.call(["sudo","nmap","-sF",IP])           
    if fil2=='4':
        IP=raw_input('\nEnter the IP :')
        subprocess.call(["sudo","nmap","-sX",IP])
    if fil2=='5':
        IP=raw_input('\nEnter the IP :')
        subprocess.call(["sudo","nmap","-sN",IP])        
    if fil2=='6':
        IP=raw_input('\nEnter the IP :')
        subprocess.call(["sudo","nmap","-sP",IP])            
    if fil2=='7':
        IP=raw_input('\nEnter the IP :')
        subprocess.call(["sudo","nmap","-sV",IP])            
    if fil2=='8':
        IP=raw_input('\nEnter the IP :')
        subprocess.call(["sudo","nmap","-sU",IP])        
    if fil2=='9':
        IP=raw_input('\nEnter the IP :')
        subprocess.call(["sudo","nmap","-sO",IP])            
    if fil2=='10':
        IP=raw_input('\nEnter the IP :')
        subprocess.call(["sudo","nmap","-sA",IP])            
    if fil2=='11':
        IP=raw_input('\nEnter the IP :')
        subprocess.call(["sudo","nmap","-sW",IP])            
    if fil2=='12':
        IP=raw_input('\nEnter the IP :')
        subprocess.call(["sudo","nmap","-sR",IP])            
    if fil2=='13':
        IP=raw_input('\nEnter the IP :')
        subprocess.call(["sudo","nmap","-sL",IP])         
    if fil2=='14':
        IP=raw_input('\nEnter the IP :')
        subprocess.call(["sudo","nmap","-sI",IP])          
    if fil2=='15':
        IP=raw_input('\nEnter the IP :')
        subprocess.call(["sudo","nmap","-b",IP])
    if fil2=='16':
        IP=raw_input('Enter IP :')
        subprocess.call(["nmap","-sO",IP])                             
    if fil2=='17':
        IP=raw_input('\nEnter the IP :')
        subprocess.call(["sudo","nmap","--allports",IP])
    if fil2=='18':
        ran=raw_input('\n Enter the range in x-y form or Port :')
        IP=raw_input('\nEnter the IP :')
        subprocess.call(["sudo","nmap","-p",ran,IP])            
    if fil2=='19':
        sc=raw_input('\n Enter the Name of script :')
        IP=raw_input('\nEnter the IP :')
        subprocess.call(["sudo","nmap","--script=",sc,IP])
               
            
if fil=='4':
    print("Enter 1 to check Protection of IP Spoofing")
    print("Enter 2 for changing or details of IPTABLES")
    print("Enter 3 for changing or details of Linux ufw Firewall")
        
    fil2=raw_input('Enter the number :') 
    if fil2=='1':        
        p=subprocess.check_output(["cat","/proc/sys/net/ipv4/conf/all/rp_filter"])
        if p.find('0'):
            print("System is protected from IP Spoofing")
        if p.find('1'):
            print("System is not protected from IP Spoofing")                
    if fil2=='2':
        print("Enter 1 to list the rules of IPTABLES")
        print("Enter 2 for adding INPUT rules of IPTABLES")
        print("Enter 3 for adding OUTPUT rules of IPTABLES")
        print("Enter 4 for adding FORWARD rules of IPTABLES")
        print("Enter 5 for adding PREROUTING rules of IPTABLES")
        print("Enter 6 for adding POSTROUTING rules of IPTABLES")
        print("Enter 7 to adding rules for specifies a protocol, such as TCP, UDP, ICMP, or ALL")
        fil3=raw_input('Enter the number :')
        if fil3=='1':
            subprocess.call(["sudo","iptables","-L","-n"])
        if fil3=='2':
            print("Enter 1 to change ACCEPT rules")
            print("Enter 2 to change DROP rules")
            print("Enter 3 to change REJECT rules")
            print("Enter 4 to change QUEUE rules")
            print("Enter 5 to change RETURN rules")
            ff=raw_input("Enter the number :")
            if ff=='1':
                IP=raw_input("Enter the source address :")
                subprocess.call(["sudo","iptables","-A","INPUT","-j","ACCEPT","-s",IP])
            if ff=='2':
                IP=raw_input("Enter the source address :")
                subprocess.call(["sudo","iptables","-A","INPUT","-j","DROP","-s",IP])    
            if ff=='3':
                IP=raw_input("Enter the source address :")
                subprocess.call(["sudo","iptables","-A","INPUT","-j","REJECT","-s",IP])
            if ff=='4':
                IP=raw_input("Enter the source address :")
                subprocess.call(["sudo","iptables","-A","INPUT","-j","QUEUE","-s",IP])
            if ff=='5':
                IP=raw_input("Enter the source address :")
                subprocess.call(["sudo","iptables","-A","INPUT","-j","RETERN","-s",IP])  

        if fil3=='3':
            print("Enter 1 to change ACCEPT rules")
            print("Enter 2 to change DROP rules")
            print("Enter 3 to change REJECT rules")
            print("Enter 4 to change QUEUE rules")
            print("Enter 5 to change RETURN rules")
            ff=raw_input("Enter the number :")
            if ff=='1':
                IP=raw_input("Enter the source address :")
                subprocess.call(["sudo","iptables","-A","OUTPUT","-j","ACCEPT","-s",IP])
            if ff=='2':
                IP=raw_input("Enter the source address :")
                subprocess.call(["sudo","iptables","-A","OUTPUT","-j","DROP","-s",IP])
            if ff=='3':
                IP=raw_input("Enter the source address :")
                subprocess.call(["sudo","iptables","-A","OUTPUT","-j","REJECT","-s",IP])
            if ff=='4':
                IP=raw_input("Enter the source address :")
                subprocess.call(["sudo","iptables","-A","OUTPUT","-j","QUEUE","-s",IP])
            if ff=='5':
                IP=raw_input("Enter the source address :")
                subprocess.call(["sudo","iptables","-A","OUTPUT","-j","RETERN","-s",IP])
        if fil3=='4':
            print("Enter 1 to change ACCEPT rules")
            print("Enter 2 to change DROP rules")
            print("Enter 3 to change REJECT rules")
            print("Enter 4 to change QUEUE rules")
            print("Enter 5 to change RETURN rules")
            ff=raw_input("Enter the number :")
            if ff=='1':
                IP=raw_input("Enter the source address :")
                subprocess.call(["sudo","iptables","-A","FORWARD","-j","ACCEPT","-s",IP])
            if ff=='2':
                IP=raw_input("Enter the source address :")
                subprocess.call(["sudo","iptables","-A","FORWARD","-j","DROP","-s",IP])
            if ff=='3':
                IP=raw_input("Enter the source address :")
                subprocess.call(["sudo","iptables","-A","FORWARD","-j","REJECT","-s",IP])
            if ff=='4':
                IP=raw_input("Enter the source address :")
                subprocess.call(["sudo","iptables","-A","FORWARD","-j","QUEUE","-s",IP])
            if ff=='5':
                IP=raw_input("Enter the source address :")
                subprocess.call(["sudo","iptables","-A","FORWARD","-j","RETERN","-s",IP])
        if fil3=='5':
            print("Enter 1 to change ACCEPT rules")
            print("Enter 2 to change DROP rules")
            print("Enter 3 to change REJECT rules")
            print("Enter 4 to change QUEUE rules")
            print("Enter 5 to change RETURN rules")
            ff=raw_input("Enter the number :")
            if ff=='1':
                IP=raw_input("Enter the source address :")
                subprocess.call(["sudo","iptables","-A","PREROUTING","-j","ACCEPT","-s",IP])
            if ff=='2':
                IP=raw_input("Enter the source address :")
                subprocess.call(["sudo","iptables","-A","PREROUTING","-j","DROP","-s",IP])
            if ff=='3':
                IP=raw_input("Enter the source address :")
                subprocess.call(["sudo","iptables","-A","PREROUTING","-j","REJECT","-s",IP])
            if ff=='4':
                IP=raw_input("Enter the source address :")
                subprocess.call(["sudo","iptables","-A","PREROUTING","-j","QUEUE","-s",IP])
            if ff=='5':
                IP=raw_input("Enter the source address :")
                subprocess.call(["sudo","iptables","-A","PREROUTING","-j","RETERN","-s",IP])
        if fil3=='6':
            print("Enter 1 to change ACCEPT rules")
            print("Enter 2 to change DROP rules")
            print("Enter 3 to change REJECT rules")
            print("Enter 4 to change QUEUE rules")
            print("Enter 5 to change RETURN rules")
            ff=raw_input("Enter the number :")
            if ff=='1':
                IP=raw_input("Enter the source address :")
                subprocess.call(["sudo","iptables","-A","POSTROUTING","-j","ACCEPT","-s",IP])
            if ff=='2':
                IP=raw_input("Enter the source address :")
                subprocess.call(["sudo","iptables","-A","POSTROUTING","-j","DROP","-s",IP])
            if ff=='3':
                IP=raw_input("Enter the source address :")
                subprocess.call(["sudo","iptables","-A","POSTROUTING","-j","REJECT","-s",IP])
            if ff=='4':
                IP=raw_input("Enter the source address :")
                subprocess.call(["sudo","iptables","-A","POSTROUTING","-j","QUEUE","-s",IP])
            if ff=='5':
                IP=raw_input("Enter the source address :")
                subprocess.call(["sudo","iptables","-A","POSTROUTING","-j","RETERN","-s",IP])
        if fil3=='7':
            print("Enter 1 for adding INPUT rules of IPTABLES")
            print("Enter 2 for adding OUTPUT rules of IPTABLES")
            print("Enter 3 for adding FORWARD rules of IPTABLES")
            print("Enter 4 for adding PREROUTING rules of IPTABLES")
            print("Enter 5 for adding POSTROUTING rules of IPTABLES")
            fil4=raw_input("Enter the number :")
            if fil4=='1':
                print("Enter 1 to change ACCEPT rules")
                print("Enter 2 to change DROP rules")
                print("Enter 3 to change REJECT rules")
                print("Enter 4 to change QUEUE rules")
                print("Enter 5 to change RETURN rules")
                ff=raw_input("Enter the number :")
                IP=raw_input("Enter the source address :")
                pro=raw_input("Enter the protocol :")
                
                if ff=='1':                                        
                    subprocess.call(["sudo","iptables","-p",pro,"-A","INPUT","-j","ACCEPT","-s",IP])
                if ff=='2':                    
                    subprocess.call(["sudo","iptables","-p",pro,"-A","INPUT","-j","DROP","-s",IP])    
                if ff=='3':                    
                    subprocess.call(["sudo","iptables","-p",pro,"-A","INPUT","-j","REJECT","-s",IP])
                if ff=='4':                    
                    subprocess.call(["sudo","iptables","-p",pro,"-A","INPUT","-j","QUEUE","-s",IP])
                if ff=='5':                    
                    subprocess.call(["sudo","iptables","-p",pro,"-A","INPUT","-j","RETERN","-s",IP])  

            if fil4=='2':
                print("Enter 1 to change ACCEPT rules")
                print("Enter 2 to change DROP rules")
                print("Enter 3 to change REJECT rules")
                print("Enter 4 to change QUEUE rules")
                print("Enter 5 to change RETURN rules")
                ff=raw_input("Enter the number :")
                if ff=='1':
                    IP=raw_input("Enter the source address :")
                    subprocess.call(["sudo","iptables","-p",pro,"-A","OUTPUT","-j","ACCEPT","-s",IP])
                if ff=='2':
                    IP=raw_input("Enter the source address :")
                    subprocess.call(["sudo","iptables","-p",pro,"-A","OUTPUT","-j","DROP","-s",IP])
                if ff=='3':
                    IP=raw_input("Enter the source address :")
                    subprocess.call(["sudo","iptables","-p",pro,"-A","OUTPUT","-j","REJECT","-s",IP])
                if ff=='4':
                    IP=raw_input("Enter the source address :")
                    subprocess.call(["sudo","iptables","-p",pro,"-A","OUTPUT","-j","QUEUE","-s",IP])
                if ff=='5':
                    IP=raw_input("Enter the source address :")
                    subprocess.call(["sudo","iptables","-p",pro,"-A","OUTPUT","-j","RETERN","-s",IP])
            if fil4=='3':
                print("Enter 1 to change ACCEPT rules")
                print("Enter 2 to change DROP rules")
                print("Enter 3 to change REJECT rules")
                print("Enter 4 to change QUEUE rules")
                print("Enter 5 to change RETURN rules")
                ff=raw_input("Enter the number :")
                if ff=='1':
                    IP=raw_input("Enter the source address :")
                    subprocess.call(["sudo","iptables","-p",pro,"-A","FORWARD","-j","ACCEPT","-s",IP])
                if ff=='2':
                    IP=raw_input("Enter the source address :")
                    subprocess.call(["sudo","iptables","-p",pro,"-A","FORWARD","-j","DROP","-s",IP])
                if ff=='3':
                    IP=raw_input("Enter the source address :")
                    subprocess.call(["sudo","iptables","-A","FORWARD","-j","REJECT","-s",IP])
                if ff=='4':
                    IP=raw_input("Enter the source address :")
                    subprocess.call(["sudo","iptables","-p",pro,"-A","FORWARD","-j","QUEUE","-s",IP])
                if ff=='5':
                    IP=raw_input("Enter the source address :")
                    subprocess.call(["sudo","iptables","-p",pro,"-A","FORWARD","-j","RETERN","-s",IP])
            if fil4=='4':
                print("Enter 1 to change ACCEPT rules")
                print("Enter 2 to change DROP rules")
                print("Enter 3 to change REJECT rules")
                print("Enter 4 to change QUEUE rules")
                print("Enter 5 to change RETURN rules")
                ff=raw_input("Enter the number :")
                if ff=='1':
                    IP=raw_input("Enter the source address :")
                    subprocess.call(["sudo","iptables","-p",pro,"-A","PREROUTING","-j","ACCEPT","-s",IP])
                if ff=='2':
                    IP=raw_input("Enter the source address :")
                    subprocess.call(["sudo","iptables","-p",pro,"-A","PREROUTING","-j","DROP","-s",IP])
                if ff=='3':
                    IP=raw_input("Enter the source address :")
                    subprocess.call(["sudo","iptables","-p",pro,"-A","PREROUTING","-j","REJECT","-s",IP])
                if ff=='4':
                    IP=raw_input("Enter the source address :")
                    subprocess.call(["sudo","iptables","-p",pro,"-A","PREROUTING","-j","QUEUE","-s",IP])
                if ff=='5':
                    IP=raw_input("Enter the source address :")
                    subprocess.call(["sudo","iptables","-p",pro,"-A","PREROUTING","-j","RETERN","-s",IP])
            if fil4=='5':
                print("Enter 1 to change ACCEPT rules")
                print("Enter 2 to change DROP rules")
                print("Enter 3 to change REJECT rules")
                print("Enter 4 to change QUEUE rules")
                print("Enter 5 to change RETURN rules")
                ff=raw_input("Enter the number :")
                if ff=='1':
                    IP=raw_input("Enter the source address :")
                    subprocess.call(["sudo","iptables","-p",pro,"-A","POSTROUTING","-j","ACCEPT","-s",IP])
                if ff=='2':
                    IP=raw_input("Enter the source address :")
                    subprocess.call(["sudo","iptables","-p",pro,"-A","POSTROUTING","-j","DROP","-s",IP])
                if ff=='3':
                    IP=raw_input("Enter the source address :")
                    subprocess.call(["sudo","iptables","-p",pro,"-A","POSTROUTING","-j","REJECT","-s",IP])
                if ff=='4':
                    IP=raw_input("Enter the source address :")
                    subprocess.call(["sudo","iptables","-p",pro,"-A","POSTROUTING","-j","QUEUE","-s",IP])
                if ff=='5':
                    IP=raw_input("Enter the source address :")
                    subprocess.call(["sudo","iptables","-p",pro,"-A","POSTROUTING","-j","RETERN","-s",IP])
    if fil2=='3':
        print("Enter 1 to check status of firewall")
        print("Enter 2 for turn on or turn off the firewall ")
        print("Enter 3 for create or delete rule")
        print("Enter 4 for turn on or turn off firewall logging")
        
        fil3=raw_input("Enter the number :")
        if fil3=='1':
            subprocess.call(["sudo","ufw","status","verbose"])
        if fil3=='2':
            print("Enter 1 for turn on the firewall")
            print("Enter 2 for turn off the firewall")
            fil4=raw_input("Enter the number :")
            if fil4=='1':
                subprocess.call(["sudo","ufw","enable"])
            if fil4=='2':
                subprocess.call(["sudo","ufw","disable"])
        if fil3=='3':
            print("Enter 1 for create firewall rules")
            print("Enter 2 for delete firewall rules")
            fil4=raw_input("Enter the number :")
            if fil4=='1':
                print("Enter 1 to set firewall default to allow all incomming connections")
                print("Enter 2 to set firewall default to deny all incomming connections")
                print("Enter 3 to set firewall default to allow all outgoing connections")
                print("Enter 4 to set firewall default to deny all outgoing connections")
                print("Enter 5 to create rule for allow incomming connection for port")
                print("Enter 6 to allow incomming connection for port with protocol")
                print("Enter 7 to allow deny connection for port")
                print("Enter 8 to allow deny connection for port with protocol")
                print("Enter 9 for allow or deny IP")
                print("Enter 10 to allow or deny  IP with port number")
                print("Enter 11 to allow or deny  IP with port number using specific protocol")
                fil5=raw_input("Enter the number :")
                if fil5=='1':
                    subprocess.call(["sudo","ufw","default","allow","incomming"])
                if fil5=='2':
                    subprocess.call(["sudo","ufw","default","deny","incomming"])
                if fil5=='3':
                    subprocess.call(["sudo","ufw","default","allow","incomming"])
                if fil5=='4':
                    subprocess.call(["sudo","ufw","default","deny","incomming"])
                if fil5=='5':
                    por=raw_input("Enter the port number :")
                    subprocess.call(["sudo","ufw","allow"])        
                if fil5=='6':
                    print("Define port with protocol in form of port/protocol")
                    por=raw_input("Enter :")
                    if ff=='1':
                        subprocess.call(["sudo","ufw","allow","incomming",por])
                    if ff=='2':
                        subprocess.call(["sudo","ufw","deny","incomming",por])
                if fil5=='7':                    
                    por=raw_input("Enter the port number :")
                    if ff=='1':
                        subprocess.call(["sudo","ufw","allow",por])
                    if ff=='2':
                        subprocess.call(["sudo","ufw","deny",por])                           
                if fil5=='8':
                    print("Define port with protocol in form of port/protocol")
                    por=raw_input("Enter :")
                    if ff=='1':
                        subprocess.call(["sudo","ufw","allow",por])
                    if ff=='2':
                        subprocess.call(["sudo","ufw","deny",por])
                if fil5=='9':
                    print("Enter 1 for allow IP :")
                    print("Enter 2 for deny IP :")
                    fil6=raw_input("Enter the Number :")
                    
                    if fil6=='1':
                       f=raw_input("Enter the IP address :")                       
                       subprocess.call(["sudo","ufw","allow","from",f])
                    if fil6=='2':
                        f=raw_input("Enter the IP address :")
                        print("Enter the IP address :")
                        te='deny'
                        subprocess.call(["sudo","ufw","deny","from",f])
                if fil5=='10':
                    print("Enter 1 for allow IP :")
                    print("Enter 2 for deny IP :")
                    fil6=raw_input("Enter the Number :")
                    
                    if fil6=='1':
                       f=raw_input("Enter the IP address :")
                       ff=raw_input("Enter the IP address :")
                       te='allow'
                       subprocess.call(["sudo","ufw","allow","from",f,"to any port",ff])
                    if fil6=='2':
                        f=raw_input("Enter the IP address :")
                        f=raw_input("Enter the IP address :")
                        print("Enter the IP address :")
                        te='deny'
                        subprocess.call(["sudo","ufw","deny","from",f,ff])
                if fil5=='11':
                    print("Enter 1 for allow IP :")
                    print("Enter 2 for deny IP :")
                    fil6=raw_input("Enter the Number :")
                    
                    if fil6=='1':
                       f=raw_input("Enter the IP address :")
                       ff=raw_input("Enter the IP address :")
                       fff=raw_input("Enter the protocol :")
                       te='allow'
                       subprocess.call(["sudo","ufw","allow","from",f,"to any port",ff,"proto",fff])
                    if fil6=='2':
                        f=raw_input("Enter the IP address :")
                        f=raw_input("Enter the IP address :")
                        print("Enter the IP address :")
                        te='deny'
                        subprocess.call(["sudo","ufw","deny","from",f,"to any port",ff,"proto",fff])
            if fil4=='2':
                print("Enter 3 to delete firewall default to allow all incomming connections")
                print("Enter 4 to delete firewall default to deny all incomming connections")
                print("Enter 5 to delete firewall default to allow all outgoing connections")
                print("Enter 6 to delete firewall default to deny all outgoing connections")
                print("Enter 7 to delete rule for allow incomming connection for port")
                print("Enter 8 to delete rule for allow incomming connection for port with protocol")
                print("Enter 9 to delete rule for allow deny connection for port")
                print("Enter 10 to delete rule to allow deny connection for port with protocol")
                print("Enter 11 for delete rule to allow or deny IP")
                print("Enter 12 for delete rule to allow or deny  IP with port number")
                print("Enter 13 to allow or deny  IP with port number using specific protocol")
                fil5=raw_input("Enter the number :")
                de="delete"
                
                if fil5=='1':
                    subprocess.call(["sudo",de,"ufw","default","allow","incomming"])
                if fil5=='4':
                    subprocess.call(["sudo",de,"ufw","default","deny","incomming"])
                if fil5=='5':
                    subprocess.call(["sudo",de,"ufw","default","allow","incomming"])
                if fil5=='6':
                    subprocess.call(["sudo",de,"ufw","default","deny","incomming"])
                if fil5=='7':
                    por=raw_input("Enter the port number :")
                    subprocess.call(["sudo",de,"ufw","allow"])        
                if fil5=='8':
                    print("Define port with protocol in form of port/protocol")
                    por=raw_input("Enter :")            
                    subprocess.call(["sudo",de,"ufw","allow",por])
                if fil5=='9':
                    por=raw_input("Enter the port number :")
                    subprocess.call(["sudo",de,"ufw","deny"])        
                if fil5=='10':
                    print("Define port with protocol in form of port/protocol")
                    por=raw_input("Enter :")            
                    subprocess.call(["sudo",de,"ufw","deny",por])
                if fil5=='11':
                    print("Enter 1 for allow IP :")
                    print("Enter 2 for deny IP :")
                    fil6=raw_input("Enter the Number :")
                    
                    if fil6=='1':
                       f=raw_input("Enter the IP address :")
                       te='allow'
                       subprocess.call(["sudo",de,"ufw","allow","from",f])
                    if fil6=='2':
                        f=raw_input("Enter the IP address :")
                        print("Enter the IP address :")
                        te='deny'
                        subprocess.call(["sudo",de,"ufw","deny","from",f])
                if fil5=='12':
                    print("Enter 1 for allow IP :")
                    print("Enter 2 for deny IP :")
                    fil6=raw_input("Enter the Number :")
                    
                    if fil6=='1':
                       f=raw_input("Enter the IP address :")
                       ff=raw_input("Enter the IP address :")
                       te='allow'
                       subprocess.call(["sudo",de,"ufw","allow","from",f,"to any port",ff])
                    if fil6=='2':
                        f=raw_input("Enter the IP address :")
                        f=raw_input("Enter the IP address :")
                        print("Enter the IP address :")
                        te='deny'
                        subprocess.call(["sudo",de,"ufw","deny","from",f,ff])
                if fil5=='13':
                    print("Enter 1 for allow IP :")
                    print("Enter 2 for deny IP :")
                    fil6=raw_input("Enter the Number :")
                    
                    if fil6=='1':
                       f=raw_input("Enter the IP address :")
                       ff=raw_input("Enter the IP address :")
                       fff=raw_input("Enter the protocol :")
                       te='allow'
                       subprocess.call(["sudo",de,"ufw","allow","from",f,"to any port",ff,"proto",fff])
                    if fil6=='2':
                        f=raw_input("Enter the IP address :")
                        f=raw_input("Enter the IP address :")
                        print("Enter the IP address :")
                        te='deny'
                        subprocess.call(["sudo",de,"ufw","deny","from",f,"to any port",ff,"proto",fff])
        if fil3=='4':
            print("Enter 1 for turn on the turn on firewall logging ")
            print("Enter 2 for turn on the turn off firewall logging ")
            fil4=raw_input("Enter the number :")
            if fil4=='1':
                subprocess.call(["sudo","ufw","logging","on"])
            if fil4=='2':
                subprocess.call(["sudo","ufw","logging","off"])
        
