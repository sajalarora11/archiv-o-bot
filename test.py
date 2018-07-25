#This is an experiment file by using different open source packages. This script has an array approach of taking each mail as one element of array.
import mailparser
import re

# This code removes all the junk text and put mails in an array with just Subject and body per element.
mails = list()
body = ""
with open("testing.txt") as f:
    for line in f:
        if line.startswith("From "):
            if body != "":
                mails.append(body)
                body = ""
            continue
        else:
            #line = re.sub("\n", " ", line)
            if not any(line.startswith(kw) for kw in ("From:", "To:", "Date", ">", "-", "In-Reply-To:", "References:", "Message-ID:", "\n", "Cc:", "Sent:", "On", "\t", "Hello", "Hi", "Regards", "With Regard", "To unsubscribe", "To change", "Voice your", "visit the list", "http", "hello", "hi", "hey", "hai", "thanks", "regards", "warm regards", "with regards")):
                body = body + line
    mails.append(body)
    print(body)
    # The below code uses the package mailparser that simply pulls out the subject and body alone out of emails...
    # for mail in mails:
    #     print(mail)
