import csv
f= open("performance.csv","r")
reader = csv.reader(f)
headers = next(reader, None)

column = {}
for h in headers:
    column[h] = []
for row in reader:
    for h,v in zip(headers,row):
        column[h].append(v)


def final_review():
    reviews= column["Final Review"]
    counts_review = dict()
    for re in reviews:
        counts_review[re] = counts_review.get(re,0)+1
    print("Counts review: ", counts_review)
    if counts_review["Low"] >= (counts_review["Good"]):
        print("Overall performance is critical")
    if counts_review["Medium"] >= (counts_review["Good"]+counts_review["Low"]):
        print("Overal performance is low")
    if counts_review["Good"] >= counts_review["Medium"]:
        print("Overall personel is OK")
#final_review()

def description_feedback():
    description = column["Description"]
    counts_description = dict()
    words=list()
    for de in description:
        de= de.rstrip()
        de = de.split()
        for quality in de:
            quality = quality.split("\n")
            for word in quality:
                counts_description[word] = counts_description.get(word,0)+1
    return counts_description

def frequent_word():
    bigcount = None
    for w,c in description_feedback().items():
        if bigcount is None or c >bigcount:
            bigcount = c
    for k,v  in sorted(description_feedback().items(),key=lambda item:item[1]):
        print(k,v)
    print(f"The frequent is: {bigcount}")
#frequent_word()

def need_assessment():
    for need in column["Description"]:
        need= need.rstrip().lower()
        if "need" in need :
            ab= need.find("need")
            ba= need.find(" ",ab)
            #print(need[ab:ba])
            ca = need.find(" ",ba)
            print(need[ab:])
#need_assessment()

def employee_assessment():
    for i in open("performance.csv"):
        i=i.rstrip().lower()
        if "need"  in i:
            one=i.find(",")
            two=i.find(",",one)
            fin=i.find(" ",two)
            employee_name= i[(two+1):fin]
            ab = i.find("need")
            ba = i.find(" ",ab)
            ca = i.find(",",ba)
            print(f" Employee: {employee_name} require: {i[ab:ca]}")
#employee_assessment()

def employee_email():
    name1 = column["Name of employee"]
    name2 = column["last name"]
    ema= []
    co =0
    for a in name1:
        co = co + 1
        mail = (f"{a}_{name2[co-1]}@company.edu")
        ema.append(mail)
        column["email"]= ema
    print(column["email"])
#employee_email()

