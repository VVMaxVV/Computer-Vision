# 🧊 Rubik’s Cube Color Scanner and Solver

This project allows you to **scan a real Rubik’s Cube using photos of its faces**, automatically detect the colors of each sticker, reconstruct the cube in code, and then **find and visualize the solution** step by step.

It combines **OpenCV**, **NumPy**, **Matplotlib**, and the **Kociemba algorithm** to achieve full color-based cube state recognition and visualization.

---

## 🚀 Features

- Detects and extracts the cube face automatically from a photo  
- Classifies each sticker into one of six standard cube colors  
- Generates visual grid overlays on each scanned image  
- Builds a 3D cube representation from six images  
- Solves the cube using the **Kociemba two-phase algorithm**  
- Displays each move visually with matplotlib graphics  

---

## 🧩 How It Works

1. **Color Detection**  
   Each face image is processed through:
   - Gaussian blur  
   - Canny edge detection  
   - Contour extraction to find the cube’s square  
   - Perspective transform for flat alignment  
   - HSV-based color classification for each 3×3 cell  

2. **Cube Reconstruction**  
   The program reads six images named:
   ```
   up.jpg, front.jpg, left.jpg, right.jpg, back.jpg, down.jpg
   ```
   Each face’s colors are detected and mapped to corresponding cube notations (`U, D, F, B, L, R`).

3. **Solution Calculation**  
   The full cube state is encoded into a Kociemba-compatible format and passed into the `kociemba.solve()` function.

4. **Visualization**  
   A step-by-step visual demonstration of the cube being solved is rendered using **matplotlib** rectangles and color-coded patches.

---

## 🛠️ Requirements

Make sure you have Python 3.9+ installed, then install dependencies:

```bash
pip install opencv-python numpy matplotlib kociemba
```

---

## 📸 Usage

1. Take **six clear photos** of each cube face (flat and centered).  
   Save them in the same folder as your script:

   ```
   up.jpg
   front.jpg
   left.jpg
   right.jpg
   back.jpg
   down.jpg
   ```

2. Run the script:

   ```bash
   python cube_scan.py
   ```

3. The program will:
   - Detect the colors
   - Save processed face images (e.g. `out_front.jpg`)
   - Display the cube’s unfolded net
   - Compute and display the step-by-step solution

---

## 🧠 Example Output

```
Detected colors:
['Green', 'Green', 'White']
['Green', 'Green', 'Red']
['Green', 'Green', 'Red']

Saved as out_up.jpg
...
Cube string: UURUUFUUFRRBRRBRRBRRDFFDFFDDDBDDBDDLFFFLLLLLLULLUBBUBB
Solution: R' U'
```

Visual cube diagrams will also appear in pop-up windows via matplotlib.

---

## 🖼️ Cube Layout (Unfolded)

```
        [UP]
 [LEFT] [FRONT] [RIGHT] [BACK]
        [DOWN]
```

---

## 🧰 Technologies Used

- **Python 3**
- **OpenCV** – image processing & color detection
- **NumPy** – matrix operations
- **Matplotlib** – cube visualization
- **Kociemba** – Rubik’s Cube solving algorithm