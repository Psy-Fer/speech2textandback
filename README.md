# speech2textandback

A quick example of how to implement speech to text, and text to speech using google cloud.

Used in Deep Learning and Beyond workshop.

```
>pip install google-cloud
>pip install google-cloud-texttospeech
>pip install google-cloud-speech

>apt-get install sox
>apt-get install libsox-fmt-all

>apt-get install gcc python-dev python-setuptools
>easy_install -U pip
>pip uninstall crcmod
>pip install -U crcmod

>wget https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-194.0.0-linux-x86.tar.gz 
# Unpack and install:
>tar -zxvf google-cloud-sdk-194.0.0-linux-x86.tar.gz
>./google-cloud-sdk/install.sh
>./google-cloud-sdk/bin/gcloud init

```


```
>gsutil -m cp -a public-read test.flac gs://<public_staging>

>gsutil rm gs://<public_staging>/test.flac

```
