import matplotlib.pyplot as plt

Ecoli_genome_file = open('DnaA_Boxes_of_E.coli/E.coli_genome.txt') # Open genome sequence
Ecoli_genome = list(Ecoli_genome_file.read()) # Create a genome sequence list


GC_graph = []
k = 0
GC_count = 0
nucleotide_count = []
OriC = [] # Sequence of possible OriC
r_OriC = [] # Reverse sequence of OriC

for nucleotide in Ecoli_genome: # Create a list containing k and #G-#C data points
    k+=1
    nucleotide_count.append(k)
    if nucleotide == 'G':
        GC_count += 1
        GC_graph.append(GC_count)
    elif nucleotide == 'C':
        GC_count -= 1
        GC_graph.append(GC_count)
    else:
         GC_graph.append(GC_count)

plt.plot(nucleotide_count,GC_graph)
plt.xlabel('k')
plt.ylabel('#G-#C')
plt.title("#G-#C at the relative location (k) in genome of E. coli")
# plt.show()

## On the left of OriC, #G - #C decreases. On the right of OriC, #G-#C increases.
## The OriC is at where #G - #C is lowest
## Length of OriC in E.coli K-12 M1666 is 232 bp.

OriC_start = nucleotide_count[min(GC_graph)] - 232 # OriC start after location of this nucleotide
OriC_end = nucleotide_count[min(GC_graph)] + 232 # OriC end after location of this nucleotide
OriC = Ecoli_genome[OriC_start:OriC_end]

## Length of DnaA box is known to be 9 bp

for nucleotide in OriC:
    if nucleotide == '\n':
        OriC.remove(nucleotide)

for nucleotide in OriC: #Create reverse strain of OriC
    if nucleotide == 'A':
        r_OriC.append('T')
    if nucleotide == 'T':
        r_OriC.append('A')
    if nucleotide == 'G':
        r_OriC.append('C')
    if nucleotide == 'C':
        r_OriC.append('G')
    
nine_mers = []

for k in range(len(OriC)-9):
    nine_mers.append(''.join(OriC[k:(k+8)]))

for k in range(len(r_OriC)-9):
    nine_mers.append(''.join(r_OriC[k:(k+8)]))

count_nine_mers = {}

for a_nine_mer in nine_mers:
    if not (a_nine_mer in count_nine_mers):
        count_nine_mers[a_nine_mer] = 0
    count_nine_mers[a_nine_mer] += 1

for a_nine_mer in count_nine_mers:
    if count_nine_mers[a_nine_mer] == 2:
       print (a_nine_mer, count_nine_mers[a_nine_mer])