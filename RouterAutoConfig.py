
#dewan
#Write a python script to configure 2 routers, use interface commands
#IT 462
#Summer S2

#import re from python library
import re

#define getVersion
def GetVersion():
    myResult = Session.ExecCommand("sh version")
    myVer = [n.strip(" ") for n in myResult.splitlines() if n.startswith("Cisco")]
    CisVer = [v.strip(" ") for v in myVer[0].split(",")]

    # Calculate IOS version numbers. This is more for demonstration, some scripts may need to check version numbers separately

    IOSVer = CisVer[2]
    IOSVerNum = IOSVerNum.split(" ")[1]
    IOSSUbVerNum = re.findall(r"[\w']+", IOSVerNum)
    myIOSMajorReleaseID = IOSSUbVerNum[0]
    myIOSMinorReleaseID = IOSSUbVerNum[1]
    myIOSMaintenNum = IOSSUbVerNum[2]
    myIOSTrainID = IOSSUbVerNum[3]
    # Calculate Router HW version
    HWVersionInfo = [v for v in myVer[1].strip(" ").split(" ")]
    HWPlatform = HWVersionInfo[0] + " " + HWVersionInfo[1]
    return "IOS Version:" + myIOSMajorReleaseID + "." + myIOSMinorReleaseID + "." + myIOSMaintenNum + "." + myIOSTrainID + ";HW:" + HWPlatform


def GetGW():
    myResult = Session.ExecCommand("sh run int vlan1")
    myIpAddress = ""
    SubnetMask = ""
    # Get VLAN1 interface details
    for thisLine in myResult.splitlines():
        if thisLine.strip(" ").startswith("ip address"):
            words = thisLine.strip(" ").split(" ")
            if len(words) > 3:
                myIpAddress = words[2]
                SubnetMask = words[3]
                break
#return ip address and subnet mask
    return ";Gateway IP:" + myIpAddress + "/" + SubnetMask

#define host name
def GetHostName():
    return "Hostname: " + Session.GetHostName("#")

