# https://github.com/m0-n/Plastic-Bottles-Dataset

import glob
import os
import xml.etree.ElementTree as ET

import cv2
import numpy as np
import supervisely as sly
from dotenv import load_dotenv
from supervisely.io.fs import (
    dir_exists,
    file_exists,
    get_file_ext,
    get_file_name,
    get_file_name_with_ext,
    get_file_size,
    mkdir,
    remove_dir,
)

# # if sly.is_development():
# load_dotenv("local.env")
# load_dotenv(os.path.expanduser("~/supervisely.env"))

# api = sly.Api.from_env()
# team_id = sly.env.team_id()
# workspace_id = sly.env.workspace_id()

# project_name = "Plastic-Bottles"
dataset_path = "APP_DATA/Plastic-Bottles-Dataset"
batch_size = 30
ds_name = "ds"
images_ext = ".jpg"
ann_ext = ".xml"

tag_names = [
    "Indonesia",
    "India",
    "Nepal",
    "Pakistan",
    "Sudan",
    "Bosnia",
    "Bangladesh",
]
id2country = {
    "001": "Indonesia",
    "002": "Indonesia",
    "003": "India",
    "004": "Nepal",
    "005": "Nepal",
    "006": "Pakistan",
    "007": "Pakistan",
    "008": "Nepal",
    "009": "Sudan",
    "010": "Pakistan",
    "011": "Bosnia",
    "012": "Bosnia",
    "013": "Pakistan",
    "014": "Pakistan",
    "015": "Pakistan",
    "016": "India",
    "017": "Nepal",
    "018": "Bangladesh",
    "019": "Bosnia",
    "020": "Bosnia",
    "021": "Pakistan",
    "022": "Pakistan",
    "023": "India",
    "024": "Nepal",
    "025": "Nepal",
    "026": "Nepal",
    "027": "Nepal",
    "028": "Nepal",
    "029": "Nepal",
    "030": "Bosnia",
    "031": "Bangladesh",
    "032": "Bangladesh",
    "033": "Bangladesh",
    "034": "Pakistan",
}
tag_metas = [sly.TagMeta(name, sly.TagValueType.NONE) for name in tag_names]


def create_ann(image_path):
    labels = []

    image_np = sly.imaging.image.read(image_path)[:, :, 0]
    img_height = image_np.shape[0]
    img_wight = image_np.shape[1]

    file_name = get_file_name(image_path)

    ann_path = os.path.join(dataset_path, file_name + ann_ext)

    if file_exists(ann_path):
        tree = ET.parse(ann_path)
        root = tree.getroot()

        coords_xml = root.findall(".//bndbox")
        for curr_coord in coords_xml:
            left = int(curr_coord[0].text)
            top = int(curr_coord[1].text)
            right = int(curr_coord[2].text)
            bottom = int(curr_coord[3].text)

            rect = sly.Rectangle(left=left, top=top, right=right, bottom=bottom)
            label = sly.Label(rect, obj_class)
            labels.append(label)

    id_ = os.path.basename(os.path.dirname(image_path))

    tags = [sly.Tag(tag_meta) for tag_meta in tag_metas if tag_meta.name == id2country[id_]]
    return sly.Annotation(img_size=(img_height, img_wight), labels=labels, img_tags=tags)


obj_class = sly.ObjClass("plastic bottle", sly.Rectangle)


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    dataset_path = "APP_DATA/Plastic-Bottles-Dataset"
    batch_size = 30
    ds_name = "ds"
    images_ext = ".jpg"
    ann_ext = ".xml"

    tag_names = [
        "Indonesia",
        "India",
        "Nepal",
        "Pakistan",
        "Sudan",
        "Bosnia",
        "Bangladesh",
    ]
    id2country = {
        "001": "Indonesia",
        "002": "Indonesia",
        "003": "India",
        "004": "Nepal",
        "005": "Nepal",
        "006": "Pakistan",
        "007": "Pakistan",
        "008": "Nepal",
        "009": "Sudan",
        "010": "Pakistan",
        "011": "Bosnia",
        "012": "Bosnia",
        "013": "Pakistan",
        "014": "Pakistan",
        "015": "Pakistan",
        "016": "India",
        "017": "Nepal",
        "018": "Bangladesh",
        "019": "Bosnia",
        "020": "Bosnia",
        "021": "Pakistan",
        "022": "Pakistan",
        "023": "India",
        "024": "Nepal",
        "025": "Nepal",
        "026": "Nepal",
        "027": "Nepal",
        "028": "Nepal",
        "029": "Nepal",
        "030": "Bosnia",
        "031": "Bangladesh",
        "032": "Bangladesh",
        "033": "Bangladesh",
        "034": "Pakistan",
    }
    tag_metas = [sly.TagMeta(name, sly.TagValueType.NONE) for name in tag_names]

    def create_ann(image_path):
        labels = []

        image_np = sly.imaging.image.read(image_path)[:, :, 0]
        img_height = image_np.shape[0]
        img_wight = image_np.shape[1]

        file_name = get_file_name(image_path)

        folder_name = os.path.basename(os.path.dirname(image_path))

        # tmppath = os.path.join(dataset_path, '')

        ann_path = os.path.join(dataset_path, folder_name, file_name + ann_ext)

        if file_exists(ann_path):
            tree = ET.parse(ann_path)
            root = tree.getroot()

            coords_xml = root.findall(".//bndbox")
            for curr_coord in coords_xml:
                left = int(curr_coord[0].text)
                top = int(curr_coord[1].text)
                right = int(curr_coord[2].text)
                bottom = int(curr_coord[3].text)

                rect = sly.Rectangle(left=left, top=top, right=right, bottom=bottom)
                label = sly.Label(rect, obj_class)
                labels.append(label)

        id_ = os.path.basename(os.path.dirname(image_path)).split("-")[0]

        tags = [sly.Tag(tag_meta) for tag_meta in tag_metas if tag_meta.name == id2country[id_]]
        return sly.Annotation(img_size=(img_height, img_wight), labels=labels, img_tags=tags)

    obj_class = sly.ObjClass("plastic bottle", sly.Rectangle)
    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=[obj_class], tag_metas=tag_metas)
    api.project.update_meta(project.id, meta.to_json())

    # for ds_name in os.listdir(dataset_path):
    #     ds_path = os.path.join(dataset_path, ds_name)
    #     if dir_exists(ds_path):

    def get_file_names(directory):
        arr = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                arr.append(os.path.join(root, file))
        return arr

    def remove_duplicates(paths):
        filenames = {}
        unique_paths = []

        for path in paths:
            # Get the filename from the path
            filename = os.path.basename(path)

            # If the filename is not in the dictionary, add it
            if filename not in filenames:
                filenames[filename] = True
                unique_paths.append(path)

        return unique_paths

    images_names = [
        im_name for im_name in get_file_names(dataset_path) if get_file_ext(im_name) == images_ext
    ]

    images_names = remove_duplicates(images_names)

    dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

    progress = sly.Progress("Create dataset {}".format(ds_name), len(images_names))

    for img_pathes_batch in sly.batched(images_names, batch_size=batch_size):
        # img_pathes_batch = [
        #     os.path.join(dataset_path, image_name) for image_name in images_names_batch
        # ]
        # TODO =========================== must have, check EXIF Rotate 180 =========================
        temp_img_pathes_batch = []
        temp_folder = os.path.join("APP_DATA", "temp")
        os.makedirs(temp_folder, exist_ok=True)
        for im_path in img_pathes_batch:
            temp_img = cv2.imread(
                im_path,
                flags=cv2.IMREAD_ANYCOLOR | cv2.IMREAD_ANYDEPTH | cv2.IMREAD_IGNORE_ORIENTATION,
            )
            foldername = os.path.basename(os.path.dirname(im_path))
            new_img_path = os.path.join(
                temp_folder,
                foldername,
                get_file_name_with_ext(im_path),
            )
            os.makedirs(os.path.join(temp_folder, foldername), exist_ok=True)
            temp_img_pathes_batch.append(new_img_path)
            cv2.imwrite(new_img_path, temp_img)

        # TODO =======================================================================================
        img_names_batch = [get_file_name_with_ext(path) for path in img_pathes_batch]
        img_infos = api.image.upload_paths(dataset.id, img_names_batch, temp_img_pathes_batch)
        img_ids = [im_info.id for im_info in img_infos]

        anns = [create_ann(image_path) for image_path in temp_img_pathes_batch]

        remove_dir(temp_folder)
        api.annotation.upload_anns(img_ids, anns)

        progress.iters_done_report(len(img_pathes_batch))

    return project
