from datetime import datetime, timedelta

mydatehr_str = '27-11-2005 11:15:45'
mydatehr = datetime.strptime(mydatehr_str, '%d-%m-%Y %H:%M:%S')
datenow = datetime.now()

totY = datenow.year - mydatehr.year
totm = datenow.month - mydatehr.month
totd = datenow.day - mydatehr.day
totH = datenow.hour - mydatehr.hour
totM = datenow.minute - mydatehr.minute
totS = datenow.second - mydatehr.second

mydate = ('{:}anni - {:}mesi - {:}giorni - {:}ore - {:}minuti - {:}secondi'.format(totY, totm, totd, totH, totM, totS))

print(mydate)



