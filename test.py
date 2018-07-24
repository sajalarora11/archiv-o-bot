import mailparser
import re

# This code removes all the junk text and put mails in an array with just Subject and body per element.
mails = list()
body = ""
with open("2010q2.txt") as f:
    for line in f:
        if line.startswith("From "):
            if body != "":
                mails.append(body)
                body = ""
            continue
        else:
            if not any(line.startswith(kw) for kw in ("From:", "To:", "Date", ">", "-", "In-Reply-To:", "References:", "Message-ID:", "\n", "Cc:", "Sent:", "On", "\t", "Hello", "Hi", "Regards", "With Regard", "To unsubscribe", "To change")):
                body = body + line
    mails.append(body)
    print(mails)
    # The below code uses the package mailparser that simply pulls out the subject and body alone out of emails...
    for mail in mails:
        mail = mailparser.parse_from_string(mail)
        print(mail.body)
