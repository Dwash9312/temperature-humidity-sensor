## 📌 Project Overview
This project is an **IoT-based home environment monitoring system** that uses an **Arduino with a DHT11 sensor** to track **temperature and humidity** in real-time. The collected data is visualized using **Power BI** to analyze trends, correlations, and variations over time.

The goal of this project is to:
- **Monitor indoor temperature and humidity patterns**.
- **Identify trends and correlations** between the two variables.
- **Optimize indoor climate conditions** based on insights.

---

## 📊 Key Features
- **Live Data Collection:** Temperature and humidity readings from the **DHT11 sensor**.
- **Time-Series Analysis:** Understanding fluctuations over time.
- **Temperature & Humidity Correlation:** Identifying how these factors influence each other.
- **Interactive Power BI Dashboard:** Visualizing insights in an easy-to-understand format.

---

## 📁 Dataset Information
- **Source:** Collected from an **Arduino DHT11 sensor**.
- **Format:** `.csv`
- **Columns:**
- `timestamp` - The date and time of the reading.
- `temperature_f` - Temperature recorded in Fahrenheit.
- `humidity` - Humidity percentage.

---

## 🛠 Technologies Used
- **Arduino** - For data collection using the DHT11 sensor.
- **Python** (Pandas) - Data preprocessing and analysis.
- **Power BI** - Dashboard visualization.
- **SQL** - Data storage and querying (if applicable).


---

## 📂 Repository Structure

/temperature-humidity-sensor
│── /Code # Python & Arduino scripts
│── /Dashboard # Power BI file and dashboard images
│── /Data # Raw sensor data (CSV format)
│── /Docs # Additional documentation
│── LICENSE # Open-source license (if applicable)
│── PCB-Design # PCB schematic (if applicable)
│── README.md # Main project documentation
│── data-insights.md # Detailed insights and findings

---

## 📈 Insights & Findings
Key insights from the data can be found in [`data-insights.md`](data-insights.md), including:
- **Temperature fluctuates** throughout the day, with dips around **early morning (4 AM)**.
- **Humidity increases in the morning**, peaking around **10 AM** before stabilizing.
- **Inverse relationship**: When temperature decreases, humidity increases.
- **Potential actions:** Adjusting **HVAC settings** and improving **ventilation for humidity control**.

---

## 📊 Power BI Dashboard Preview
Here’s a preview of the **Power BI dashboard**:

![image](https://github.com/user-attachments/assets/8838fee1-4c1b-4ef1-b14f-09579a8d1f2b)


---

## 📖 How to Use This Project
1. **Clone the repository:**
```sh
git clone https://github.com/Dwash9312/temperature-humidity-sensor.git

2. Open Power BI and load the dashboard.pbix file.
3. Explore the visualizations for insights on temperature and humidity trends.

🚀 Future Improvements
• Automate data collection and integrate with a cloud database.
• Add real-time dashboard updates.
• Compare indoor vs. outdoor temperature by integrating weather APIs.

📬 Contact

If you have any questions or feedback, feel free to reach out!
Author:
Darian Washington

LinkedIn:
(https://www.linkedin.com/in/darian-washington-mba-msda-99b49a130/)

GitHub:
(https://github.com/Dwash9312)

Email:Darianwashington8@gmail.com

