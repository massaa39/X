import openai
import os

# 環境変数からOpenAI APIキーを取得する
openai.api_key = os.getenv("OPENAI_API_KEY")

def make_tweet():
    prompt = """
    Create a tweet in the style of @satetu4401. The tweet should be insightful, critical, and use the same kind of language and themes as @satetu4401's tweets. Here is an example of a topic you can use:
    "AIと労働市場の変化"
    """
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=280,
            temperature=0.7
        )
        return response.choices[0]['message']['content']
    except openai.OpenAIError as e:
        print(f"OpenAI Error: {e}")
        return None

# テスト用の関数呼び出し
if __name__ == "__main__":
    tweet = make_tweet()
    print(f"Generated Tweet: {tweet}")
