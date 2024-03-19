# Autonomous-Vehicle-2021
This repostiry is dedicated to study the following: 
- A brief study of CNNs
- Image Detection using YOLO-V5

![3-1024x630-1024x630](https://github.com/ArthasMenethil-A/Ghazal-Self-Driving-Car/assets/69509720/7c0e8572-2afd-472a-a1e6-e665990b3c47)

Overview: 
- Driver Monitoring
  - Introduction
  - Yolo-V5
    - Convolutional Neural Networks (CNNs)
    - Yolo-V5 Setup
    - Yolo-V5 Training
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

**Step 2: Install Pytorch and Cuda**

First go to the [Pytorch Local Installation](https://pytorch.org/get-started/locally/) address. In the following section choose the appropriate installation version for your computer. Copy the output command and run it in your Virtual Env 

![Untitled-2](https://github.com/ArthasMenethil-A/Ghazal-Self-Driving-Car/assets/69509720/287fd88c-3a69-469b-932d-893bcaec10c9)

NOTE: If you choose the GPU-activated version with Cuda, you have to have the currect version of Cuda installed on your pc. Google Cuda version 11.8 (or your version) and open the first link which takes you to a page similar to this [CUDA Download Page](https://developer.nvidia.com/cuda-11-8-0-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exe_local)

**Step 3: Use Default Model**

The following jupyter notebook contains the code necessary for Using Yolo-V5 for a given image.

[Yolo-V5 Default Model Jupyter Notebook](https://github.com/ArthasMenethil-A/Ghazal-Self-Driving-Car/blob/main/Python/yolov5.ipynb)

![1](https://github.com/ArthasMenethil-A/Ghazal-Self-Driving-Car/assets/69509720/e11981fa-c82e-41a2-82fc-f31c191b4ceb)

#### Yolo-V5 Training
------

**WHAT IS TRANSFER LEARNING**

This approach involves leveraging the knowledge gained from pre-trained models to enhance the performance of new tasks. In the context of object detection for driver monitoring, transfer learning offers a practical solution to efficiently train accurate models. The process begins with a pre-trained model, such as Yolo-V5, which has already learned to recognize a wide range of objects in images. Instead of starting from scratch, this model's learned features and representations are repurposed for the specific task of detecting driver behaviors like eating, drinking, speaking on the phone, and more. This is particularly valuable as it reduces the need for massive amounts of labeled training data, which can be resource-intensive to collect and annotate.

In the Ghazal-Self-Driving-Car project, transfer learning is employed to fine-tune the Yolo-V5 model for the task of driver behavior detection. The initial training on a broad dataset allows the model to grasp fundamental visual patterns and features present in various objects. Then, during the fine-tuning stage, the model is trained on a smaller dataset containing specific driver behavior examples. This process helps the model specialize in identifying the behaviors relevant to driver monitoring. So basically, all of the model's layerz are frozen for the fine-tuning, excpet the last ReLU layer that is for final classification. 

**Step 1: Labeling Training Data**

Using a [Google Image Web-Scarper]() or something similar, you can gather your data. Upon gathering the images, you have to label each of them using a Label Image Application which can be installed using the following command:
```
git clone https://github.com/tzutalin/labelImg
```

you run the following commands for running the labelImg.py script and opening the application.
```
pip install pyqt5 lxml --upgrade
cd labelImg && pyrcc5 -o libs/resources.py resources.qrc
cd labelImg && python labelImg.py
```

NOTE: it is advisable that you run these commands in CMD rather than Jupyter Notebook.

**Step 2: Changing 'dataset.yml' File**

After labeling the dataset and saving the labels the direction (plus the important file locations) should look something like this: 
```
root 
    |
    yolov5
    |     |
    |     dataset.yml
    |
    labelImg
    |       |
    |       labelImg.py
    |
    data
        |
        images
        |
        labels
```

in dataset.yml file the overall structure should be something like the following: 

```
path: ../data  
train: images  
val: images  
test:  

names:
  0: normal
  1: drowsy
  2: speaking 
  3: eating
  4: drinking
```

**Step 3: Training**

run the following command to train data.
```
cd yolov5 && python train.py --img 320 --batch 4 --epochs 150 --data dataset.yml --weights yolov5s.pt --workers 1
```

**Step 4: Testing**

run the following command to load custom model in Jupyter Notebook
```
model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp12/weights/last.pt', force_reload=True)
```

![68747470733a2f2f692e6962622e636f2f5a4c38645735532f64657465637465642d706963747572652e6a7067 jpg](https://github.com/ArthasMenethil-A/Ghazal-Self-Driving-Car/assets/69509720/442950dd-1c30-4885-b6ad-3d5d53aa7f08)

**Finally**

The said method is from Nicholas Renotte YouTube Channel (Reference [2])

All of the code needed is included in the

[Yolo-V5 Training Jupyter Notebook](https://github.com/ArthasMenethil-A/Ghazal-Self-Driving-Car/blob/main/Python/yolov5_finetuning.ipynb)

### Dataset Preparation
------
For gathering data we'll use Google Image and a python script for web-scraping. The Python script is linked below: 

[Python Web-Scraper](https://github.com/ArthasMenethil-A/Ghazal-Self-Driving-Car/tree/main/Research/Dataset)


### Results
------



## References
------

[1] [Code Basics Tutorial](https://www.youtube.com/watch?v=ag3DLKsl2vk&ab_channel=codebasics)

[2] [Nicholas Renotte Tutorial](https://www.youtube.com/watch?v=tFNJGim3FXw&t=873s&ab_channel=NicholasRenotte) 

[3] [YOLOv5 - medium article](https://medium.com/axinc-ai/yolov5-the-latest-model-for-object-detection-b13320ec516b)

[4] [Yolo Main Repository](https://github.com/ultralytics/yolov5)
