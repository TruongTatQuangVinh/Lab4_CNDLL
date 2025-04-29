# Lab 4
Họ và tên: Trương Tất Quang Vinh <br>
MSSV: 22521683 <br>
Dataset: https://www.kaggle.com/datasets/jayaantanaath/student-habits-vs-academic-performance/data

## Structure
```
lab-4_original
├── data
│   └── train.csv          # Training data for the model
├── server
│   ├── sender.py          # Server that sends data
│   └── receiver.py        # Server that receives data
├── model
│   ├── train_model.py     # Logic for training the model
│   └── utils.py           # Utility functions for preprocessing and evaluation
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

## Setup Instructions
1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd lab-4_original
   ```

2. **Install dependencies**:
   Socket, pandas
   
4. **Prepare the data**:
   Ensure that the `data/train.csv` file is present and contains the necessary training data.

## Usage
1. **Start the receiver server**:
   Open a terminal and run:
   ```
   python server/receiver.py
   ```

2. **Start the sender server**:
   In another terminal, run:
   ```
   python server/sender.py
   ```

3. **Train the model**:
   After the data has been sent and received (the received file is in `Lab4/data/` folder), you can train the model by running:
   ```
   python model/train_model.py
   ```
   
