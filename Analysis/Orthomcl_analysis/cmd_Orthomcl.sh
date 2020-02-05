### AdjustFasta
orthomclAdjustFasta ATTC ~/share/Paenibacillus_polymyxa_pan_genome_project/strain_seq/input_directory/protein_sequence/ATCC_15970_GCA_001922145.1_ASM192214v1_protein.faa 1
orthomclAdjustFasta CF05 ~/share/Paenibacillus_polymyxa_pan_genome_project/strain_seq/input_directory/protein_sequence/CF05_GCF_000785455.1_ASM78545v1_protein.faa 1
orthomclAdjustFasta CR1 ~/share/Paenibacillus_polymyxa_pan_genome_project/strain_seq/input_directory/protein_sequence/CR1_GCA_000507205.2_ASM50720v2_protein.faa 1
orthomclAdjustFasta E681 ~/share/Paenibacillus_polymyxa_pan_genome_project/strain_seq/input_directory/protein_sequence/E681_GCA_000146875.2_ASM14687v2_protein.faa 1
orthomclAdjustFasta HY96 ~/share/Paenibacillus_polymyxa_pan_genome_project/strain_seq/input_directory/protein_sequence/HY96-2_GCA_002893885.1_ASM289388v1_protein.faa 1
orthomclAdjustFasta JPA ~/share/Paenibacillus_polymyxa_pan_genome_project/strain_seq/input_directory/protein_sequence/J_GCA_001719045.1_ASM171904v1_protein.faa 1
orthomclAdjustFasta MPA ~/share/Paenibacillus_polymyxa_pan_genome_project/strain_seq/input_directory/protein_sequence/M1_GCA_000237325.1_ASM23732v1_protein.faa 1
orthomclAdjustFasta SC2 ~/share/Paenibacillus_polymyxa_pan_genome_project/strain_seq/input_directory/protein_sequence/SC2_GCA_000164985.2_ASM16498v2_protein.faa 1
orthomclAdjustFasta SQR ~/share/Paenibacillus_polymyxa_pan_genome_project/strain_seq/input_directory/protein_sequence/SQR21_GCA_000597985.1_ASM59798v1_protein.faa 1
orthomclAdjustFasta Sb3 ~/share/Paenibacillus_polymyxa_pan_genome_project/strain_seq/input_directory/protein_sequence/Sb3-1_GCA_000819665.1_ASM81966v1_protein.faa 1
orthomclAdjustFasta YC01 ~/share/Paenibacillus_polymyxa_pan_genome_project/strain_seq/input_directory/protein_sequence/YC0136_GCA_001874405.3_ASM187440v3_protein.faa 1
orthomclAdjustFasta YC05 ~/share/Paenibacillus_polymyxa_pan_genome_project/strain_seq/input_directory/protein_sequence/YC0573_GCA_001874425.3_ASM187442v3_protein.faa 1
orthomclAdjustFasta ZF12 ~/share/Paenibacillus_polymyxa_pan_genome_project/strain_seq/input_directory/protein_sequence/ZF129_GCA_006274405.1_ASM627440v1_protein.faa 1
orthomclAdjustFasta ZF19 ~/share/Paenibacillus_polymyxa_pan_genome_project/strain_seq/input_directory/protein_sequence/ZF197_GCA_007858415.1_ASM785841v1_protein.faa 1
  

                       
### FilterFasta
orthomclFilterFasta compliantFasta/ 10 20 
### blastp
makeblastdb -in goodProteins.fasta -dbtype prot -out good_proteins.fasta
blastp -db good_proteins.fasta -query goodProteins.fasta -outfmt 7 -out goodProteins_blastp.out
grep -v -P "^#" goodProteins_blastp.out > goodProteins_v1_blastp.out
### BlastParser,LoadBlast,Pairs,DumpPairsFiles
orthomclBlastParser goodProteins_v1_blastp.out ./compliantFasta >similarSequences.txt
orthomclLoadBlast ~/biosoft/orthomclSoftware-v2.0.9/my_orthomcl_dir/orthomcl.config similarSequences.txt
orthomclPairs ~/biosoft/orthomclSoftware-v2.0.9/my_orthomcl_dir/orthomcl.config pairs.log cleanup=no 
orthomclDumpPairsFiles ~/biosoft/orthomclSoftware-v2.0.9/my_orthomcl_dir/orthomcl.config
### mcl,MclToGroups
mcl mclInput --abc -I 1.5 -o mclOutput
orthomclMclToGroups No_ 1 <mclOutput >groups.txt