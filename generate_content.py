def generate_question_content():
    word_list = []
    level = ''

    for text in word_list:
        params = { "query": text }
        headers = {
            "Accept-Version": "v1",
            "Authorization": "Client-ID {}".format(unsplash_access_key)
        }
        response = requests.get("https://api.unsplash.com/search/photos", params=params, headers=headers)
        image_url = json.loads(response.text)["results"][0]["urls"]["full"]

        speech_question = SpeechQuestion(text=text, level=level, image_url=image_url)
        db.session.add(speech_question)
        db.session.commit()

    print("{} {}-level words have been added to the database!".format(len(word_list), level))
