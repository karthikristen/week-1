# 💧 Water Quality Checker (AI/ML Project)

## 📌 Project Overview
This project is an **AI/ML-based Water Quality Checker** that predicts whether a given water sample is **Safe, Moderate, or Unsafe** for drinking.  
The model uses input parameters such as **pH, Hardness, Nitrate, Conductivity, and TDS** and classifies the water quality based on trained rules.

This is an ongoing project – currently showing **30% progress**.

---

## ✅ Current Features (30% Progress)
- **Synthetic Dataset Creation** (500 samples with random values for water quality parameters).
- **Labeling Function** that categorizes water into `Safe`, `Moderate`, or `Unsafe`.
- **RandomForest Classifier** trained on the dataset.
- **Tkinter GUI** for user input:
  - Enter pH, Hardness, Nitrate, Conductivity, and TDS values.
  - Get classification result in a popup window.
- **Visualization**:
  - Displays a bar chart of entered parameters for better understanding.

---

## 🖼️ GUI Preview
When you run the program, you will see:
- Input fields for **pH, Hardness, Nitrate, Conductivity, TDS**.
- A **Check Water Quality** button.
- Result displayed as **Safe, Moderate, or Unsafe**.
- A **bar chart** of entered water sample parameters.

---

## 🔮 Next Steps (Planned Progress)
- [ ] Replace synthetic dataset with a **real-world water quality dataset**.
- [ ] Improve GUI design with modern styling and icons.
- [ ] Add feature to **export results as PDF/CSV report**.
- [ ] Package project into a **standalone `.exe` application**.
- [ ] (Optional 🚀) Integrate **IoT sensors** for real-time water sample input.

---

## 🛠️ Technologies Used
- **Python 3**
- **Pandas, NumPy** (data handling)
- **Scikit-learn** (RandomForest model)
- **Tkinter** (GUI)
- **Matplotlib** (visualization)

---

## 📂 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Water-Quality-AIML.git
   cd Water-Quality-AIML
2.Install required dependencies:

pip install pandas numpy scikit-learn matplotlib


3.Run the program:

python water_quality_checker.py
