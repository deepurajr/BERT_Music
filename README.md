1. Download the following dataset files and place it in `data` folder :
 - [fma_metadata.zip](https://os.unil.cloud.switch.ch/fma/fma_metadata.zip)
 - [fma_small.zip](https://os.unil.cloud.switch.ch/fma/fma_small.zip)


<br>

2. Unzip the zip files

```
> unzip fma_small.zip
> unzip fma_metadata.zip
```

<br>
3. Run the following python files in the below order to generate the 128x128 sliced spectrogram images

```
> python data/import_data.py
> python data/load_train_data.py
> python data/slice_spectrogram.py
```

<br> 
4. Train the model

```
> python cnn_train.py
```

<br>
5. Run the application

```
> python app_server.py
```

Access the UI at the URL [http://localhost:5000](http://localhost:5000)
