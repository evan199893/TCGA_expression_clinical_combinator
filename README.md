# TCGA_miRNA_expression_clinical_combinator
1. You should download the expression data and clinical in advanced.
2. Make sure you download the correct metadata.cart.json file on TCGA webpage. In this program will use .json to convert the expression file name.
   e.g: Project: TCGA-STAD, Data Category: Transcriptome Profiling, Data Type: miRNA-Seq. ##Should set correct.
3. You should check wether the the column index is the data you want. (Surival,Stage) In different project may arrange a little differenet. Setting at line #45.
4. Before running the program you should setting the correct absolute path in the specific place.(Line #9,20,37)
5. Setting the output file place at line #39.  
6. The miRNA/gene expression default is RPKM and take log2 in advanced if you don't need that or you need the read count you can change the defaul by yourself.(Line #88, 95)
7. I update the program to the user input mode. When you run the program it will ask you to input specific data file absolute path. 
8. I upload a R script about dowaload the TCGA data. 
