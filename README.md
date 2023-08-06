# Ghazal-Self-Driving-Car
------
Welcome to the Ghazal-Self-Driving-Car repository! This repository stores the progress of the PSG Team on developing self-driving car technologies.

![3-1024x630-1024x630](https://github.com/ArthasMenethil-A/Ghazal-Self-Driving-Car/assets/69509720/7c0e8572-2afd-472a-a1e6-e665990b3c47)

Overview: 
- Introduction
- Yolo-V5
  - Convolutional Neural Networks (CNNs)
  - Yolo-V5 Setup
  - Yolo-V5 Training
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

The output of Yolo contains three things [1]: 
1. Is object detected or not (Boolian)
2. The class of the detected object
3. The position of the detected object

#### Convolutional Neural Networks 
------

Convolutional Neural Networks (CNN) can be quite challenging to understand, as I myself had struggled with it in the past. However, providing and example can help us understand the intuition behind CNNs. Assuming we have a picture of a given object (in this case a car), we want to detect using artificial intelligence. This object has some unique "features," such as the shape of the headlamps, the doors, or the edges of the rear spoiler.

![Untitled-2](https://github.com/ArthasMenethil-A/Ghazal-Self-Driving-Car/assets/69509720/eca56bd0-102d-4ebf-af4b-1100aac3a894)

What CNN does is essentially learn these unknown features and searches for them inside the picture. The features are represented as [feature_1, feature_2, ..., feature_k]. For each value of "i" between 1 and k, CNN takes feature_i and looks for that specific feature within the picture. In the case of our car example, if CNN recognizes the "shape of the mirror" as an interesting feature during training, it will search for that specific feature in the image during prediction. If CNN finds that feature (mirror), it will identify the object it is attached to as a car.

For further information about CNN, you can refer to this [Medium Article](https://towardsdev.com/lenet-5-theory-cnn-gd-sgd-dropout-maxpool-lenet-5-ba7863360bdd)

#### Yolo-V5 Setup
------

**Step 1: Virtual Environment**

The first step is to make a virtual Environment, you can find details of making a virtual environemnt using Python in the following link:

[HOW TO MAKE A VIRTUAL ENV](https://github.com/ArthasMenethil-A/Ghazal-Self-Driving-Car/blob/main/Research/Yolo%20Setup/Virtual%20Env/README.md)

## References
------

[1] [Code Basics Tutorial](https://www.youtube.com/watch?v=ag3DLKsl2vk&ab_channel=codebasics)

[2] [Nicholas Renotte Tutorial](https://www.youtube.com/watch?v=tFNJGim3FXw&t=873s&ab_channel=NicholasRenotte) 

[3] [YOLOv5 - medium article](https://medium.com/axinc-ai/yolov5-the-latest-model-for-object-detection-b13320ec516b)

[4] [Yolo Main Repository](https://github.com/ultralytics/yolov5)
