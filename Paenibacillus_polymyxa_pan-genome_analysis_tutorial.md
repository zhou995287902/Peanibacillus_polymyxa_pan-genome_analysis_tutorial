# Paenibacillus polymyxa strains pan-genome analysis tutorial

## 1. Strains sequence downloads

```shell
cd Data/
python3 ../../scripts/download_ref_seq.py Bacillus_amyloliquefaciens strain_list_add_num.txt > cmd_download_seq.sh
bash cmd_download_seq.sh
```

## 2. Phylogenetic analysis

### 2.1 16S rRNA Phylogenetic analysis

#### 16S rRNA sequence prediction  

```shell
cd ../Analysis/16srRNA/
python ../../scripts/prediction_16SrRNA.py ../../Data/*.fna
python ../../scripts/create_16SrRNA.py ./*.fsa
```

16S rRNA phylogenetic tree was generated using MEGAX according to the neighbor-joining algorithm

### 2.2  Core -genome SNP phylogenetic tree

Harvest suite tools ParSNP and Gingr were used to align whole genome, to visualize single nucleotide polymorphism (SNP) density, and to establish phylogenetic relationship among strains (Treangen et al., 2014). The SNP phylogenetic tree between the genome sequenced *P. polymyxa* strains was established using Harvest suite tools.

```shell
cd ../parsnp_analysis/
bash cmd_parsnp.sh
```

### 2.3 Orthologous protein cluster phylogenetic tree

Consensus tree was built using one thousand bootstrap replicates. Homologous coding sequences (CDS) from these 14 *P. polymyxa* genomes were predicted using OrthoMCL (Li et al., 2003). Orthologous groups were predicted by all-versus-all BLASTp comparison using the Markov Clustering Algorithm (MCL). Multiple sequence alignment was created using MAFFT software. Quality control comparison was conducted with Gblocks software. orthologous protein cluster phylogenetic tree was generated using MEGAX according to the neighbor-joining algorithm.

```shell
cd ../Orthomcl_analysis/
bash cmd_Orthomcl.sh
```

### 2.4 The average nucleotide identity (ANI) phylogenetic tree

The average nucleotide identity (ANI) values were calculated using MUMmer algorithm of JSpecies v1.2.1 and visualized as a heatmap using R language

## 3.   Pan-genome and core genome analyses

Pan-genome and core genome of *P. polymyxa* were obtained by BPGA pipeline. 

## 4.  COG and KEGG functional classification of genes

### 4.1 COG analysis

```shell
cd ../COG_analysis_out
bash cmd_2_diamod_blast_COG.sh
bash cmd_tidy_class.sh
```

### 4.2 KEGG analysis

KEGG Orthology (KO) functional annotation of core, accessory, and unique genomes was performed using KAAS online tools (KEGG Automatic Annotation Server: https://www.genome.jp/kaas-bin/kaas_main).

```shell
cd ../KEGG_pathway_analysis/
bash cmd_kegg_analysis.sh
```

## 5. Secondary metabolite cluster analysis

The software antiSMASH 5.0 (antibiotics and secondary metabolite analysis shell) was used to predict the secondary metabolite clusters.

```shell
cd ../secondary_metabolite_biosynthetic_gene_clusters/
bash cmd_1.sh
```

## 6. Genomic islands analysis

IslandViewer 4 server was used to identify the genomic island (GI) of the 14 *P. polymyxa* strains.

```shell
cd ../Gene_ISland_analysis
bash cmd_count_gene_Island_gene.sh
```

