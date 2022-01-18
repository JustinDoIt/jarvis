import pandas as pd
import sys
import re
sys.path.append('../analysis/')
from translate import translate_baidu_api

##############################################

# 你现在认为永远不会再看的文章，你以后可能会再看 #
# SOLUTION: 不考虑那么多！！！！！！！！！
##############################################

"""
level 
    5
    4
    3
    2
    1
    0
    100: classical paper like UniProt、PDB、
    -1:   一定不关心，比如 RNA、cancer、tumor

Minimally-overlapping words for sequence similarity search
# ccNetViz: a WebGL-based JavaScript library for visualization of large networks
# 这个最大可视化多大的网络？
RCSB Protein Data Bank 1D Tools and Services

# FASPR: an open-source tool for fast and accurate protein side-chain packing
# ProteinFishing: a protein complex generator within the ModelX toolsuite
# OPUS-TASS: a protein backbone torsion angles and secondary structure predictor based on ensemble neural networks
"""

"""
Biomedical Text Mining

Dataset-aware multi-task learning approaches for biomedical named entity recognition
DeepEventMine: end-to-end neural nested event extraction from biomedical texts


VISAR: an interactive tool for dissecting chemical features learned by deep neural network QSAR models
Fast and accurate prediction of partial charges using Atom-Path-Descriptor-based machine learning


MinReact: a systematic approach for identifying minimal metabolic networks
RSSALib: a library for stochastic simulation of complex biochemical reactions

EnrichrBot: Twitter bot tracking tweets about human genes


Redundancy-weighting the PDB for detailed secondary structure prediction using deep-learning models

# CLPred: a sequence-based protein crystallization predictor using BLSTM neural network
# 结晶预测？

VisFeature: a stand-alone program for visualizing and analyzing statistical features of biological sequences
!!!!!!!!!!!!!!
Seq2Feature: a comprehensive web-based feature extraction tool

GCPred: a web tool for guanylyl cyclase functional centre prediction from amino acid sequence

ChemTreeMap: an interactive map of biochemical similarity in molecular datasets
"""


def print_(texts, msg='', trans=False):
    # print(f"{msg}相关文献共有{len(texts)}篇")
    for text in texts:
        try:
            print(f"{text}") # .decode('utf-8')
            if trans:
                print(translate_baidu_api(text))
        except Exception as e:
            # raise e
            print("[ERROR] unknown error for print this text")
        finally:
            # print("[ERROR] ")
            print('-'*60)


def locate_papers(titles, kws, verbose=False, show_filtered_paper=False, return_filted_papers=True):
    """返回剩余paper和滤掉的paper"""
    filter_titles = [title for title in titles if re.findall(kws, title)]
    if verbose:
        print("")
        if show_filtered_paper:
            print('[INFO] 滤掉了如下这些文章：')
            print('-'*100)
            print_(filter_titles)
    if return_filted_papers:
        return filter_titles
    else:
        raise NotImplementedError("SORRY!!!!! COMING SOON!!!!")



class Papers():
    def __init__(self, titles) -> None:
        """滤掉不关心的文献"""
        self.titles = titles
        self.filtered_titiles = titles
                   
        
        protein_tasks = [
            #'structure'
            'secondary structure prediction',
            'enzyme',
            'solub',
            'stabil',
            'disorder',
            'binding affinity',
            'co-evolut',
            'coevolut',
            'evolution',

            'protein',
            'dynamic simulation',
            'dynamics simulation',
            'md simulations',
            'dock',
            'scoring function', 
            'deep mutational scanning',
            'ancestral sequence reconstruction',
            'ancestral reconstruction',
            # 'language model',  # 这不是生物学问题
            # 'embedding',
            # ---------
            'binding site',
            'active site',
            'site predict', # phosphorylation site prediction
            'contact map',
            'contact predict',
            # '',
            'feature extract',

            'feature selection',

            'sequence similarity',
            'visualization',
            'visual',
            # ----------
            'cluster',
            # ----------
            'biomedical text',
            'biomedical named entity recog',
            'text mining',
            'biomedical link predict',
            'biomedical literature',
            'ambiguous biomedical name', #Semantic persistence of ambiguous biomedical names in the citation network
            'biomedical event extract',
            # -----------
            'de bruijn',
            'electron density', # chemical 
            'biochemical reaction',
            'chemical reaction',

            'molecular',
        ]

        BLOCK_kws = [
            'single-cell gene expression data',
            'single-cell',
            'human',
            'tumour',
            'breast cancer',
            # ------ 
            'multi-omics',
            'omic',
            'nanopore*seq',
            # ----------
            'cancer',
            'tumor',
            'clinical',
            'antigen',
            'antibody',
            'anticancer',
            'vaccine',
            't cell receptor',
            't-cell receptor',
            'b cell receptor',
            'b-cell receptor',
            'disease',
            # ------ 医学task
            'drug-target interaction', # AND predict
            'drug-drug interaction', # AND predict
            'blood',
            'tissue',
            'drug response',
            'drug',
            'imaging data',
            'imaging',
            'image',
            'immune',
            'survivaL analys',
            'survival analysis',
            'survival',
            # ---------------
            'signalling',
            'signaling',
            # ---------------
            'biomarker',
            'marker',
        ]
        # 模糊
        CLASSICAL_BIOINFO = [
            'copy number',
            'non-coding',
            # ---------------------------
            'gene regulatory',
            'target gene predict',
            'multiple sequence alignment',
            'multiple sequences alignment',
            'alignment',
            'phylogenetic tree',
            'phylogenetic',
            # ---------------------------
            'transcript*regulatory network',
            'gene interaction network',
            'gene regulatory network',
            'regulatory gene',
            'regulatory network',
            'gene expression',
            'driver gene',
            'long read', # long*read
            'long-read',
            'short-read',
            'short read'
            'transcrip',
            'transcription factors',
            'gene ontology',
            'phenotype predict',
            'variant calling',
            'variant calli',
            'mutation calling',
            'variation',
            'geno assembly',
            'genome assembly',
            'assemble',
            'primer design',
            'primer3',
            'primer',
            'plasmid',
            'genome-wide association studies',
            'n4-methylcytosine site', # predict @PTM @
            'nanopore',
            'tandem repeat',
            'species tree',
            'species network',
            'signaling network',
            'remote homology detection',
            'ngs read alignment',
            'differential gene',
            'genome-wide association stud',
            'epigenome-wide-association stud',
            'epigenome wide association stud',
            'genome analysis',
            'dna methylation analysis',
            'methylation detection',
            'dna methylation',
            'sigma promoter',
            'enhancer'
            'promoter',
            'intron',
            'quality control',
            'quality assessment',
            'variant detection',
            'epigenetic state predict',
            'antimicrobial peptide',
            'batch effect',
            'synonymous codon',
            # --------------------
            'pathway reconstruction',
            'metabolic pathway',
            'pathway',
            # --------------------
            'gene annotation',
            'function annotation',
            # --------------------
            'mass spectrometr',
            'x-ray',
            'protom*',
            # --------------------
            'codon optimization', # TODO 忽略大小写
            # -------------------- 大词放后面
            'annotation',
            'predict isoform functions',
            'thermodynamics-based flux analysis',
            'metabolic flux'
            'flux balance',
            'metabolic network',
            'metabolic reconstruction',
            'sequencing data',
            'genome sequencing',
            'sequencing'
            'flux',
            'metabolic',
            'reaction',
            # '' # 代谢网络重建
        ]

        CLASSICAL_BIOINFO_upcase = [
            'CRISPR',
            'PCR',
            'DNA',
            'RNA-seq',
            'lncRNA',
            'single-cell RNA',
            'RNA',
            'COVID-19',
            'CITE-seq',
            'ChIP-seq',
            'ChIP',
            'Hi-C',
            'Ribo-seq',
            '4C-seq',
            'RAD-seq',
            'BS-seq'
            'Tn-seq',
            'ATAC-seq',
            
            'FASTQ file',
            
            'Illumina',
            'SNP-gene-disease network',
            'SNP',
            'next-generation sequencing',
            'GWAS',
            'NGS',
            'reads',

            # ---------------
            'QSAR',
            'virtual screening',
            # ---------------
            'NMR',
            'MATLAB', # 专门为这个语言写的一个包，其实里面就存在大量机会
            'Matlab',
            'Julia',
            'R package',
            'R-package',
            ' R ',
            'an R',
            'in R',
            'in program R',
            'JavaScript', # visual*
            'Javascript',
            # 'a* package',
            # --------------------
        ]
        # 筛掉 MATLAB 等
        print("严格大小写滤掉")
        for index, kws in enumerate(CLASSICAL_BIOINFO_upcase):
            self.filter_papers(kws)
            print(f"[INFO] epoch {index} done. {kws:30} res: {len(self.filtered_titiles)}")
        # 忽略大小写（全部转换为小写
        print("忽略大小写敏感")
        for index, kws in enumerate(BLOCK_kws + CLASSICAL_BIOINFO):
            self.filter_papers(kws, CaseMatch=False)
            print(f"[INFO] epoch {index} done. {kws:30} res: {len(self.filtered_titiles)}")
        print("专业词汇")
        for index, kws in enumerate(protein_tasks):
            self.filter_papers(kws, CaseMatch=False)
            print(f"[INFO] epoch {index} done. {kws:30} res: {len(self.filtered_titiles)}")

        print_(self.filtered_titiles)
        print("Done")
        
    def filter_papers(self, kws, CaseMatch=True, log=False, log_filtered_paper=False, return_filted_papers=False):
        """返回剩余paper和滤掉的paper"""
        if CaseMatch:
            self.filtered_titiles = [title for title in self.filtered_titiles if not re.findall(kws, title)] # MATLAB
        else:
            self.filtered_titiles = [title for title in self.filtered_titiles if not re.findall(kws, title.lower())] # 忽略大小写 == 全部转换为小写
        # if verbose:
            # print("")
            # if show_filtered_paper:
            #     print('[INFO] 滤掉了如下这些文章：')
            #     print('-'*100)
            #     print_(filter_titles)
        # if return_filted_papers:
        #     return filter_titles
        # else:
        #     raise NotImplementedError("SORRY!!!!! COMING SOON!!!!")




        


def main():
    FILE = '../data/2015-2020_Bioinforma-set.csv'
    df = pd.read_csv(FILE)
    titles = df['Title']
    # print_(titles)
    p = Papers(titles)
    # print(".")



if __name__ == "__main__":
    main()