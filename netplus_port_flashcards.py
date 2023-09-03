from random import randrange

print("Test your port to protocol knowledge!")
# Initalize the variubles
order=[];
wrong=[];
score=0;
count=0;
answer_key=[[22,"SSH"],[20,"FTP-DATA"],[21,"FTP-CONTROL"],[23,"TELNET"],[25,"SMTP"],[53,"DNS"],[67,"DHCP-SERVER"],[68,"DHCP-CLIENT"],[69,"TFTP"],[80,"HTTP"],[110,"POP3"],[123,"NTP"],[143,"IMAP"],[161,"SNMP"],[162,"SNMPTRAP"],[389,"LDAP"],[443,"HTTPS"],[445,"SMB"],[514,"SYSLOG"],[587,"SMTP/TLS"],[636,"LDAP/SSL"],[993,"IMAP/SSL"],[995,"POP3/SSL"],[1433,"SQL"],[1521,"SQLNET"],[3306,"MYSQL"],[3389,"RDP"],[5060,"SIP"],[5061,"SIP"]
]

# Grab the length of the answer key and set it to be the number of questons
question_number=len(answer_key)
# Set the question number to 10 instead of all answers in the answer key
question_number=10

# generate the questions to be asked in this instance and save them to the order list
while(len(order) < question_number):
    temp=randrange(len(answer_key))
    if(temp not in order):
        order.append(temp)
# print out the possible accepted answers
print("Accepted text answers are: ")
for i in answer_key:
    print(i[1])
# Port number to protocol questions
for i in order:
    count+=1
    print("Question "+str(count)+" of "+str(len(order)))
    print("what protocol corrosponds with the following port? "+str(answer_key[i][0]))
    answer=input("Answer: ")
    if(answer.upper()==answer_key[i][1]):
        score+=1;
    else:
        wrong.append(answer_key[i])

# output the ports for the user to review
if(len(wrong) > 0):
    print("Review the following")
    for i in wrong:
        print(str(i[0])+"->"+i[1])

print("Score : "+str(score)+"/"+str(len(order)))
print("Percentage: %"+str(score/len(order)*100))
input()
