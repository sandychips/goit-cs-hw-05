import requests
import re
from collections import defaultdict
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor
import argparse

def fetch_text(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def map_words(text):
    words = re.findall(r'\w+', text.lower())
    return [(word, 1) for word in words]

def reduce_word_counts(pairs):
    word_counts = defaultdict(int)
    for word, count in pairs:
        word_counts[word] += count
    return word_counts

def visualize_top_words(word_counts, top_n=10):
    top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:top_n]
    words, counts = zip(*top_words)
    plt.bar(words, counts)
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title('Top Words by Frequency')
    plt.show()

def main():
    parser = argparse.ArgumentParser(description="Analyze word frequency from a URL text using MapReduce.")
    parser.add_argument('url', type=str, help="URL of the text to analyze.")
    args = parser.parse_args()

    text = fetch_text(args.url)
    with ThreadPoolExecutor() as executor:
        mapped = list(executor.map(map_words, [text]))[0]
    word_counts = reduce_word_counts(mapped)
    visualize_top_words(word_counts)

if __name__ == "__main__":
    main()
