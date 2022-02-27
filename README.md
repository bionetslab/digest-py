<p align="center">
  <img alt="DIGEST Logo" src="https://github.com/bionetslab/digest/blob/main/digest_logo.png?raw=true" width="500" />
</p>

# biodigest
The python package for [DIGEST](https://digest-validation.net/) (validation of **di**sease and **ge**ne **s**ets or clus**t**erings). It greatly facilitates in silico validation of gene and disease sets or clusterings via fully automated validation pipelines comprising disease and gene ID mapping, enrichment
analysis, comparisons of shared genes and variants, and background distribution estimation. Moreover, functionality is provided to automatically update the external databases used by the pipelines.

[Source code](https://github.com/bionetslab/digest)

## Setup for proper usage
```python
import biodigest
```

Before you can run the validation, you need to download precalculated mappings and distance matrices. These can be downloaded in two ways:
### 1. [Recommended] Get data from api
The API keeps all data up to date and checks for updates at regular intervals. This process takes 1-5 minutes depending on the internet connection.
```python
from biodigest import setup
setup.main(setup_type="api")
```
### 2. Create data from scratch
Any mappings are freshly fetched from the databases and the distance matrices are calculated. Be aware that this can take up to 3 hours. 
```python
from biodigest import setup
setup.main(setup_type="create")
```

## Run validation
```python
from biodigest.single_validation import single_validation
results = single_validation(tar: Union[pd.DataFrame, set], tar_id: str, mode: str, distance: str = "jaccard",
                            ref: Union[str, set] = None, ref_id: str = None, enriched: bool = False,
                            mapper: Mapper = FileMapper(), runs: int = config.NUMBER_OF_RANDOM_RUNS,
                            background_model: str = "complete", replace=100, verbose: bool = False)
```
All results that can later be saved and visualize are saved in `results` as data type `dict()`.
### Parameters
#### Required parameters
- **tar**: Target input you want to be validated
  - a cluster should be of type `pd.DataFrame()` with `columns=["id","cluster"]`
  - a set should be of type `set()`
- **tar_id**: Is the id type of the target (see possible options below)
- **ref**: Reference, to which **tar** will be compared (Only for mode id-set and set-set) 
  - a single id should be of type `str`
  - a set should be of type `set()`
- **ref_id**: Is the id type of the reference (see possible options below)
- **mode**: Desired mode. See possible options below.
#### Optional parameters
- **distance**: Distance measure used for pairwise comparison
- **enriched**: Set `True`, if only enriched attributes of the reference set should be used (Only for set-set)
- **background_model**: Model defining how random values should be picked. See possible options below.
- **runs**: Number of runs with random target values for p-value calculation
- **replace**: Percentage of how many of the original ids should be replaced with random ids
- **verbose**: get additional information during the run
#### Supported types
- **gene types**: entrez, ensembl, symbol, uniprot
- **disease types**: mondo, omim, snomedct, umls, orpha, mesh, doid, ICD-10
#### Modes
- **set**: Compare similarity inside the set using the mean of all pairwise comparisons
- **id-set**: Compare target set to reference set
- **set-set** Compare target set to reference id
- **cluster** Compare cluster quality inside clustering using multiple quality measures (Dunn index, Davied Bouldin Index, Sillhouette Score)
#### Background models
- **complete**: Random ids will be picked completely randomly
- **term-pres**: Random ids will preserve the number of mapped terms for the replaced ids
### Result
The method call returns the result in a json format of datatype dict which consists of 
the following elements:
```python
result = {'status': 'Status text',
          'input_values': {'values': dict(), 'mapped_ids': list()}, 
          'p_values': {'values': dict()}}
```
- **status**: contains either an error message if a mapping failed or "ok" if IDs could be mapped
- **input_values**:
  - **values**: table in dict format with the functional or genetic relevance score(s) determined for solely their input
  - **mapped_ids**: list containing the IDs with non empty annotations per functional or genetic annotation type
  
- **p_values**: table in dict format with the calculated empirical P-values using the selected background model and other parameters that indicate the significance of the calculated relevance scores derived from the input
## Save and visualize results
```python
from biodigest.single_validation import save_results
from biodigest.evaluation.d_utils.plotting_utils import create_plots

# Save results into json file and 2 .csv table files
save_results(results: dict, prefix: str, out_dir)

# Generate at save plots based on results
create_plots(results, mode, tar, tar_id, out_dir, prefix, file_type: str = "pdf")
```
### Parameters
#### Required parameters
- **results**: Is the output created with method `single_validation` as data type `dict()`
- **prefix**: Prefix for file names
- **out_dir**: Output directory for the generated files
#### Additional required parameters for create_plots
- **tar**: Target input you want to be validated
  - a cluster should be of type `pd.DataFrame()` with `columns=["id","cluster"]`
  - a set should be of type `set()`
- **tar_id**: Is the id type of the target (see possible options above)
#### Optional parameters for create_plots
- **file_type**: Type of the plots image files.
## Example runs
Check out the [tutorial](https://github.com/bionetslab/digest-tutorial) to see examples of usage in a script.
