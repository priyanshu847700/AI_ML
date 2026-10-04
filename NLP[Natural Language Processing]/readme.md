# What is NLP
- NLP (Natural Language Processing) is a part of Artificial Intelligence that helps computers understand, read, write, and talk like humans.
- In short, NLP allows machines to process human language jaise ki English, Hindi, etc. instead of Os and 1s.

- You type "Weather in Delhi" in Google. Google understands your text and shows you the correct answer. That's NLP:
- You say, "Hey Alexa, play Arijit Singh songs" Alexa listens, understands your sentence, and plays the music. That's NLP working behind the scene

- Again just for the sake of your machine to understand the language we use NLP. And this language is different from the computer languages like python, Java, C etc.
This is real language Hindi, English, french etc.

- Humans talk in languages like Hindi, English, Tamil.
But computers only understand numbers (0 and 1).
To bridge this gap, we need NLP so that computers can read and understand our language.

# Real world Applications -

1. Chatbots & Virtual Assistants
- Examples: ChatGPT, Alexa, Siri, Google Assistant
- NLP allows these tools to understand what you're saying or typing.
- They recognize your intent and give a relevant response.
- This involves speech recognition, text understanding, and response generation

2. Email Spam Filtering
- Example: Gmail Spam Detection
- NLP scans the content of emails for suspicious or spammy phrases like "You won a lottery!"
- It helps filter out spam and send important mails to the inbox.


3. Sentiment Analysis
- Examples: Twitter Analysis, Amazon Reviews, Customer Feedback
- Companies use NLP to detect whether people are feeling positive, negative, or neutral about their product.
- Very useful for brand monitoring and public opinion analysis.

- Now there are more and more applications in use the list goes on and on and the use is growing more and more.

# Approaches of NLP- 

1. Rule-Based Approach (Old School NLP)
- Early method of solving NLP using handwritten rules and grammar logic.
- You write rules manually to process and understand language.
- These rules can define grammar, spelling , corrections, sentence structure, etc.

## Limitation:
- Can't handle complex, ambiguous, or new patterns
- Not scalable for large data



2. Statistical (Machine Learning) Approach
- Language is treated like data, and algorithms learn patterns from it.

#  Use of models like:
- Naive Bayes
- Logistic Regression
- SVM (Support Vector Machines)

- Requires text to be converted into numbers using techniques like Bag of Words, TF-IDF, etc.

# Example: 
- Train a model on 10,000 product reviews. It learns which words indicate positive or negative sentiment and predicts for new reviews.
# Used for:
- Sentiment analysis
- Spam detection
- Text classification

# Sarcastic examples-
- - 1. Yeah, because staying up all night debugging is exactly what I dreamed of."
- ML Thinks: "dreamed", "exactly" → sounds like passion
- Reality: It's a painful dev life moment

- - 2. I love it when the internet stops working during a meeting."
- ML Thinks: "love", "meeting" → positive
- Reality: Sarcastic rage

# Limitation:
- Loses context of words (like sarcasm or sequence of words)

3. Deep Learning-Based Approach (Modern NLP) -
- Uses neural networks to automatically learn complex patterns and context from text.
- Models can understand meaning, context, word order, and more.
# Popular architectures:
- - RNN (Recurrent Neural Networks)
- - LSTM (Long Short-Term Memory)
- - GRU (Gated Recurrent Units)
- - Transformers (BERT, GPT, T5, etc.)

- Even in deep learning, we have to convert text into numbers but we don't use traditional techniques like Bag of Words or TF-IDF. Instead, we use more advanced methods like Word Embeddings (Word2Vec, GloVe) or Token IDs with Embedding Layers, which actually capture the meaning and context of words.

- Now since we haven't learned Deep Learning yet, in this video we'll focus on how NLP works with traditional Machine Learning using techniques like Bag of Words and TF-IDF. Once we complete Deep Learning, we'll dive into advanced embedding techniques like Word2Vec and BERT, and build more powerful models using those.


# Pipeline- let's see nlp pipeline!

## Step (1) - Gathering the text or say getting the data.

1) You can use the pre build public data set for this.
2) you can do Web Scraping (When Data is Not Available Ready-Made)
3) APls (Structured + Legal Way to Get Liv data)
4) Manual Collection / Crowdsourcing
5) Use NLP Tools to Auto-Generate Data (text Augmentation)
 
## Step (2) - Text Cleaning.

- Now there are many things we do in Text cleaning and depending on the task, Let's see some examples.
- - 1. lowercase      -> convert all text to lowercase!


- - 2. Remove Punctuation
Now there are many things we do in Text cleaning and depending on the task, Let's see some examples.

- - 3. Remove Numbers 
Remove digits from the text (optional — depends on task).
"I bought 5 phones" → you may or may not need the number.

- - 4. Remove URLs / Links
Remove any links in the text (very common in social media data)

- - 5. Remove HTML Tags
If scraping from web, remove things like <div>, <p>, etc.

- - 6. Remove Emojis & Special Characters
Emojis might break vectorization if not removed or handled

- - 7. Remove Stopwords
Remove common words like "is", "the", "was", "and", "in", etc.
These don't help in understanding the meaning.

- - 8. (Optional) Spelling Correction
Fix spelling mistakes using TextBlob or other libraries


# Removing stopwords

- doing all the other tasks are easy but for removing the stop words like 'is', 'the', 'are' etc we have to use a library and that is NLTK.
- BTW you can use spacy aswell

- Now there is your data with messages and that is known as the CORPUS 

# Corpus
- A collection of texts. Think of it like a dataset of text.
- Example: A folder of 10,000 tweets is your cornus
- You can say:
    "Text is one message. Corpus is the whole colletion


# Sentence
- " A group of words that forms a meaningful statement.
- Example: "This is a spam message."
- In NLP, some tools split long text into sentences before breaking them into words

# Token
- Each individual word or symbol in the text is called a token.
- Example: "I love NLP" → Tokens = ["I", "love", "NLP" ]
- The process of splitting text into tokens i called Tokenization

