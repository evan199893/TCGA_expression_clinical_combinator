import json
import os
import csv
import math
import operator

filedict={}
##You need to download the metadata.cart.json on TCGA database and setting all correct.
with open('/Volumes/256GB/safari download/metadata.cart.2020-09-23-2.json','r') as f:
    out= json.loads(f.read())   
time=len(out)
print('Scaning metadata.json...')
for i in range(time):
   finame=out[i]['file_id']
   ##print(finame)
   tcgasample=out[i]['associated_entities'][0]['entity_submitter_id']
   ##print(tcgasample)
   filedict[finame]=tcgasample
##Setting miRNA_Expression_Quantification directiory absolute path
yourPath='/Users/evan/GDCdata/TCGA-DLBC/harmonized/Transcriptome_Profiling/miRNA_Expression_Quantification'
allFileList = os.listdir(yourPath)
cou=0
print("Start converting!")
for origin_name in allFileList:
    cou+=1
    if origin_name =='.DS_Store': continue  
    if origin_name not in filedict: continue
    newfol=filedict[origin_name]
    orglo = yourPath + '/'+ origin_name
    new_loc = yourPath + '/'+ newfol        
    os.rename(orglo,new_loc)
    print(origin_name+' >>> '+newfol)
print('Convert '+str(cou)+' samples!')

allFileList2 = os.listdir(yourPath)
## clinical csv file absolute path.You need to download clinical csv file in advanced.
with open('/Users/evan/GDCdata/TCGA-DLBC_Clinical.csvical.csv',newline='') as csvfile:
    ##Product final miRNA survival csv file name, setting the location 
    with open('/Users/evan/GDCdata/dlbcmirnaexp.csv','w') as newcsv:
        rows=csv.reader(csvfile)
        c3writer=csv.writer(newcsv)
        for r in rows:
            ##delete alive
            ##Set the column index of 'days to death' of clinical csv
            survival=r[45]
            if survival=='NA': continue 
            if r[0]=='submitter_id':
                ##Randomly chose mirna file build mirna label
                 path1=yourPath+'/'+allFileList2[1]
                 mirnatxt=os.listdir(path1)
                 optxt=open(path1+'/'+mirnatxt[0])
                 optxtl=optxt.readlines()
                 lst=[]
                 for lin in optxtl:
                    linesp=lin.split()
                    if linesp[0]=='miRNA_ID': continue
                    lst.append(linesp[0])
                 c3writer.writerow([r[0]]+[survival]+lst)
                 optxt.close()
                 continue
            else:
                ##Ignoring dead <30 days            
                if int(survival)<30: continue
                newr1=round(int(survival)/30,2)
                for oned in allFileList2:
                    ##print(oned[13:15])
                    ##Ignoring normal cell samples
                    if oned[13:15]=='11': continue
                    if oned =='.DS_Store': continue
                    if oned[0:12]==r[0]:
                        lstt=[]
                        lstt2=[]
                        path11=yourPath+'/'+oned
                        mirnatxtr=os.listdir(path11)
                        optxtt=open(path11+'/'+mirnatxtr[0])
                        optxtll=optxtt.readlines()
                        for linee in optxtll:
                            linespp=linee.split()
                            if linespp[0]=='miRNA_ID': continue
                            if float(linespp[2])==0:
                                lstt.append(linespp[0])
                                lstt2.append(float(linespp[2]))
                            else:
                                ##input miRNA log2(rpkm)
                                lstt.append(linespp[0])
                                lstt2.append(math.log(float(linespp[2]),2))
                         ##write csv file 
                        if (operator.eq(lst,lstt))==False:
                            print("miRNAs label were different in different patient, should edit this program.")
                        c3writer.writerow([r[0]]+[newr1]+lstt2)  
                        optxtt.close()
                        continue
                    else: continue 
print("MiRNAs expression combine survival csv file create sucessful!!")