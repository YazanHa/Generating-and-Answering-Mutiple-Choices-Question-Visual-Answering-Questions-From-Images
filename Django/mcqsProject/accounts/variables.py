# mcqsApp/messages.py


# def get_messages(description):

#     return [
#         {
#             'role': 'user',
#             'content': "The image depicts a female tennis player in the midst of serving. She is dressed in a light blue tennis dress with yellow trim, and her attire includes a matching yellow visor. The player's right arm is extended upwards, reaching towards a yellow tennis ball that is positioned above her head, indicating the serve motion. Her left arm is bent at the elbow, providing balance. She wears white tennis shoes with blue accents, and her posture suggests a powerful serve. The court surface is green with white boundary lines, and the shadow of the player is cast on the ground, suggesting outdoor play under sunlight. There are no other players or objects in the immediate vicinity, focusing the action solely on the serving player."
#         },
#         {
#             'role': 'assistant',
#             'content': """
#                 **Easy (1-5)**

#                 1. What color is the tennis dress?
#                 a) Yellow
#                 b) Light blue
#                 c) Green
#                 d) White

#                 Answer: b) Light blue

#                 Difficulty_Level: Easy

#                 2. Which arm is extended upwards during the serve motion?
#                 a) Left arm
#                 b) Right arm
#                 c) Both arms
#                 d) No arm is extended

#                 Answer: b) Right arm

#                 Difficulty_Level: Easy

#                 3. What color are the tennis shoes?
#                 a) Yellow
#                 b) White
#                 c) Blue
#                 d) Green

#                 Answer: b) White

#                 Difficulty_Level: Easy

#                 4. Where is the player serving?
#                 a) Indoor court
#                 b) Outdoor court under sunlight
#                 c) Nighttime court
#                 d) Court with other players

#                 Answer: b) Outdoor court under sunlight

#                 Difficulty_Level: Easy

#                 5. What color are the boundary lines on the court surface?
#                 a) Yellow
#                 b) White
#                 c) Blue
#                 d) Green

#                 Answer: b) White

#                 Difficulty_Level: Easy

#                 **Medium (6-10)**

#                 6. What is the player's left arm doing during the serve motion?
#                 a) Extended upwards
#                 b) Bent at the elbow
#                 c) Holding onto something
#                 d) Not visible

#                 Answer: b) Bent at the elbow

#                 Difficulty_Level: Medium

#                 7. What color are the trim and visor of the tennis dress?
#                 a) Green
#                 b) Blue
#                 c) Yellow
#                 d) White

#                 Answer: c) Yellow

#                 Difficulty_Level: Medium

#                 8. Is there anyone or anything else on the court surface besides the serving player?
#                 a) Yes, another player is present.
#                 b) No, only the serving player is present.
#                 c) Yes, an object is present.
#                 d) No, nothing else is visible.

#                 Answer: b) No, only the serving player is present.

#                 Difficulty_Level: Medium

#                 9. What does the posture of the player suggest?
#                 a) A weak serve
#                 b) A powerful serve
#                 c) A slow serve
#                 d) A fast serve

#                 Answer: b) A powerful serve

#                 Difficulty_Level: Medium

#                 10. What color is the tennis ball?
#                 a) Green
#                 b) Yellow
#                 c) Blue
#                 d) White

#                 Answer: b) Yellow

#                 Difficulty_Level: Medium

#                 **Hard (11-15)**

#                 11. What is the purpose of the player's left arm being bent at the elbow?
#                 a) To add power to the serve
#                 b) To provide balance during the serve motion
#                 c) To distract the opponent
#                 d) To adjust her stance

#                 Answer: b) To provide balance during the serve motion

#                 Difficulty_Level: Hard

#                 12. What is the significance of the player's shadow on the ground?
#                 a) It indicates a strong serve
#                 b) It shows where the ball will land
#                 c) It suggests outdoor play under sunlight
#                 d) It represents the player's focus

#                 Answer: c) It suggests outdoor play under sunlight

#                 Difficulty_Level: Hard

#                 13. What can be inferred about the court surface based on the text?
#                 a) It is an indoor court with artificial turf
#                 b) It is an outdoor court with a natural grass surface
#                 c) It is a clay court
#                 d) It is a hard court

#                 Answer: b) It is an outdoor court with a natural grass surface

#                 Difficulty_Level: Hard

#                 14. What does the text suggest about the lighting conditions during the serve?
#                 a) It is nighttime or indoors
#                 b) It is daytime or outdoors under sunlight
#                 c) It is cloudy or overcast
#                 d) It is a mixture of both daytime and night

#                 Answer: b) It is daytime or outdoors under sunlight

#                 Difficulty_Level: Hard

#                 15. What is the primary focus of the image?
#                 a) The tennis ball in mid-air
#                 b) The player's facial expression
#                 c) The serving motion itself
#                 d) The court surface and boundaries

#                 Answer: c) The serving motion itself

#                 Difficulty_Level: Hard

#                 **Very Hard (16-20)**

#                 16. What can be inferred about the player's technique during the serve?
#                 a) She is using a forehand grip
#                 b) She is using a backhand grip
#                 c) She is using an overhead toss
#                 d) She is relying on her strength alone

#                 Answer: c) She is using an overhead toss (implied by the text)

#                 Difficulty_Level: Very Hard

#                 17. What does the text suggest about the player's dominance during the serve?
#                 a) It implies she is a weak server
#                 b) It implies she is a strong server
#                 c) It implies she is average in her serving skills
#                 d) It doesn't provide any information about her serving ability

#                 Answer: b) It implies she is a strong server

#                 Difficulty_Level: Very Hard

#                 18. What can be inferred about the player's movement during the serve?
#                 a) She is stationary and relying on arm strength
#                 b) She is moving forward to generate power
#                 c) She is staying back and using her legs for propulsion
#                 d) She is jumping or leaping to add height to her serve

#                 Answer: a) She is stationary and relying on arm strength (implied by the text)

#                 Difficulty_Level: Very Hard

#                 19. What does the text suggest about the player's mental state during the serve?
#                 a) It implies she is anxious or nervous
#                 b) It implies she is focused and confident
#                 c) It implies she is distracted or unfocused
#                 d) It doesn't provide any information about her mental state

#                 Answer: b) It implies she is focused and confident

#                 Difficulty_Level: Very Hard

#                 20. What can be inferred about the court environment during the serve?
#                 a) It is a crowded stadium with many spectators
#                 b) It is an empty court with no one present
#                 c) It is a small, intimate setting with a few fans
#                 d) It is an outdoor setting with natural surroundings

#                 Answer: d) It is an outdoor setting with natural surroundings (implied by the text)
#             """
#         },
#         {
#             'role': 'user',
#             'content': f"Generate as many multiple choice questions as possible using the selected text, and set the difficulty level for each question. Text:{description}"
#         },
#     ]

def get_messages(description, context=None):
    messages = [
        {
            'role': 'user',
            'content': "The image depicts a female tennis player in the midst of serving. She is dressed in a light blue tennis dress with yellow trim, and her attire includes a matching yellow visor. The player's right arm is extended upwards, reaching towards a yellow tennis ball that is positioned above her head, indicating the serve motion. Her left arm is bent at the elbow, providing balance. She wears white tennis shoes with blue accents, and her posture suggests a powerful serve. The court surface is green with white boundary lines, and the shadow of the player is cast on the ground, suggesting outdoor play under sunlight. There are no other players or objects in the immediate vicinity, focusing the action solely on the serving player."
        },
        {
            'role': 'assistant',
            'content': """
                **Easy (1-5)**

                1. What color is the tennis dress?
                a) Yellow
                b) Light blue
                c) Green
                d) White

                Answer: b) Light blue

                Difficulty_Level: Easy

                2. Which arm is extended upwards during the serve motion?
                a) Left arm
                b) Right arm
                c) Both arms
                d) No arm is extended

                Answer: b) Right arm

                Difficulty_Level: Easy

                3. What color are the tennis shoes?
                a) Yellow
                b) White
                c) Blue
                d) Green

                Answer: b) White

                Difficulty_Level: Easy

                4. Where is the player serving?
                a) Indoor court
                b) Outdoor court under sunlight
                c) Nighttime court
                d) Court with other players

                Answer: b) Outdoor court under sunlight

                Difficulty_Level: Easy

                5. What color are the boundary lines on the court surface?
                a) Yellow
                b) White
                c) Blue
                d) Green

                Answer: b) White

                Difficulty_Level: Easy

                **Medium (6-10)**

                6. What is the player's left arm doing during the serve motion?
                a) Extended upwards
                b) Bent at the elbow
                c) Holding onto something
                d) Not visible

                Answer: b) Bent at the elbow

                Difficulty_Level: Medium

                7. What color are the trim and visor of the tennis dress?
                a) Green
                b) Blue
                c) Yellow
                d) White

                Answer: c) Yellow

                Difficulty_Level: Medium

                8. Is there anyone or anything else on the court surface besides the serving player?
                a) Yes, another player is present.
                b) No, only the serving player is present.
                c) Yes, an object is present.
                d) No, nothing else is visible.

                Answer: b) No, only the serving player is present.

                Difficulty_Level: Medium

                9. What does the posture of the player suggest?
                a) A weak serve
                b) A powerful serve
                c) A slow serve
                d) A fast serve

                Answer: b) A powerful serve

                Difficulty_Level: Medium

                10. What color is the tennis ball?
                a) Green
                b) Yellow
                c) Blue
                d) White

                Answer: b) Yellow

                Difficulty_Level: Medium

                **Hard (11-15)**

                11. What is the purpose of the player's left arm being bent at the elbow?
                a) To add power to the serve
                b) To provide balance during the serve motion
                c) To distract the opponent
                d) To adjust her stance

                Answer: b) To provide balance during the serve motion

                Difficulty_Level: Hard

                12. What is the significance of the player's shadow on the ground?
                a) It indicates a strong serve
                b) It shows where the ball will land
                c) It suggests outdoor play under sunlight
                d) It represents the player's focus

                Answer: c) It suggests outdoor play under sunlight

                Difficulty_Level: Hard

                13. What can be inferred about the court surface based on the text?
                a) It is an indoor court with artificial turf
                b) It is an outdoor court with a natural grass surface
                c) It is a clay court
                d) It is a hard court

                Answer: b) It is an outdoor court with a natural grass surface

                Difficulty_Level: Hard

                14. What does the text suggest about the lighting conditions during the serve?
                a) It is nighttime or indoors
                b) It is daytime or outdoors under sunlight
                c) It is cloudy or overcast
                d) It is a mixture of both daytime and night

                Answer: b) It is daytime or outdoors under sunlight

                Difficulty_Level: Hard

                15. What is the primary focus of the image?
                a) The tennis ball in mid-air
                b) The player's facial expression
                c) The serving motion itself
                d) The court surface and boundaries

                Answer: c) The serving motion itself

                Difficulty_Level: Hard

                **Very Hard (16-20)**

                16. What can be inferred about the player's technique during the serve?
                a) She is using a forehand grip
                b) She is using a backhand grip
                c) She is using an overhead toss
                d) She is relying on her strength alone

                Answer: c) She is using an overhead toss (implied by the text)

                Difficulty_Level: Very Hard

                17. What does the text suggest about the player's dominance during the serve?
                a) It implies she is a weak server
                b) It implies she is a strong server
                c) It implies she is average in her serving skills
                d) It doesn't provide any information about her serving ability

                Answer: b) It implies she is a strong server

                Difficulty_Level: Very Hard

                18. What can be inferred about the player's movement during the serve?
                a) She is stationary and relying on arm strength
                b) She is moving forward to generate power
                c) She is staying back and using her legs for propulsion
                d) She is jumping or leaping to add height to her serve

                Answer: a) She is stationary and relying on arm strength (implied by the text)

                Difficulty_Level: Very Hard

                19. What does the text suggest about the player's mental state during the serve?
                a) It implies she is anxious or nervous
                b) It implies she is focused and confident
                c) It implies she is distracted or unfocused
                d) It doesn't provide any information about her mental state

                Answer: b) It implies she is focused and confident

                Difficulty_Level: Very Hard

                20. What can be inferred about the court environment during the serve?
                a) It is a crowded stadium with many spectators
                b) It is an empty court with no one present
                c) It is a small, intimate setting with a few fans
                d) It is an outdoor setting with natural surroundings

                Answer: d) It is an outdoor setting with natural surroundings (implied by the text)
            """
        }
    ]

    if context:
        print("yesssssss")
        messages.append(
            {
                'role': 'user',
                'content': f"Generate as many multiple choice questions as possible using the selected text and the additional context provided, and set the difficulty level for each question. Text: {description} Context: {context}"
            }
        )
    else:
        print("noooooo")
        messages.append(
            {
                'role': 'user',
                'content': f"Generate as many multiple choice questions as possible using the selected text, and set the difficulty level for each question. Text: {description}"
            }
        )

    return messages

def get_full_prompt():
    return """
                Describe the image with specific details, focusing on the following key elements:
                1. Identifiable Objects:
                    - List and describe all objects in the image, including their attributes such as size, shape, and color.
                2. Positions and Relationships:
                    - Specify the positions of objects relative to each other and describe spatial relationships and interactions.
                3. Colors and Textures:
                    - Note the colors of objects and any notable textures or patterns.
                4. Actions and Movements:
                    - Describe any actions being performed and details about any motion.
                5. Expressions and Emotions:
                    - For people or animals, describe facial expressions or emotional states.
                6. Context and Setting:
                    - Provide details about the setting or environment and the overall scene context.
                7. Clothing and Accessories:
                    - Describe what the people in the image are wearing, including specific items and colors.
                8. Lighting and Atmosphere:
                    - Note the lighting conditions, their effect on the scene, and describe the general atmosphere or mood.

                - Avoid using subjective language or broad descriptions. Include enough detail to allow someone to form precise questions about the image.
                """

def get_prompt():
    return """Describe the image with specific details, focusing on identifiable objects, their positions, colors, and actions. Avoid using subjective language or broad descriptions. Include enough detail to allow someone to form precise questions about the image."""


