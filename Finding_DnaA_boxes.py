
Ecoli_genome_file = open('DnaA_Boxes_of_E.coli/E.coli_genome.txt') # Open genome sequence
Ecoli_genome = list(Ecoli_genome_file.read()) # Create a genome sequence list

GC_graph = []
k = 0
GC_count = 0

for nucleotide in Ecoli_genome: # Create a list containing k and #G-#C data points
    k+=1
    if nucleotide == 'G':
        GC_count += 1
        GC_graph.append([k,GC_count])
    elif nucleotide == 'C':
        GC_count -= 1
        GC_graph.append([k,GC_count])
    else:
         GC_graph.append([k,GC_count])

