Dataset **Plastic Bottles** can be downloaded in Supervisely format:

 [Download](https://assets.supervise.ly/supervisely-supervisely-assets-public/teams_storage/4/h/TD/EXhjZDolSHCMOZOOWwT3Llx5YO4BRBwiCJlQSkcfCCewB7t14a6JkTURmfQXGJB07KvJ0v0Pve9jbSETMOcytHkBg7KpLbM2J5KOPr7V4QDHNDWZlssE4Z9IVPdH.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Plastic Bottles', dst_path='~/dtools/datasets/Plastic Bottles.tar')
```
The data in original format can be 🔗[downloaded here](https://github.com/m0-n/Plastic-Bottles-Dataset/archive/master.zip)