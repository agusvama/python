import csv
with open("test.csv","rb") as source:
    rdr= csv.reader( source  )
    with open("test2.csv","wb") as result:
        wtr= csv.writer( result  )
        for r in rdr:
            wtr.writerow( (r[2], r[4]))
