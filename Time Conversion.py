def timeConversion(s):
    # Write your code here
    time = s.split(":")

    if "am" in time[2].casefold() and "12" in time[0]:
        time[0] = "00"
        s = ":".join(time)
        return s.casefold().replace("am", "")

    elif "am" in time[2].casefold() and "12" not in time[0]:
        s = ":".join(time)
        return s.casefold().replace("am", "")
    elif "pm" in time[2].casefold() and '12' in time[0]:
        s = ":".join(time)
        return s.casefold().replace("pm", "")
    else:
        temp = int(time[0])
        temp = temp + 12
        time[0] = str(temp)
        s = ":".join(time)
        return s.casefold().replace("pm", "")


s = input()

result = timeConversion(s)
print(result)

