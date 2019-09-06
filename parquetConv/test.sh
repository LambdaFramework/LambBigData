#!/bin/bash

fr="/Users/shoh/Projects/CMS/PhD/Analysis/SSL/dataset-v12-VH/TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1-v1.root"

python parquetConverter.py -i ${fr} -o Prodv1
