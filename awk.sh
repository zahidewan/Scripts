#zahid Dewan
#Script to Search through network logs using awk and find IP, timestamps, UserID and MAC Address 
#change/modify UID strings depending on your UID format 

egrep $1 | awk '{match($0,/[a-zA-Z][a-zA-Z][0- 9][0-9][0-9][0-9][a-zZ-Z][a-zA-Z]/) ; UID = substr($0,RSTART,RLENGTH); match($1,/[0-9][0-9]\:[0-9][0-9]\:[0-9][0-9]/) ; timestamp = substr($1,RSTART,RLENGTH) ; match($0,/[0-9a-f][0-9a-f]\-[0-9a-f][0-9a-f]\- [0-9a-f][0-9a-f]\-[0-9a-f][0-9a-f]\-[0-9a-f][0-9a-f]\-[0-9a-f][0-9a-f]/); macaddr = substr($0,RSTART,RLENGTH); print "Time Stamp: "timestamp " | Star ID: " starID " | Mac-Address: " macaddr}'
