# Ghazal-Self-Driving-Car
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
