echo "Recording your Speech (Ctrl+C to Transcribe)"
arecord -q -f cd -t wav -d 0 -r 16000 test.wav
echo "Converting file...."
sox -G test.wav --channels=1 --bits=16 --rate=16000 test.flac
echo "Uploading to cloud...."
gsutil -m cp -a public-read test.flac gs://sound_staging
echo "Cleaning up...."
rm test.flac test.wav
echo "Detecting speech and stuff...."
python async_speech.py test.flac
echo "Cleaning up cloud..."
gsutil rm gs://sound_staging/test.flac

