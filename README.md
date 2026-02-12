# Genomic Visualization Exercise 3

This repository contains the solution for **Visualization Exercise 3**, where a multi-panel line plot figure is recreated using Python and Matplotlib.

The visualization consists of a **2x3 grid of line plots**, each representing percentage values over time.

---

## 📂 Repository Structure

- `data/`
  - `10_project_data_lineplots.csv` – Dataset used for generating the plots.

- `images/`
  - `lineplots_grid_example.png` – Example output image.

- `notebooks/`
  - `Visualization_Exercise_3.ipynb` – Jupyter notebook containing the complete solution.

- `scripts/`
  - `plot_lineplots_grid.py` – Standalone Python script to generate the visualization.

- `images/`
  - `lineplots_grid_example.png` – Example output image (optional).

---

## 📊 Visualization Description

The figure contains:

- A 2x3 grid layout
- Six line plots labeled A–F
- Percentage-formatted y-axis
- Clean styling (no top/right/left spines)
- Horizontal grid lines
- Uniform y-axis limits for visual comparability

This layout enables easy comparison across categories while maintaining consistent formatting.

---

## 🛠 Libraries Used

- Python 3.x
- pandas
- numpy
- matplotlib

---

## ▶ How to Run
### 1. Clone the Repository

```bash
git clone https://github.com/Kin-zala/Genomic_visualization_3.git
```
### 2. Install Required Libraries
#### Make sure Python 3.x is installed, then run:
```bash 
pip install -r requirements.txt
```

### 3. Run the Project
**Option A** – Using Jupyter Notebook:
```bash
 jupyter notebook
```
#### Open:
```bash
 notebooks/Visualization_Exercise_3.ipynb
```
#### Then click 'Run All Cells'.

**Option B** – Using Python Script:
```bash
 python scripts/plot_lineplots_grid.py
```


### OUTPUT
![alt-image](https://github.com/Kin-zala/Genomic_visualization_3/blob/ea5b7bb13a2948e1776e3879b23312af1937b422/images/lineplots_grid_example.png)
