# discharge-pressure-prediction

It is a regression of predicting Discharge Pressure of a compressor in psig.

![image](https://user-images.githubusercontent.com/33491664/137442836-aa014416-3779-4b38-b1cb-d97051154455.png)


**Use the following commands to run the application :** \
Step 1: `git clone git@github.com:abhishek-shrm/discharge-pressure-prediction.git` \
Step 2: Move to the downloaded repository \
Step 3: `sudo docker build -t discharge-pressure-prediction:1.0.0 .` \
Step 4: `sudo docker run -p 5000:5000 discharge-pressure-prediction:1.0.0` \
Step 5: Open localhost:5000 to use the application

## Data

![image](https://user-images.githubusercontent.com/33491664/137443044-e2b3d778-1cf0-4392-b8ed-05a7c6a4ddc9.png)

This dataset contains 296450 rows and 9 columns.

## Results
|                Algorithm                |  RMSE  |
|:---------------------------------------:|:------:|
| Multiple Linear Regression              | 2.4545 |
| Multi-Dimensional Polynomial Regression | 1.2163 |
| XGBoost Regressor                       | 1.3080 |
| Multi-Layer Perceptron                  | 1.6427 |

## Final Pipeline
![image](https://user-images.githubusercontent.com/33491664/137442215-b335dff5-4613-44ca-98e1-62d220c3581f.png)
