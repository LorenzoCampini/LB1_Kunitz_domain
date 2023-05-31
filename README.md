# LB1_Kunitz_domain

This is my GitHub repository for the LB1 project. The aim of the project is to create a method 
to annotate proteins in SwissProt and classify them as Kunitz or non-Kunitz. 
For this purpose three HMMs were developped from multiple structure alignment of entries from PDB.
Below are listed the various filters used to select the structures:

- First model 
    - Pfam identifier = PF00014, 
    - Resolution <= 3.0 Å, 
    - 50 < polymer entity length < 70, 
    - mutation count = 0
	Before modifying anything they are 21 ids
  In this model 5NX1:D was mapped to 05067 as was 1AAP:A

- Second model 
    - SCOP2 identifier = 4003337, 
    - Pfam identifier = PF00014, 
    - Resolution <= 3.0 Å, 
    - 50 < polymer entity length < 70
	Before modifying anything they are 13 ids

- Third model 
    - CATH identifier = 4.10.410.10, 
    - Pfam identifier = PF00014, 
    - Resolution <= 3.0 Å, 
    - 50 < polymer entity length < 70
	Before modifying anything they are 22 ids
  In this model 5NX1:D was mapped to 05067 as was 1AAP:A



Files with the extention .csv contain the Entry ID and the Auth Asym ID of the selected protein strctures
Files with the extention .pdbids contain the IDs identifying structures from PDB database
Files with the extention .ids contain the IDs indentifying sequences from UniProt/SwissProt database
Files with the extention .fasta contain protein sequences in fasta format
Files with the extention .search contain the result from the hmmsearch command
Files with the extention .hmm contain the HMM file
Files with the extention .bl8 contain the result of the blast operation of the training set against the positive example of kunitz domain
Files with the extention .logo contain the HMM logo for the relative HMM


For more information look at the report






