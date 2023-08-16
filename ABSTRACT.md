Rivers as vehicles for plastic transport remain understudied in the context of global plastic pollution emissions. The Plastic Bottles dataset is dedicated to present a prototype of a model that can detect plastic objects in rivers which can be used on resource-constrained devices without internet connection.

Estimates on how much plastic is emitted by a river mainly rely on mathematical models that consider the size of cities near the river, their development level and more. This is not very granular, as only a monthly estimate for the output of a whole river or city is given. This makes the data often not very actionable insight, because the most polluting rivers tend to also be very long, which makes it hard to know where to start exactly. The data is also statistically infered, not measured in the real world and reflects what we think is realistic not what actually is.

The instructions for the photographers were:

* Always point the camera in a 90-degree angle relative to the river
* Try to photograph a little bit from above
* Do not use the zoom of their camera
* Take a lot of pictures in different places (at least 50x pictures in each place, wait at least 5 seconds between two pictures).
* In general, don't wait for the perfectshot, but take many (hundreds).
* Try to make pictures at different times in the same location (e.g.: after sunset,around noon, afternoon etc.)

During the data gathering, the photographers were given examples of good and bad images from the pool they sent in and edge cases were discussed. The data gathering / picture taking process took roughly two months of work. Pictures were mostly taken from the side of a river. This means, for example, that the dataset maybe less suitable for e.g. aerial surveillance.

No images were taken during nighttime or during bad weather conditions. While some variance of the time of day naturally occurred, all images were taken during daylight. Camera zoom was intentionally not used in order to cover a large variety of dis-tances. This means, that are a significant number of images where the plastic bottle is very far away and may only be visible upon a close look and/or using zoom. Author of the dataset hopes to increase the odds that a machine learning system can detect these as well, enabling surveillance of larger rivers. He estimates the bottles farthest away in the dataset have a distance of about 50-60 meters to the camera. At this point, even with zoom, a human has problems classifying the object in the picture – it is still clearly distinct from the water surface, but not easily separable e.g. from a bird. The variety of their dataset means there is also a lot of variance in the number of bottles represented in an image.

There are images with bottles swimming freely as well as bottles that are relatively stationary. All bottles are photographed either on river water or on other pollution objects, including more bottles. No bottles have been photographed on land. The images were taken with different devices, both mobile phones and cameras. Due to this, the images generally have different resolutions. No tripod has been used for any pictures and the height from which the pictures were taken may variate slightly as well as the angle of the camera.	

| Attribute               | Value                                                        |
| :---------------------- | :----------------------------------------------------------- |
| Total images:           | 989 (some dublicate images were removed)                     |
| Avg. bottles per image: | 5.6                                                          |
| Image format            | JPG                                                          |
| Total image file size:  | 2.6 GB                                                       |
| Photographed in:        | 34 Sessions                                                  |
| Countries of rivers:    | Bangladesh, Bosnia, India, Indonesia, Nepal, Pakistan, Sudan |
| Camera perspective:     | Side of river (mostly)                                       |
| Labeling format:        | Pascal                                                       |
| License:                | Public Domain                                                |
