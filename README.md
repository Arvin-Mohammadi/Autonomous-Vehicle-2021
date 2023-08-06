![image](https://github.com/ArthasMenethil-A/Ghazal-Self-Driving-Car/assets/69509720/36190454-61dc-43d9-861f-5d26dd98032b)# Ghazal-Self-Driving-Car
------
Welcome to the Ghazal-Self-Driving-Car repository! This repository stores the progress of the PSG Team on developing self-driving car technologies.

![3-1024x630-1024x630](https://github.com/ArthasMenethil-A/Ghazal-Self-Driving-Car/assets/69509720/7c0e8572-2afd-472a-a1e6-e665990b3c47)

Overview: 
- Introduction
- Yolo-V5
  - Convolutional Neural Networks (CNNs)
  - Yolo-V5 Theory
- Setup and Installation
- Dataset Preparation
- Results 


## DRIVER MONITORING
------
Driver monitoring plays a critical role in ensuring the safety and optimizing the performance of self-driving cars. These systems leverage a variety of sensors and technologies to track the driver's behavior and detect signs of distraction or impairment. In complex driving situations or emergencies, the system smoothly transitions control back to the human driver. Additionally, driver monitoring facilitates data-driven improvements in autonomous driving algorithms by learning from the driver's interactions and preferences. This essential safety feature continuously supports the development and validation of self-driving technology, providing a safer and more efficient driving experience.

### Introduction
------
Our approach to this challenge involves utilizing Object Detection with Yolo Ultralytics (Yolo-V5). During driving, individuals commonly engage in dangerous activities such as:

* Eating/Drinking
* Drowsy Driving
* Using a Phone
  * Texting
  * Speaking
* Driving Under Influence (Alcohol, Drugs, etc)
* Distracted Driving

With Object Detection, we can accurately identify whether the driver is eating/drinking, drowsy, or speaking on the phone. However, for the other activities (Texting, Driving under the influence of drugs, Distracted Driving), Yolo-V5 or object detection, in general, may not be the most suitable approach. Let's proceed step by step. The first model we need to implement is Yolo-V5, using "Transfer Learning" to detect five classes for us:

* `normal`: Driver at normal state of driving
* `drowsy`: Driver at drowsy state while driving
* `speaking`: Driver speaking on the phone while driving 
* `eating`: Driver eating while driving
* `drinking`: Driver drinking while driving


![Untitled-1](https://github.com/ArthasMenethil-A/Ghazal-Self-Driving-Car/assets/69509720/47b1a1e0-2eaa-4fc9-a8de-ed31a7fa96b9)


By focusing on these classes, we can effectively monitor and enhance the safety of the driving experience.



### Yolo-V5
------
Yolo-V5 is an object detection model developed by ultralytics which was released in June 2020. Yolo-V5 has four main models and each of those four model will give different levels of performance. [3]


![image](https://github.com/ArthasMenethil-A/Ghazal-Self-Driving-Car/assets/69509720/d53c3d78-927c-4785-8635-51f5950217ce)
[Source: https://github.com/ultralytics/yolov5]

The output of Yolo contains three things [1]: 
1. Is object detected or not (Boolian)
2. The class of the detected object
3. The position of the detected object

### Convolutional Neural Networks 
CNN is a complex topic, and I've had trouble understanding it myself. So, let's try to make it clearer with an example. Imagine I have a picture of a Lamborghini that I want to detect using artificial intelligence. This special car has unique "features" like the shape of the headlamps, the doors, or the rear spoiler.

![image](https://github.com/ArthasMenethil-A/Ghazal-Self-Driving-Car/assets/69509720/e67ebe39-840b-4e65-85ae-e9a594c5653a)

CNN's main function is to learn these unknown features and search for them within the picture. These features can be represented as [features_1, feature_2, ..., feature_k]. For each value of "i" between 1 and k, CNN will take feature_i and search for that specific feature in the picture. In our Lamborghini example, if CNN considers the "shape of the mirror" as an interesting feature, it will scan the picture to find that specific feature. When the mirror is found, CNN will think, "huh, maybe this is a Lamborghini."


Now, let's delve into the mathematical representation of these features. In the basic application of CNN on RGB images, the images have three color channels: Red, Blue, and Green. In mathematical form, each of these channels is represented as matrices with numbers between 0 and 255 (before normalization). The features are also represented as matrices, but they are smaller in size.

[Source: https://e2eml.school/convert_rgb_to_grayscale.html]

These features can be visualized as filters that slide over the picture. When a filter encounters a shape similar to our feature, it becomes "activated" or in simpler terms, it says, "hey, found your mirror." Since we have "k" features, we end up with "k" output channels.


In summary, CNN learns interesting features to identify an object. It then searches for these features in a given picture. When enough features are detected in the picture, CNN concludes that the desired object is present. Of course, there's much more to CNN, but I won't go into further detail as that's not the intention of this article. Let's move on to the next topic.




## References
------

[1] [Code Basics Tutorial](https://www.youtube.com/watch?v=ag3DLKsl2vk&ab_channel=codebasics)
[2] [Nicholas Renotte Tutorial](https://www.youtube.com/watch?v=tFNJGim3FXw&t=873s&ab_channel=NicholasRenotte) 
[3] [YOLOv5 - medium article](https://medium.com/axinc-ai/yolov5-the-latest-model-for-object-detection-b13320ec516b)
[4] [Yolo Main Repository](https://github.com/ultralytics/yolov5)
