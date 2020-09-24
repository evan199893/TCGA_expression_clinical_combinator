library(TCGAbiolinks)
query<- GDCquery(project = "TCGA-DLBC", 
                 experimental.strategy = "miRNA-Seq",
                 data.category = "Transcriptome Profiling",
                 data.type = "miRNA Expression Quantification")
GDCdownload(query)
clinical <-GDCquery_clinic(project = "TCGA-DLBC",type = "clinical")
write.csv(clinical, file = '/Users/evan/GDCdata/TCGA-DLBC_Clinical.csvical.csv', row.names =F)
