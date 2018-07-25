import re
with open("testing.txt") as f:
    data = {}
    for line in f:
        # Skip the unnecessary lines
        if any(line.startswith(kw) for kw in ("From ", "From:", "To:", "Date", ">", "-", "In-Reply-To:", "References:", "Message-ID:", "\n", "Cc:", "Sent:", "On", "\t", "Hello", "Hi", "Regards", "With Regard", "To unsubscribe", "To change", "Voice your", "visit the list", "http", "hello", "hi", "hey", "hai", "thanks", "regards", "warm regards", "with regards")):
            continue
        # removes the Subject from the line...
        if line.startswith("Subject:"):
            current_subject = line.split(":")[-1].strip()
        else:
            # Append the subject and the body of the email into a dictionary with sight more cleaning...
            data.setdefault(current_subject, "")
            line = re.sub("\n", " ", line)
            line = re.sub("\t", "", line)
            data[current_subject] += line

print(data)