import csv

with open('questions.csv', 'r') as f:
    reader = csv.DictReader(f)
    questions = list(reader)
    results = []
    for question in questions:
        question_dict = {
            "original_url": question.get("URL Original"),
            "fb_modified_question": question.get("Pregunta"),
            "fb_answer": question.get("Respuesta"),
            "original_fb_post": question.get("Contexto Pregunta"),
            "original_fb_answer": question.get("Contexto Respuesta"),
            "main_category": question.get("Categoria Principal"),
            "category_2": question.get("Categoria 2"),
            "category_3": question.get("Categoria 3"),
            "category_4": question.get("Categoria 4"),
            "category_5": question.get("Categoria 5"),
            "answer": question.get("Respuesta"),
            "link_1": question.get("Link 1"),
            "link_2": question.get("Link 2"),
            "link_3": question.get("Link 3"),
            "link_4": question.get("Link 4"),
            "tag_1": question.get("Tag 1"),
            "tag_2": question.get("Tag 2"),
            "tag_3": question.get("Tag 3"),
            "tag_4": question.get("Tag 4"),
            "tag_5": question.get("Tag 5"),
            "location": "",
            "modified_by": "system",
            "version": 1
        }
        results.append(question_dict)
    print(results[0])
