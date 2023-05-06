# CS-411-A5-Team-5
Project for CS 411 A5 Team 5

### Contact Info

Richard Buehling, rbueh@bu.edu, +16308081663

Joshua Alvarez, jhsualva@bu,edu, +19173764766

Christopher Chan, chrisdc@bu.edu, +18457296611

## Project Overview and Description

Our project is a web app called sumitup that allows users to upload audio, have that audio transcribed, and summarized.

### Demo: https://youtu.be/GIyNk0tfpC0

### sumitup includes the following features:

- Sign in with Google
- Ability to upload, transcribe, and summarize audio (meetings, visits, videos, etc.)
- Search meeting transcriptions by keyword
- Administrative API allowing site owner to query all Users and their meeting data for processing
- Mobile friendly

### sumitup used the following systems and frameworks:

- Django as a web framework
- Tailwind CSS as a CSS framework
- Sqlite as a database
- all-auth Django plugin and Google Console for social logins
- Django Rest Framework for the API framework
- Assembly AI for meeting transcription
- OpenAI (ChatGPT) for meeting summarization

### API Json Example:

```
{
    {
        "email": "chris@gmail.com",
        "first_name": "chris",
        "id": 11,
        "meetings": [
            {
                "id": 26,
                "title": "I want IGUADALA",
                "audio": "/media/data/audio/i_want_iguadala_Fertk5Z.mp4",
                "audioid": "6kyy7dlxql-4bd8-46f5-8e7d-71b1dbbdce91",
                "transcription": "With the game on the line. One shot. Who would you rather have taking it? Iggy or curry of everyone on Golden State. Open shot. Fate of the universe on the line. Or the Martians have the death beam pointed at Earth? You better hit it. I want. Igua dolla. Igua Doll's got ice water in his veins. Igua Dollar is that type of player. High leverage moment. Fate of the universe on the line. I want an open shot, not go get it. I want Iguadala taking that shot for me. So you're not the shooter. Steph is. But I'm saying when it matters most, you're the dude I think doesn't care about that moment. Same guy like ice water in his veins. Your response? He crazy. Yeah.",
                "summary": "The speaker is discussing which player they would rather have taking a game-winning shot: Iguadala or Curry of the Golden State Warriors. They state that Iguadala has \"ice water in his veins\" and is the type",
                "created": "2023-05-05T22:19:36.963365Z",
                "supervisor": 11
            },
        ]
    }
````
