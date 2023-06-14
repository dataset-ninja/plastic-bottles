# Path to the original dataset
import os
import xml.etree.ElementTree as ET

import supervisely as sly
from supervisely.io.fs import get_file_name


def create_ann(image_path, ann_dir, obj_class):
    labels = []

    image_np = sly.imaging.image.read(image_path)[:, :, 0]
    img_height = image_np.shape[0]
    img_wight = image_np.shape[1]

    file_name = get_file_name(image_path)

    ann_path = os.path.join(ann_dir, file_name + ".xml")

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

    return sly.Annotation(img_size=(img_height, img_wight), labels=labels)


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    dataset_path = "../datasets-bot/datasets/plastic-bottles"
    ds_name = "ds0"
    imd_dir = "images"
    ann_dir = "annotations"

    # Function should read local dataset and upload it to Supervisely project, then return project info.
    obj_class = sly.ObjClass("Plastic Bottle", sly.Rectangle)
    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=[obj_class])
    api.project.update_meta(project.id, meta.to_json())

    dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

    images_path = os.path.join(dataset_path, imd_dir)
    ann_path = os.path.join(dataset_path, ann_dir)
    images_names = os.listdir(images_path)

    progress = sly.Progress(f"Process dataset {ds_name}", len(images_names))

    for images_names_batch in sly.batched(images_names):
        img_pathes_batch = [
            os.path.join(images_path, image_name) for image_name in images_names_batch
        ]

        img_infos = api.image.upload_paths(dataset.id, images_names_batch, img_pathes_batch)
        img_ids = [im_info.id for im_info in img_infos]

        anns = [create_ann(image_path, ann_path, obj_class) for image_path in img_pathes_batch]
        api.annotation.upload_anns(img_ids, anns)

        progress.iters_done_report(len(images_names_batch))

    return project
