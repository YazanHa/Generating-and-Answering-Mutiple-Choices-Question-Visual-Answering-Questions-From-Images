# mcqsApp/utils.py

from gradio_client import Client, file
from ollama import Client as OllamaClient
import json
from .variables import get_messages, get_full_prompt
import os
from groq import Groq


def image_to_text(image_path):
    # Initialize clients
    image_describe_client = Client("openbmb/MiniCPM-Llama3-V-2_5")
    
    # Get the image description
    print(image_describe_client.predict(
        image=file(image_path),
        _chatbot=[],
        api_name="/upload_img"
    ))

    prompt = get_full_prompt()

    describe_result = image_describe_client.predict(
        _chat_bot=[[prompt,None]],
        params_form="Sampling",
        num_beams=3,  # Increased for higher quality
        repetition_penalty=1.2,
        repetition_penalty_2=1.05,
        top_p=1,  # Slightly higher for more comprehensive consideration
        top_k=10,
        temperature=0.3,  # Slightly lower for coherence
        api_name="/respond"
    )
    
    description = describe_result[0][1]
    return description


# def text_to_mcqs(description, context=None):

#     description_MCQs_client = OllamaClient(host='http://172.25.1.139:11434')

#     messages = get_messages(description, context)

#     response = description_MCQs_client.chat(
#         model='llama3',
#         messages=messages
#     )

#     MCQs_output = response['message']['content']
#     response2 = description_MCQs_client.chat(
#         model='llama3',
#         messages=[
#             {
#                 'role': 'system',
#                 'content': """
#                     You are an assistant for create JSON format like:
#                         {   
#                             "question": "",
#                             "option_1": "",
#                             "option_2": "",
#                             "option_3": "",
#                             "option_4": "",
#                             "correct_answer": ""
#                             "Difficulty_Level":""
#                         }
#                         create List of this questions with JSON format.
#                     """
#             },
#             {
#                 'role': 'user',
#                 'content': MCQs_output
#             },
#         ]
#     )

#     MCQs_JSON_output = response2['message']['content']

#     start_index = MCQs_JSON_output.find('[')
#     end_index = MCQs_JSON_output.rfind(']') + 1
#     json_part = MCQs_JSON_output[start_index:end_index]
#     questions_dict = json.loads(json_part)
    
#     return questions_dict


# def groq_text_to_mcqs(description, context=None):

#     GroqClient = Groq(
#         api_key="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",
#     )
#     messages = get_messages(description, context)

#     chat_completion = GroqClient.chat.completions.create(
#         messages=messages,
#         model="llama3-70b-8192",
#         model="llama3-8b-8192",
#         model="mixtral-8x7b-32768",
#     )


#     MCQs_output = chat_completion.choices[0].message.content

#     chat_completion2 = GroqClient.chat.completions.create(
#         messages=[
#             {
#                 'role': 'system',
#                 'content': """
#                     You are an assistant for create JSON format like:
#                         {   
#                             "question": "",
#                             "option_1": "",
#                             "option_2": "",
#                             "option_3": "",
#                             "option_4": "",
#                             "correct_answer": ""
#                             "Difficulty_Level":""
#                         }
#                         create List of this questions with JSON format.
#                     """
#             },
#             {
#                 'role': 'user',
#                 'content': MCQs_output
#             },
#         ],
#         model="llama3-70b-8192",
#     )

    

#     MCQs_JSON_output = chat_completion2.choices[0].message.content

#     start_index = MCQs_JSON_output.find('[')
#     end_index = MCQs_JSON_output.rfind(']') + 1
#     json_part = MCQs_JSON_output[start_index:end_index]
#     questions_dict = json.loads(json_part)
    
#     return questions_dict

from abc import ABC, abstractmethod
import json

class TextToMCQsStrategy(ABC):
    @abstractmethod
    def text_to_mcqs(self, description, context=None):
        pass




class TextToMCQsStrategyA(TextToMCQsStrategy):
    def text_to_mcqs(self, description, context=None):
        try:

            GroqClient = Groq( api_key="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")

            messages = get_messages(description, context)

            chat_completion = GroqClient.chat.completions.create(
                messages=messages,
                model="llama3-70b-8192"
            )

            MCQs_output = chat_completion.choices[0].message.content

            chat_completion2 = GroqClient.chat.completions.create(
                messages=[
                    {
                        'role': 'system',
                        'content': """
                            You are an assistant for creating JSON format like:
                                {   
                                    "question": "",
                                    "option_1": "",
                                    "option_2": "",
                                    "option_3": "",
                                    "option_4": "",
                                    "correct_answer": ""
                                    "Difficulty_Level":""
                                }
                                create List of these questions in JSON format.
                            """
                    },
                    {
                        'role': 'user',
                        'content': MCQs_output
                    },
                ],
                model="llama3-70b-8192"
            )

            MCQs_JSON_output = chat_completion2.choices[0].message.content

            start_index = MCQs_JSON_output.find('[')
            end_index = MCQs_JSON_output.rfind(']') + 1
            json_part = MCQs_JSON_output[start_index:end_index]
            questions_dict = json.loads(json_part)
            
            return questions_dict
        except Exception as e:
            return None


class TextToMCQsStrategyB(TextToMCQsStrategy):
    def text_to_mcqs(self, description, context=None):
        try:
            description_MCQs_client = OllamaClient(host='http://172.25.1.139:11434')

            messages = get_messages(description, context)

            response = description_MCQs_client.chat(
                model='llama3',
                messages=messages
            )

            MCQs_output = response['message']['content']
            response2 = description_MCQs_client.chat(
                model='llama3',
                messages=[
                    {
                        'role': 'system',
                        'content': """
                            You are an assistant for creating JSON format like:
                                {   
                                    "question": "",
                                    "option_1": "",
                                    "option_2": "",
                                    "option_3": "",
                                    "option_4": "",
                                    "correct_answer": ""
                                    "Difficulty_Level":""
                                }
                                create List of these questions in JSON format.
                            """
                    },
                    {
                        'role': 'user',
                        'content': MCQs_output
                    },
                ]
            )

            MCQs_JSON_output = response2['message']['content']

            start_index = MCQs_JSON_output.find('[')
            end_index = MCQs_JSON_output.rfind(']') + 1
            json_part = MCQs_JSON_output[start_index:end_index]
            questions_dict = json.loads(json_part)
            
            return questions_dict
        except Exception as e:
            return None

class TextToMCQsContext:
    def __init__(self, strategy_a, strategy_b):
        self.strategy_a = strategy_a
        self.strategy_b = strategy_b

    def text_to_mcqs(self, description, context=None):
        result = self.strategy_a.text_to_mcqs(description, context)
        if result is None:
            result = self.strategy_b.text_to_mcqs(description, context)
        return result
