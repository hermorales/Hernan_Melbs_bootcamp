reader = open('uniprot_sprot.fasta', 'r')
#noOfHumanProteins=0
#for line in reader:
#    if ( line[0] == '>'):
#print line
#        if "Homo sapiens" in line:
#            noOfHumanProteins+=1
#print "No = ",noOfHumanProteins
#reader.close()


reader = open('uniprot_sprot.fasta', 'r')
noOfHumanProteins=0
for line in reader:
    if ( line[0] == '>' and "Homo sapiens" in line):
#print line
        noOfHumanProteins+=1
print "No = ",noOfHumanProteins
reader.close()
