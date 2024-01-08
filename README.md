# Financial_industry_transaction_Project
## Introduction
This project is aimed at testing my knowledge on Dictionaries,JSon and CSV files.The JSON file consists of two types of events: card events and user events. These are
terminologies used in the fintech industry to describe transactions conducted by users and
carried out with their payment cards.

## Definition of terms
- Card Event:
A card event is any transaction associated with a payment card, such as making a purchase,
withdrawing cash from an ATM, or reporting a lost or stolen card. An event is triggered
whenever a transaction occurs with a payment card.
- User Event:
User event refers to any engagement that the user performs on the fintech system. It is a way to
track and understand user behaviors and interactions within the financial security system. These
activities could include logging in, changing account settings, or initiating a financial transaction.
A user event is triggered whenever any activity is carried out on the fintech system by the user.

## Description of the Data
The data is stored in JSON file format, with each entry containing two keys: payload and
metadata.
- Payload refers to the actual data being transmitted and provides details about the
user and the card event, including information such as id, user id, address, job, name, and user
score, among other details.
Each recorded event also contains metadata, which is data that provides information about a
particular event. 
- The metadata includes details about the type of event recorded, the time the
event was recorded, and a unique identifier for that event.
We have decided to include the metadata as a part of our data, as it could help provide context
and categorize the type of event.
