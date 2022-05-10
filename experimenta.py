import random 
random.seed(7)
random.choice('ACGT')
import csv
from index import hashtable

# Making dummy Data for Refrence Genome or healthy human
def make_virtual_Fasta(n_bases):
    seq=''
    for _ in range(n_bases):
        seq+=random.choice('ACGT')
    return seq

seq=make_virtual_Fasta(3000)
print('Refrence Genome')
print(seq)   
print('-'*120)  

# Making dummy Data for disesed human

diseasd_seq=seq
diseasd_seq[10:20]=make_virtual_Fasta(10)

# some pattern  to find in refrence genome
print('pattern')
p =seq[10:20]   
print(p)


print('---'*50)       
indexed_genome=hashtable(seq,5)

print(indexed_genome) 



# convert the bulk data to csv file 
# with open('ur file.csv','w') as out:
#     csv_out=csv.writer(out)
#     csv_out.writerow(['k_mer','position'])
#     for row in indexed_genome:
#         csv_out.writerow(row)