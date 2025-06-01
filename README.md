# Synthetic Data Generation Pipeline using NVISII

A modular and efficient synthetic data generation pipeline built with [NVISII](https://www.nvisii.com/) (from NVIDIA), designed to support high-quality dataset creation for computer vision tasks such as object detection, segmentation, and more.

This project automates the process of placing 3D models into diverse lighting and environmental conditions using HDRIs and 3D scenes, enabling rapid generation of annotated datasets.

---

## 📦 Repository Structure

```

.
├── backgrounds/              # Background images used in data generation
├── blenderproc\_data\_gen/    # Optional integration with BlenderProc (if needed)
├── dome\_hdri\_haven/         # HDRI environments from HDRI Haven
├── models/                  # 3D object models (e.g., Ketchup bottle)
│   └── Ketchup/google\_16k/
├── nvisii\_data\_gen/         # Core NVISII rendering scripts and generation logic
├── validate\_data.py         # Script to verify generated annotations and images
├── LICENSE                  # License information
└── README.md                # This file

````

---

## 🚀 Features

- ✅ Fully scriptable rendering pipeline using Python
- 🌍 High dynamic range environments (HDRIs) for photorealism
- 📷 Automatic camera positioning and scene randomization
- 🏷️ Output includes rendered images and annotation metadata
- 🧪 Data validation tools to ensure annotation integrity

---

## 🧰 Technologies Used

- **Python** — scripting language for orchestration
- **NVISII** — real-time photorealistic rendering from NVIDIA
- **NumPy, Pillow** — image and array processing
- **OpenGL (via NVISII backend)** — GPU-accelerated rendering
- *(Optional)* **BlenderProc** — integration-ready for alternative pipelines

---

## 💡 Example Usage

Here’s a minimal example of generating a scene using NVISII:

```python
import nvisii
import random

nvisii.initialize(headless=True)

# Set up camera
nvisii.create_camera("camera", position=(0, 0, 1), look_at=(0, 0, 0))

# Load 3D model
model = nvisii.entity.create(
    name="ketchup",
    mesh=nvisii.mesh.create_from_file("models/Ketchup/google_16k/model.obj"),
    transform=nvisii.transform.create("ketchup_transform"),
    material=nvisii.material.create("ketchup_material")
)

# Randomize lighting
nvisii.set_dome_light_intensity(random.uniform(0.5, 2.0))
nvisii.set_dome_light_color((1.0, 1.0, 1.0))
nvisii.set_dome_light_texture("dome_hdri_haven/example.hdr")

# Render and save
nvisii.render_to_file(512, 512, "output/ketchup_render.png")
nvisii.deinitialize()
````

---

## 📂 Output

Each run of the pipeline produces:

* High-resolution `.png` renders
* Metadata and bounding box annotations (e.g., COCO or YOLO format)
* Optional segmentation masks

---

## 🔍 Validation

Use `validate_data.py` to inspect and validate the quality and consistency of your generated data.

```bash
python validate_data.py --input_dir output/
```

---

## 📜 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions, issues, and ideas are welcome! Please open an issue or submit a pull request if you'd like to collaborate.

---

## 🌐 Credits

* [NVISII](https://github.com/owl-project/NVISII)
* [HDRI Haven](https://polyhaven.com/hdris) for dome lighting assets
* Google Scanned Objects for 3D models

---

*Crafted with 💡 and GPU power.*

