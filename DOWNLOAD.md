Dataset **Plastic Bottles** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogImZzOi8vYXNzZXRzLzE1NDdfUGxhc3RpYyBCb3R0bGVzL3BsYXN0aWMtYm90dGxlcy1EYXRhc2V0TmluamEudGFyIiwgInNpZyI6ICI2UjVDY0g5Z0tFYy9jYWR6dVJmTUxWVDh1TEtwZGM3SlEzR0pNQnFGRUFzPSJ9)

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