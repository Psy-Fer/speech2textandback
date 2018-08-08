import sys
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types


filename = 'gs://sound_staging/' + sys.argv[1]


def main():
    print "calling API"
    transcribe_gcs(filename)
    print "Done!"


def transcribe_gcs(gcs_uri):
    """Asynchronously transcribes the audio file specified by the gcs_uri."""
    
    client = speech.SpeechClient()

    audio = types.RecognitionAudio(uri=gcs_uri)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=16000,
        language_code='en-AU')

    operation = client.long_running_recognize(config, audio)

    print('Waiting for operation to complete...')
    response = operation.result(timeout=90)

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    output = []
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        output.append(result.alternatives[0].transcript)
        #print('Transcript: {}'.format(result.alternatives[0].transcript))
        #print('Confidence: {}'.format(result.alternatives[0].confidence))
    print('Transcription:')
    print(' '.join(output))
    with open('input.txt', 'w') as f1:
        f1.write(' '.join(output))
    
if __name__ == '__main__':
    main()

