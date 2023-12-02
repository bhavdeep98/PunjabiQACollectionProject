# PunjabiQACollectionProject

## Human-in-the-Loop System for Non-English Language Prompts and Completions

This system constitutes a human-in-the-loop framework designed to facilitate the generation of prompts and completions in non-English languages.

### Problem Statement:

The primary issue addressed by this project was the challenge faced by team members in incorporating new examples in Punjabi. The Punjabi language, due to various factors, is experiencing a decline, particularly among individuals working away from their native regions. Many, including myself, have encountered difficulty in recalling how to write in Punjabi, if not read it. This project aims to bridge this linguistic gap. 

### Key Challenges:

1. **Linguistic Decay:** Punjabi language faces a decline, especially among individuals away from their homeland.
2. **Translation Challenges:** Existing automatic translators struggle with accurately translating Punjabi.
3. **Digitization Issues:** Limited digitization of old and historical Punjabi texts results in a scarcity of high-quality digital content.

### System Workflow:

The system functions by retrieving crawled news from the internet, as it represents well-written Punjabi content available in digital format. Google's Translator API is utilized to convert the Punjabi text into English, enabling the initiation of the process in either language. Subsequently, a set of questions in English is generated using the [question_generator](https://github.com/AMontgomerie/question_generator/tree/master) code, full credits to the owners.

### Human Intervention:

Upon reviewing the generated questions, a human operator has the option to modify the questions or create entirely new ones. An answer can be derived from the entered question using Hugging Face's open-source QA models like BERT. However, due to potential inaccuracies, human intervention is critical to verify and rectify the answer. The generated answer aids in locating relevant information within the text.

### Translation and Model Refinement:

The human-provided answer is then translated back into the original language, Punjabi in this case. Translation errors are addressed in Punjabi before feeding the model. This iterative process significantly accelerates the manual entry process, achieving a tenfold increase in efficiency.

This project not only addresses immediate challenges faced by the team but also contributes to the preservation and revitalization of Punjabi language through effective human-machine collaboration.
