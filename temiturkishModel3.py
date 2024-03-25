from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline
from gtts import gTTS


def text_to_speech(text, language='tr', slow=False):
    tts = gTTS(text=text, lang=language, slow=slow)
    tts.save("./temp_output.mp3")
    return "./temp_output.mp3"


def get_answer(question, context):
    tokenizer = AutoTokenizer.from_pretrained("muratsimsek003/turkish_bert_qa")
    model = AutoModelForQuestionAnswering.from_pretrained("muratsimsek003/turkish_bert_qa")
    qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)


    answer = qa_pipeline(question=question, context=context)["answer"]
    return answer


def temi_main(question):
    # Bu örnekte, gerçek bir uygulamada yerine geçecek basit bir metin kullanıyoruz.
    # Gerçek uygulamada, bu context verisi dinamik olarak sağlanmalıdır.
    with open('ostim.txt', encoding='utf-8') as dosya:
        context = dosya.read()

    answer = get_answer(question, context)
    speech_file_path = text_to_speech(answer)

    return answer, speech_file_path
