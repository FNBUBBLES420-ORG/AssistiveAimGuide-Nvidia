# 🎯 Assistive AimGuide Configuration GUI

A sleek, user-friendly configuration tool built with `Tkinter` for customizing and launching the Assistive AimGuide, designed to help disabled gamers and streamers optimize their aim-assist tool powered by AI models. Perfect for users with physical or cognitive challenges who need support while gaming.

> 💙 Built with accessibility in mind by the FNBUBBLES420 Organization.

---

## 📦 Features

- Dynamic GUI to update and reload configurations
- Visual toggles for features like masking, visuals, and headshot targeting
- Easy switching between ONNX and TensorRT model types
- Live launching of the assistive detection tool
- Full support for `CUDA` and device targeting

---

## 🐍 Install Python 3.11.9 Without Admin Access (Super Easy!)

1. In the extracted folder, **look for** the file:  

```
python3119.bat
```

2. **Double-click** this `.bat` file.
3. It will automatically:
- Download Python 3.11.9
- Install it locally (no admin required)
- Add it to your PATH
- Close when complete

> 💡 Now you’re ready to install packages and run the app — without needing admin access!

## 🛠️ Requirements

Ensure you have the following installed before running the GUI:

```bash
pip install -r requirements.txt
```

### **Sample dependencies include**:

- `torch`, `torchvision`, `torchaudio`

- `onnx`, `onnxruntime`, `cupy`, `pyautogui`, `pywin32`

- `tkinter` (usually comes with Python)

Your model placed in `pt_models/` (without extension, either `.engine` or `.onnx`)

## 🚀 How to Run the GUI

Make sure you're in the project root directory. Then, launch the GUI with:

```
python gui.py
```
- Use the `launcher.bat` to run the application.
- If you get a error stating model cant be found via common.py
- Move your `.engine` or `.onnx` model to `pt_models/` folder then run application again no need to close app.
- Click `run app`

## 🧠 How It Works

- Modify detection and model settings in the GUI.

- Press 💾 Update Config to save changes.

- Press 🚀 Run App to launch the AI detection engine in the background.

- Use 🔁 Reload Config to reset the GUI to match the saved JSON configuration.

- Close safely with ❌ Close App.

---

## 📂 Default Configuration File

Configuration is stored in `user_config.json`. The GUI reads and writes to this file automatically using `get_config()` and `set_config()` from `config.py`.

Example config:

```json
{
    "screenShotHeight": 320,
    "screenShotWidth": 320,
    "useMask": true,
    "maskSide": "left",
    "maskWidth": 80,
    "maskHeight": 200,
    "aaMovementAmp": 0.4,
    "confidence": 0.4,
    "aaQuitKey": "Q",
    "headshot_mode": true,
    "cpsDisplay": true,
    "visuals": false,
    "centerOfScreen": true,
    "model_path": "pt_models/v5",
    "model_type": "onnx",
    "enable_cuda": true,
    "device_type": "cuda",
    "Close App": false
}
```
---

## 📢 Notes

- Ensure your model file (ONNX or TensorRT) exists at the given path.

- You can switch between model types (`onnx`, `engine`) directly from the GUI.

- All runtime config changes are persisted in `user_config.json`.


---
# 🙌 Made With ❤️ by Bubbles The Dev & FNBubbles420 Org
### This app is part of the mission of [FNBUBBLES420 ORG](https://fnbubbles420.org) – helping gamers with disabilities break limits and play freely.

### 💌 Questions or Support?
- Join our Discord community.
- [Click To Join Discord](https://discord.fnbubbles420.org/invite)
---



# 🚀 NVIDIA CUDA Installation Guide
---

## DO `EVERY STEP AND FOLLOW EVERY STEP` OF THE NVIDIA INSTALLATION GUIDE OR IT WON'T WORK PROPERLY

---
### 1. **Download the NVIDIA CUDA Toolkit 11.8**

First, download the CUDA Toolkit 11.8 from the official NVIDIA website:

👉 [Nvidia CUDA Toolkit 11.8 - DOWNLOAD HERE](https://developer.nvidia.com/cuda-11-8-0-download-archive)

### 2. **Install the CUDA Toolkit**

- After downloading, open the installer (`.exe`) and follow the instructions provided by the installer.
- Make sure to select the following components during installation:
  - CUDA Toolkit
  - CUDA Samples
  - CUDA Documentation (optional)

### 3. **Verify the Installation**

- After the installation completes, open the `cmd.exe` terminal and run the following command to ensure that CUDA has been installed correctly:
```
nvcc --version
```
This will display the installed CUDA version.

### **4. Install Cupy**
Run the following command in your terminal to install Cupy:
```
pip install cupy-cuda11x
```

## 5. CUDNN Installation 🧩
Download cuDNN (CUDA Deep Neural Network library) from the NVIDIA website:

👉 [Download CUDNN](https://developer.nvidia.com/downloads/compute/cudnn/secure/8.9.6/local_installers/11.x/cudnn-windows-x86_64-8.9.6.50_cuda11-archive.zip/). (Requires an NVIDIA account – it's free).

## 6. Unzip and Relocate 📁➡️
Open the `.zip` cuDNN file and move all the folders/files to the location where the CUDA Toolkit is installed on your machine, typically:

```
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8
```


## 7. Get TensorRT 8.6 GA 🔽
Download [TensorRT 8.6 GA](https://developer.nvidia.com/downloads/compute/machine-learning/tensorrt/secure/8.6.1/zip/TensorRT-8.6.1.6.Windows10.x86_64.cuda-11.8.zip).

## 8. Unzip and Relocate 📁➡️
Open the `.zip` TensorRT file and move all the folders/files to the CUDA Toolkit folder, typically located at:

```
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8
```


## 9. Python TensorRT Installation 🎡
Once all the files are copied, run the following command to install TensorRT for Python:

```
pip install "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\python\tensorrt-8.6.1-cp311-none-win_amd64.whl"
```

🚨 **Note:** If this step doesn’t work, double-check that the `.whl` file matches your Python version (e.g., `cp311` is for Python 3.11). Just locate the correct `.whl` file in the `python` folder and replace the path accordingly.

## 10. Set Your Environment Variables 🌎
Add the following paths to your environment variables:
- `system path`
```
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\lib
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\libnvvp
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\bin
```

# Setting Up CUDA 11.8 with cuDNN on Windows

Once you have CUDA 11.8 installed and cuDNN properly configured, you need to set up your environment via `cmd.exe` to ensure that the system uses the correct version of CUDA (especially if multiple CUDA versions are installed).

## Steps to Set Up CUDA 11.8 Using `cmd.exe`

### 1. Set the CUDA Path in `cmd.exe`

You need to add the CUDA 11.8 binaries to the environment variables in the current `cmd.exe` session.

Open `cmd.exe` and run the following commands:
- DO each one `Separately`
```
set PATH=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\bin;%PATH%
set PATH=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\libnvvp;%PATH%
set PATH=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\extras\CUPTI\lib64;%PATH%
```
These commands add the CUDA 11.8 binary, lib, and CUPTI paths to your system's current session. Adjust the paths as necessary depending on your installation directory.

2. Verify the CUDA Version
After setting the paths, you can verify that your system is using CUDA 11.8 by running:
```
nvcc --version
```
This should display the details of CUDA 11.8. If it shows a different version, check the paths and ensure the proper version is set.

3. **Set the Environment Variables for a Persistent Session**
If you want to ensure CUDA 11.8 is used every time you open `cmd.exe`, you can add these paths to your system environment variables permanently:

1. Open `Control Panel` -> `System` -> `Advanced System Settings`.
Click on `Environment Variables`.
Under `System variables`, select `Path` and click `Edit`.
Add the following entries at the top of the list:
```
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\bin
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\libnvvp
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\extras\CUPTI\lib64
```
This ensures that CUDA 11.8 is prioritized when running CUDA applications, even on systems with multiple CUDA versions.

4. **Set CUDA Environment Variables for cuDNN**
If you're using cuDNN, ensure the `cudnn64_8.dll` is also in your system path:
```
set PATH=C:\tools\cuda\bin;%PATH%
```
This should properly set up CUDA 11.8 to be used for your projects via `cmd.exe`.

#### Additional Information
- Ensure that your GPU drivers are up to date.
- You can check CUDA compatibility with other software (e.g., PyTorch or TensorFlow) by referring to their documentation for specific versions supported by CUDA 11.8.

### Environmental Variable Setup

![pic](https://github.com/FNBUBBLES420-ORG/Assistive-AimGuide/blob/main/Environtmental_Setup/pic.png)

```
import torch

print(torch.cuda.is_available())  # This will return True if CUDA is available
print(torch.version.cuda)  # This will print the CUDA version being used
print(torch.cuda.get_device_name(0))  # This will print the name of the GPU, e.g., 'NVIDIA GeForce RTX GPU Model'
```
run the `get_device.py` to see if you installed it correctly 

---
# 🚀 Visual Studio 2022 Community Edition Installation Guide

This guide will help you download and install **Visual Studio 2022 Community Edition** with the **Desktop Development with C++** workload for C and C++ development.

## 📥 Step 1: Download Visual Studio

Click the following link to download **Visual Studio 2022 Community Edition**:  
👉 [Download Visual Studio 2022 Community Edition](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Community&channel=Release&version=VS2022&source=VSLandingPage&cid=2030&passive=false)

## 🛠 Step 2: Installing Visual Studio

1. Once the installer is downloaded, **run the installer**.
2. In the **Visual Studio Installer**, select the **Workloads** tab.

## 🖥 Step 3: Select Workload for C++ Development

To set up **C++ development**, ensure you select the **Desktop development with C++** workload:

1. In the **Workloads** tab, check the option **Desktop development with C++**.
   - This will install the necessary tools for C++ programming, including compilers, libraries, and debugging tools.
2. Click **Install** to begin the installation process.

## 🛠 System Requirements Visual Studio 2022

Make sure your system meets the minimum requirements for Visual Studio 2022:
- **OS**: Windows 10 or higher.
- **Processor**: Quad-core processor or better.
- **RAM**: 8 GB of RAM (16 GB recommended).
- **Disk Space**: Minimum 20 GB free space.

## 🛑 Troubleshooting

If you encounter any issues during installation, refer to the official troubleshooting guide:  
- [Visual Studio Installation Troubleshooting](https://docs.microsoft.com/en-us/visualstudio/install/troubleshooting-installation-issues?view=vs-2022)

## Now you're ready to start developing C and C++ applications in Visual Studio 2022! 🎉
---
## 🛠 Run Script `run.bat`

The `run.bat` script is a batch file to help you install all the required dependencies for this project. Below is the content of the file and the steps it will execute:

```
@echo off
echo Installing ONNX Runtime (GPU)...
pip install onnxruntime-gpu
echo Press enter to continue with the rest of the dependency installs
pause

echo Installing NumPy...
pip install numpy
echo Press enter to continue with the rest of the dependency installs
pause

echo Installing comtypes...
pip install comtypes
echo Press enter to continue with the rest of the dependency installs
pause

echo Installing OpenCV (opencv-python)...
pip install opencv-python
echo Press enter to continue with the rest of the dependency installs
pause

echo Installing pandas...
pip install pandas
echo Press enter to continue with the rest of the dependency installs
pause

echo Installing bettercam...
pip install bettercam
echo Press enter to continue with the rest of the dependency installs
pause

echo Installing onnx...
pip install onnx
echo Press enter to continue with the rest of the dependency installs
pause

echo Installing PyWin32...
pip install pywin32
echo Press enter to continue with the rest of the dependency installs
pause

echo Installing Dill...
pip install dill
echo Press enter to continue with the rest of the dependency installs
pause

echo Installing CuPy (GPU accelerated array library for CUDA 11.8)...
pip install cupy-cuda11x
echo Press enter to continue with the rest of the dependency installs
pause

echo Installing psutil...
pip install psutil
echo Press enter to continue with the rest of the dependency installs
pause

echo Installing colorama...
pip install colorama
echo Press enter to continue with the rest of the dependency installs
pause

echo Installing ultralytics...
pip install ultralytics
echo Press enter to continue with the rest of the dependency installs
pause

echo Installing PyAutoGUI...
pip install PyAutoGUI
echo Press enter to continue with the rest of the dependency installs
pause

echo Installing PyGetWindow...
pip install PyGetWindow
echo Press enter to continue with the rest of the dependency installs
pause

echo Installing pyyaml...
pip install pyyaml
echo Press enter to continue with the rest of the dependency installs
pause

echo Installing tqdm...
pip install tqdm
echo Press enter to continue with the rest of the dependency installs
pause

echo Installing matplotlib...
pip install matplotlib
echo Press enter to continue with the rest of the dependency installs
pause

echo Installing seaborn...
pip install seaborn
echo Press enter to continue with the rest of the dependency installs
pause

echo Installing requests...
pip install requests
echo Press enter to continue with the rest of the dependency installs
pause

echo Installing ipython...
pip install ipython
echo Press enter to continue with the rest of the dependency installs
pause

echo Installing dxcam...
pip install dxcam
echo Press enter to continue with the rest of the dependency installs
pause

echo Installing pyarmor...
pip install pyarmor
echo Press enter to continue with the rest of the dependency installs
pause

echo Installing serial...
pip install serial
echo Press enter to continue with the rest of the dependency installs
pause

echo Installing onnx-simplifier...
pip install onnx-simplifier
echo Press enter to continue with the rest of the dependency installs
pause

echo Installing onnxruntime...
pip install onnxruntime
echo Press enter to continue with the rest of the dependency installs
pause

echo MAKE SURE TO HAVE THE WHL DOWNLOADED BEFORE YOU CONTINUE!!!
pause
echo Click the link to download the WHL: press ctrl then left click with mouse
echo https://github.com/cupy/cupy/releases/download/v13.4.0/cupy_cuda11x-13.4.0-cp311-cp311-win_amd64.whl
pause

echo Installing CuPy from WHL...
pip install https://github.com/cupy/cupy/releases/download/v13.4.1/cupy_cuda11x-13.4.1-cp311-cp311-win_amd64.whl
pause

echo All packages installed successfully!
pause

```

## How to Use the `run.bat` Script

1. **Download the Required Files:**

   - Ensure you have downloaded the WHL file for CuPy from the following link:
     [Download CuPy WHL](https://github.com/cupy/cupy/releases/download/v13.4.1/cupy_cuda11x-13.4.1-cp311-cp311-win_amd64.whl)

2. **Run the Batch File:**

   - Execute the `run.bat` file to automatically install all necessary Python dependencies for this project.

   - The script will pause after each step so you can verify the installation. Simply press any key to continue after each pause.

   To execute the batch file, you can use:

   ```
   ./run.bat
   ```
