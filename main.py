with open("2010q2.txt") as f:
    data = {}
    for line in f:
        if any(line.startswith(kw) for kw in ("From:", "To:", "Date", ">", "-", "In-Reply-To:", "References:", "Message-ID:","From" , "\n", "Cc:", "Sent:", "On", "Hello", "Hi", "Regards", "With Regard", "To unsubscribe", "To change")):
            continue
        if line.startswith("Subject:"):
            current_subject = line.split(":")[-1].strip()
        else:
            data.setdefault(current_subject, "")
            data[current_subject] += line

print(data)