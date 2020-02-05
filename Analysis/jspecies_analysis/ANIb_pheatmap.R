#!/usr/bin/env Rscript
library("ggplot2")
library("reshape")
library('pheatmap')
setwd('D:/share/Paenibacillus_polymyxa_pan_genome_project/jspecies_output/')
strain_name <- c('ANI','ZF197','SQR21','ZF129','YC0136','CF05','M1','ATCC','SC2','YC0573','HY96','J','Sb3','CR1','E681')
userprefs <- commandArgs(trailingOnly = TRUE)
# file_name <- userprefs[1]
file_name <- 'ANIb.tab'
# read file
data.ANI <- read.table(file_name,sep = '\t',header = T)
colnames(data.ANI) <- strain_name
row.names(data.ANI) <- strain_name[-1]
data.ANI <- data.ANI[,-1]
data.ANI <- as.matrix(data.ANI)
data.ANI <- data.ANI/100
#yanse <- colorRampPalette(c("#0577fa","yellow","red"))(nrow(data.ANI))
yanse <- colorRampPalette(c("green","yellow","red"))(nrow(data.ANI))

# heatmap
heatmap(data.ANI,col=yanse)


# pheatmap
pheatmap(data.ANI,color=yanse,cluster_rows = T,cluster_cols = T,
         display_numbers = T,cutree_rows = 5,cutree_cols = 5,
         treeheight_col=0,treeheight_row = 0,
         labels_row = rep('',nrow(data.ANI)),labels_col = rep('',ncol(data.ANI)),
         filename = 'ANIb.png',width = 10,height = 8)


# cluster and order matrix
row.order <- hclust(dist(data.ANI))$order # clustering
col.order <- hclust(dist(t(data.ANI)))$order
dat_new <- data.ANI[row.order, col.order] # re-order matrix accoring to clustering

# melt to dataframe
df_molten_dat <- melt(as.matrix(dat_new)) # reshape into dataframe
names(df_molten_dat)[c(1:3)] <- c("shewanella1", "shewanella2", "ANI")

# make plot
p1 <- ggplot(data = df_molten_dat,
             aes(x = shewanella1, y = shewanella2, fill = ANI)) +
  geom_raster() +
  scale_fill_distiller(palette = "RdYlBu", limits=c(0.8, 1)) +
  theme(axis.text.x = element_text(angle = 90, hjust = 1)) +
  ggtitle("Shewanella ANI heatmap")+
  geom_text(aes(label = round(ANI, 2)))+
  theme(axis.title=element_text(size=16), strip.text.x=element_text(size=16),
        legend.title=element_text(size=15), legend.text=element_text(size=14),
        axis.text = element_text(size=14), title=element_text(size=20),
        strip.background=element_rect(fill=adjustcolor("lightgray",0.2))
  )

# export plot
png("Heatmap_ANI_highres.png", width=15, height=15, units="in", pointsize=12, res=500)
p1
dev.off()
