# goi2roimapping
Leveraging spatial, anatomical, microarray expression data from the Allen
Institute for Brain Science. This program maps genes of interest (Goi) by their levels of
expression to brain regions (Roi). The identified regions that co-express the input Goi
can, in turn, be studied further with many experimental modalities. This program can be
customized to map gene expression data and identify significant Roi from similar
reference expression data in other contexts outside of neuroscience.

# Purpose
Technologies in experimental neuroscience have exponentially improved,
however, translational neuroscience (from mouse-to-humans) has not been as
successful in producing therapeutics that treat human disease. Although there are many
limitations to research performed with human participants, one of the main advantages
is an easier translation of findings into clinical settings. However, current tools lack the
ability to query molecular and brain-region specific data, an approach that is required
for bedside-to-bench-to-bedside research.

Goi2Roimapping utilizes a compilation of ex vivo, spatial, microarray expression
data from the human brain that is freely available at the Allen Institute for Brain Science.
Goi2Roimapping allows a user to input Goi relevant to their field of study (eg. targets of
microRNAs, genes detected through GWAS, etc.). Once Goi are defined by the user,
Goi2Roimapping will iterate though brain regions and compare expression levels of the
Goi relative to all other genes (using a Wilcoxon test). At the end, the user will obtain
brain Roi where those genes are significantly co-expressed as a .csv file. Additionally,
box plots showing relative expression of the Goi relative to all other genes are
generated. By determining brain regions where input genes are expressed, investigators
can take on exploring different aspects of regional brain function in various modalities,
including human brain imaging. By determining whether Goi are expressed in specific
brain regions, investigators can better inform their current and future experiments.
Ultimately, my aim is that this tool can help neuroscientists bridge the gaps in molecular
neuroscience.

# Dependencies
With minimal experience with other programming languages, I consider this project my
first introduction into programming in general, and certainly my first introduction to
Python. Therefore, I've leveraged several important basic libraries:

pandas – to iterate through dataframes and create new output dataframes.

matplot.lib - to generate boxplots

scipy.stats. - to perform comparisons between input goi and all other genes as we iterate through the dataframe analysis.

This program requires Python 3.8 or higher.

# Using goi2roimapping
In its current form, the program asks the user to input a working directory for the
reference data and brain region key. The program will ask the user for this at key steps when
required and then ask for further required inputs (gene names of interest).
Note that currently, the program is designed to iterate through a dataset
containing median expression values from microarray data of 6 compiled reference
brains. Next, (and soon) I plan to update the program to add an additional output:
mapping the identified brain regions onto a glass brain using Nilearn.
