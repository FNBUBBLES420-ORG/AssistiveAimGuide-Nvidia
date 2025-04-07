# 🎯 Assistive AimGuide

**Assistive AimGuide** is a vision-based AI tool created to support **disabled gamers**. It provides intelligent, smooth aiming assistance by detecting objects on the screen and gently guiding the mouse. Perfect for users with physical or cognitive challenges who need support while gaming.

> 💙 Built with accessibility in mind by the FNBUBBLES420 Organization.

---

## 🟢 How to Download and Install (No GitHub Required)

1. Click the **green `Code` button** at the top-right of this page.
2. Select **`Download ZIP`**.
3. Once downloaded, **extract the ZIP** to any folder (such as your Desktop).
4. Open the folder you extracted.

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

---

## 📦 Install Requirements

Once Python is installed (via the `.bat` file or manually), open a terminal or command prompt in the folder and run:

```bash
pip install -r requirements.txt
```

## 🧠 How It Works

- Uses YOLO models to detect objects on the screen.

- Moves the mouse in smooth, human-like motions toward targets.

- Designed to be assistive, not aggressive or fast-paced.

- Optional headshot mode, mask filtering, confidence levels, and more.

## ⚙️ Configuration

Edit your settings directly in `config.py`.

```
# Configurations for the application

# Screen capture dimensions
screenShotHeight = 320
screenShotWidth = 320

# Mask configurations
useMask = False
maskSide = "left"
maskWidth = 100
maskHeight = 200

# Mouse movement amplification
aaMovementAmp = .4

# Detection confidence threshold
confidence = 0.4

# Key to terminate the program
aaQuitKey = "8"

# Enable aiming at the head region
headshot_mode = True

# Display processing speed in console
cpsDisplay = True

# Enable visual overlays of detections
visuals = False

# Focus detections around the center of the screen
centerOfScreen = True

# Path to the model file (change as needed)
model_path = 'pt_models//v5'  # base path without extension

# Model type ('onnx' for ONNX models, 'engine' for TensorRT models)
model_type = 'onnx'

# GPU configurations
enable_cuda = True
device_type = 'cuda'
```

## 🚀 How to Run
Once everything is ready:

```
python main_tensorrt.py
```

- Press the configured quit key (e.g., `8`) to stop the app at any time.
---

# 🙌 Made With ❤️ by Bubbles The Dev & FNBubbles420 Org
### This app is part of the mission of [FNBUBBLES420 ORG](https://fnbubbles420.org) – helping gamers with disabilities break limits and play freely.

### 💌 Questions or Support?
- Join our Discord community.
- [Click To Join Discord](https://discord.fnbubbles420.org/invite)