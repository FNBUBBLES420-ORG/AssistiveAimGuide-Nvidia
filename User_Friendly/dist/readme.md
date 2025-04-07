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