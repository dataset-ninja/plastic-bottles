Dataset **Plastic Bottles** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/4/1/Mq/FODOCuecb30E19cmthOrbbkMqzLRueckAdPq8EU1xTCm5BqxLgsNsL6sgmBgNMya8uOBypQBxbDRyXwawIX5unZr53kLfGzWpyAA3edBDckQfMvtUVCruc3Dt920.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Plastic Bottles', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://github.com/m0-n/Plastic-Bottles-Dataset/archive/master.zip).