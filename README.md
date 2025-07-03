# HAR on a Raspberry Pi

These python files are intended to run on a raspberry pi connected to a Qwiic phat with a Multisensor stick (BME280 + LTR559 + LSM6DS3). 
The mainV1.py file will read accelerator values and pass them through a deep learning model trained on UCI HAR dataset. It will predict what the human wearing the device is doing (walking, walking up, walking down, standing, lying and sitting)

The link to the model used can be found here: https://github.com/emadeldeen24/TS-TCC/blob/main/data_preprocessing/uci_har/preprocess_har.py
