echo "Converting text to speech..."
python text_to_speech.py input.txt
echo "Converting audio..."
sox -G output.mp3 --channels=1 --bits=16 --rate=16000 output.wav
echo "Playing audio..."
aplay output.wav
echo "Cleaning up..."
rm output.mp3 output.wav
echo "Done!"

