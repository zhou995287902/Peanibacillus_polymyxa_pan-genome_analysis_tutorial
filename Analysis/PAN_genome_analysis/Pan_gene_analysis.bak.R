## 绘制核心基因数目和泛基因组数目的关系图
library(ggplot2)
library(ggthemes)
library(plyr)
setwd('D:/share/Paenibacillus_polymyxa_pan_genome_project/PAN_genome_analysis/')

data_summary <- function(data, varname, grps){
  require(plyr)
  summary_func <- function(x, col){
    c(mean = mean(x[[col]], na.rm=TRUE),
      sd = sd(x[[col]], na.rm=TRUE))
  }
  data_sum<-ddply(data, grps, .fun=summary_func, varname)
  data_sum <- rename(data_sum, c("mean" = varname))
  return(data_sum)
}

pan_genome_num = read.table('./pan_genome1.txt',sep = '\t',header = T)
colnames(pan_genome_num) <- c('Pan_Number_of_genomes', 'Pan_genome')

#pan_genome_num1 <- data_summary(pan_genome_num,varname = 'Pan_genome',grps = 'Pan_Number_of_genomes')
core_genome_num = read.table('./core_genome1.txt',sep = '\t',header = T)
colnames(core_genome_num) <- c('Core_Number_of_genomes','Core_genome')

head(pan_genome_num)
head(core_genome_num)


all_genome_num <- cbind(pan_genome_num,core_genome_num)
colnames(all_genome_num) <- c('Pan_Number_of_genomes', 'Pan_genome', 'Core_Number_of_genomes','Core_genome')
head(all_genome_num)

#mydata_all <- merge(pan_genome_num,core_genome_num,by=c('Pan_Number_of_genomes','Core_Number_of_genomes'),all=T)


## 画箱线图
core_genome_num$Core_Number_of_genomes <- factor(core_genome_num$Core_Number_of_genomes)
pan_genome_num$Pan_Number_of_genomes <- factor(pan_genome_num$Pan_Number_of_genomes)
all_genome_num <- cbind(pan_genome_num,core_genome_num)
colnames(all_genome_num) <- c('Pan_Number_of_genomes', 'Pan_genome', 'Core_Number_of_genomes','Core_genome')

## 计算核心基因和特有基因的拟合曲线
pan_genome_num_mean <- tapply(pan_genome_num$Pan_genome,pan_genome_num$Pan_Number_of_genomes,mean)
core_genome_num_mean <- tapply(core_genome_num$Core_genome,core_genome_num$Core_Number_of_genomes, mean)
## 计算Pan基因的非线性拟合曲线
pan_genome_num_mean <- as.data.frame(pan_genome_num_mean)
pan_genome_num_mean$gene_num <- c(1:14)
head(pan_genome_num_mean)
pan_genome_nls <- nls(pan_genome_num_mean~theta1*gene_num^theta2+theta3,start=list(theta1=1000,theta2=0.1,theta3=2000),data = pan_genome_num_mean,trace = T)
summary(pan_genome_nls)

ggplot(pan_genome_num_mean,aes(gene_num,pan_genome_num_mean))+
  geom_point(size=3)+geom_line(aes(gene_num,fitted(pan_genome_nls)),col='red')

## 计算core基因的非线性拟合曲线
core_genome_num_mean <- as.data.frame(core_genome_num_mean)
core_genome_num_mean$gene_num <- c(1:14)
head(core_genome_num_mean)
core_genome_nls <- nls(core_genome_num_mean~theta1*exp(gene_num*theta2)+theta3,start = list(theta1= 2000,theta2=-0.3,theta3=2000),data = core_genome_num_mean,trace = T)
#core_genome_nls <- nls(core_genome_num_mean~theta1*gene_num^theta2+theta3,start = list(theta1= -500,theta2=0.3446,theta3=2000),data = core_genome_num_mean,trace = T)
summary(core_genome_nls)

ggplot(core_genome_num_mean,aes(gene_num, core_genome_num_mean))+
  geom_point(size=3)+geom_line(aes(gene_num,fitted(core_genome_nls)),col='red')

head(all_genome_num)
## 设置字体
windowsFonts(myFont = windowsFont("Times New Roman"))

p <- ggplot(all_genome_num)+
  geom_boxplot(aes(Pan_Number_of_genomes,Pan_genome),fill='cyan',width = 0.2)+
  #geom_errorbar(aes(pan_genome_num1$Number.of.genomes,pan_genome_num1$Pan.genome,ymin=pan_genome_num1$Pan.genome- pan_genome_num1$sd,ymax=pan_genome_num1$Pan.genome+ pan_genome_num1$sd), width=0.2)
  geom_boxplot(aes(Core_Number_of_genomes,Core_genome),fill='pink',width = 0.2)+
  labs(title="Core and Pan Genome Plot", x="Number of Genomes", y="Number of Gene Families",fill='')+
  ylim(2000,10000) +
  theme_bw()+
  theme(title = element_text(size = 15, family = "myFont"),plot.title = element_text(hjust = 0.5))

ggsave('pan_boxplot.png',p,width = 10,height = 8)

## 画点图
q <- ggplot(data=all_genome_num,aes(Pan_genome,Core_genome)) +
  geom_point(aes(Pan_Number_of_genomes,Pan_genome),colour='cyan')+
  geom_line(data=pan_genome_num_mean,aes(gene_num,fitted(pan_genome_nls)),
            #col='orange',
            col='cyan')+
  #geom_smooth(aes(x=Pan_Number_of_genomes,y=Pan_genome),method="auto",se=F,formula = y ~ x,colour='orange')+
  geom_point(aes(Core_Number_of_genomes,Core_genome),
             #colour='violet',
             colour='pink')+
  geom_line(data=core_genome_num_mean,aes(gene_num,fitted(core_genome_nls)),col='pink')+
  #geom_smooth(aes(Core_Number_of_genomes,Core_genome),method="auto",se=F,formula = y ~ x,colour='violet') +
  labs(title="Core and Pan Genome Plot", x="Number of Genomes", y="Number of Gene Families",fill='')+
  ylim(2000,10000) +
  theme_bw()+
  scale_colour_manual(name=c('A',"B",'C','D'),values=c('cyan','orange','pink','violet'))+
  theme(title = element_text(size = 15, family = "myFont"),plot.title = element_text(hjust = 0.5))


ggsave('pan_point.png',q,width = 10,height = 8)

