#install.packages("gggenes")
setwd('../KEGG_pathway_analysis/14_Paenibacilus_polymyxa_KEGG/')
library(ggplot2)
library(gggenes)
gene_structure <- read.table('nif_gene_structure.table',sep = '\t')
head(gene_structure)
nif_gene_structure <- gene_structure
colnames(nif_gene_structure) <- c('molecule','gene','start','end','strand','direction')
head(nif_gene_structure)
nif_gene_structure$strand<- as.vector(nif_gene_structure$strand)
nif_gene_structure$start <- as.numeric(nif_gene_structure$start)
nif_gene_structure$end <- as.numeric(nif_gene_structure$end)
nif_gene_structure$gene <- as.character(nif_gene_structure$gene)
nif_gene_structure$molecule <- as.character(nif_gene_structure$molecule)
nif_gene_structure$direction <- as.character(nif_gene_structure$direction)
for (i in 1:length(nif_gene_structure$strand)){
  if (nif_gene_structure$strand[i] == '+'){nif_gene_structure$strand[i] <-  'forward'}
  if (nif_gene_structure$direction[i] == '+'){nif_gene_structure$direction[i] <-  1}
  if (nif_gene_structure$strand[i] == '-'){nif_gene_structure$strand[i] <-  'reverse'}
  if (nif_gene_structure$direction[i] == '-'){nif_gene_structure$direction[i] <-  -1}}
nif_gene_structure$direction <- as.numeric(nif_gene_structure$direction)
#dummies <- make_alignment_dummies(nif_gene_structure, aes(xmin = start, xmax = end, y = molecule, id = gene),on = "nifB" )
## 设置字体
windowsFonts(myFont = windowsFont("Times New Roman"))

p1 <- ggplot(nif_gene_structure, aes(xmin = start, xmax = end, y = molecule, fill = gene,label = gene, forward = direction)) +
  geom_gene_arrow() +
  facet_wrap(~ molecule, scales = "free", ncol = 1) +
  #scale_fill_brewer(palette = "Set3") +
  scale_fill_brewer(palette = "Paired") +
  theme_genes()+
  labs(title="Nitrogen Fixation", x="", y="")+
  theme(title = element_text(size = 15, family = "myFont"),plot.title = element_text(hjust = 0.5))+
  #geom_blank(data = dummies) +
  geom_gene_label(align = "centre",height = grid::unit(3, "mm"),reflow=T)
ggsave("nif_gene.tiff", p1, width = 8, height = 5,dpi = 300)
