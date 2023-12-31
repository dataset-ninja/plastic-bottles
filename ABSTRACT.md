The **Plastic Bottles** dataset is designed to introduce a model prototype for identifying plastic objects in rivers. Importantly, this model is optimized for deployment on resource-constrained devices that operate without an internet connection. The authors mention that the role of rivers in transporting plastic waste, a crucial aspect of global plastic pollution, has not received sufficient attention in research. 

Current estimates of plastic emissions from rivers primarily rely on mathematical models that take into account factors like the size and development level of cities located near the river. However, these estimates lack granularity, offering only a monthly assessment for entire rivers or cities. This limited granularity often leads to a lack of actionable insights because the most environmentally harmful rivers are frequently lengthy, making it challenging to pinpoint precise intervention areas. Additionally, this data is often statistically inferred rather than directly measured in the real world, representing what is assumed to be realistic rather than what truly exists.

The instructions for the photographers were:

* Always point the camera at a 90-degree angle relative to the river
* Try to photograph a little bit from above
* Do not use the zoom of their camera
* Take a lot of pictures in different places (at least 50x pictures in each place, wait at least 5 seconds between two pictures).
* In general, don't wait for the perfect shot, but take many (hundreds).
* Try to take pictures at different times in the same location (e.g.: after sunset, around noon, afternoon etc.)

During the data gathering, the photographers were given examples of good and bad images from the pool they sent in and edge cases were discussed. The data-gathering / picture-taking process took roughly two months of work. Pictures were mostly taken from the side of a river. This means, for example, that the dataset may be less suitable for e.g. aerial surveillance.

No images were taken during nighttime or during bad weather conditions. While some variance in the time of day naturally occurred, all images were taken during daylight. Camera zoom was intentionally not used in order to cover a large variety of distances. This means, that there are a significant number of images where the plastic bottle is very far away and may only be visible upon a close look and/or using zoom. The author of the dataset hopes to increase the odds that a machine learning system can detect these as well, enabling surveillance of larger rivers. He estimates the bottles farthest away in the dataset have a distance of about 50-60 meters from the camera. At this point, even with zoom, a human has problems classifying the object in the picture – it is still clearly distinct from the water surface, but not easily separable e.g. from a bird. The variety of their dataset means there is also a lot of variance in the number of bottles represented in an image.

There are images of bottles swimming freely as well as bottles that are relatively stationary. All bottles are photographed either on river water or on other pollution objects, including more bottles. No bottles have been photographed on land. The images were taken with different devices, both mobile phones and cameras. Due to this, the images generally have different resolutions. No tripod has been used for any pictures and the height from which the pictures were taken may vary slightly as well as the angle of the camera.	

| Attribute               | Value                                                        |
| :---------------------- | :----------------------------------------------------------- |
| Total images:           | 989 (some duplicate images were removed)                     |
| Avg. bottles per image: | 5.6                                                          |
| Image format            | JPG                                                          |
| Total image file size:  | 2.6 GB                                                       |
| Photographed in:        | 34 Sessions                                                  |
| Countries of rivers:    | Bangladesh, Bosnia, India, Indonesia, Nepal, Pakistan, Sudan |
| Camera perspective:     | Side of the river (mostly)                                       |
| Labeling format:        | Pascal                                                       |
| License:                | Public Domain                                                |
