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

# Key to activate the aim assist
aaActivateKey = "CapsLock"

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
