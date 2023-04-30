import requests
import os
import json


# Define the API URL
url_template = "https://bible-api.com/{book}{chapter}:{verse}"

# Define the list of books of the Bible
books_of_bible=["genesis", "exodus", "leviticus", "numbers", "deuteronomy", "joshua", "judges", "ruth", "1samuel", "2samuel", "1kings", "2kings", "1chronicles", "2chronicles", "ezra", "nehemiah", "esther", "job", "psalms", "proverbs", "ecclesiastes", "songofsolomon", "isaiah", "jeremiah", "lamentations", "ezekiel", "daniel", "hosea", "joel", "amos", "obadiah", "jonah", "micah", "nahum", "habakkuk", "zephaniah", "haggai", "zechariah", "malachi", "matthew", "mark", "luke", "john", "acts", "romans", "1corinthians", "2corinthians", "galatians", "ephesians", "philippians", "colossians", "1thessalonians", "2thessalonians", "1timothy", "2timothy", "titus", "philemon", "hebrews", "james", "1peter", "2peter", "1john", "2john", "3john", "jude", "revelation"]

# The image that will be used as a background for the text
image_url = 'https://i.pinimg.com/originals/7d/ea/9c/7dea9c3521b8209b1d90779d4e62dc43.jpg' 


def create_payload(image_url, text):

    payload = {
        "image_url": image_url,   # url for the background image.
        "text": text,             # text to be placed on the image.
        "text_color": 'ffffffff', # Hex color codes to be overlay on the background
        "text_size": 32,          # Possible values : 8, 10, 12, 14, 16, 32, 64, 128
        "margin": 200,            # margin for where the text will placed
        "y_align": 'top',         # vertical alignment. Allowed values are: top, middle, bottom
        "x_align": 'center'       # horizontal alignment. Allowed values are: left, right, center
    }
    encoded_params = "&".join([f"{key}={value}" for key, value in payload.items()])

    # https://textoverimage.moesif.com/#documentation
    base_url = 'https://textoverimage.moesif.com/image?'
    return f"{base_url}{encoded_params}"


def download_image(book, verses, chapter):
    # Create the 'book' directory if it doesn't exist
    if verses != []:
        if not os.path.exists(book + '\\' + str(chapter)):
            os.makedirs(book + '\\' + book + str(chapter))
    else:
        return
    
    count = 1
    photo_text = [""]
    length = 0
    for verse in verses:
        if length + len(verse) <= 500: # Number of charaters that will be used per photo (+/- one verse)
            photo_text[-1] += str(verses.index(verse) + 1) + '. ' + verse.replace('\n', ' ')
            length += len(verse)
        else:
            photo_text.append(str(verses.index(verse) + 1) + '. ' + verse.replace('\n', ' '))
            length = len(verse)
    
    for text in photo_text:
        filename = os.path.join(book + '\\' + book + str(chapter), str(count)+'.jpg')
        count += 1
        
        # Make a GET request to the URL and save the content to the file
        text = text.replace('”', '"').replace('“', '"')
        url = create_payload(image_url, text.replace(" ","%20"))
        response = requests.get(url)
        if response.ok:
            photo_text = ''
            with open(filename, 'wb') as f:
                f.write(response.content)
    
        print(f"Image downloaded to {filename}")


def get_verses(book):
    # Create an empty list to store the verses
    verses = []
    
    # Loop through all the verses in the chapter, starting from verse 1
    for chapter_index in range(1, 9999999): # 9999999 used as an upper limit it will break once the index is bigger that the biggest chapter in the book
        # Construct the URL for the current chapter
        url = url_template.format(book=book, chapter=chapter_index, verse=1)
        response = requests.get(url)
        
        # Check if the chapter exists
        if response.ok:
            # Loop through all the verses in the chapter
            for verse_index in range(1, 9999999): # Same as line 72
                url = url_template.format(book=book, chapter=chapter_index, verse=verse_index)
                response = requests.get(url)
                if response.ok:
                    verse_data = response.json()
                    verses.append(verse_data['text'])
                else:
                    # If the response is not ok, it means there are no more verses in this chapter
                    # Download the images for the verses in this chapter and move on to the next chapter
                    download_image(book, verses, chapter_index)
                    # Clear the verses list for the next chapter
                    verses = []
                    break
        else:
            # If the response is not ok, it means there are no more chapters in this book
            break


if __name__ == '__main__':
    
    # Loop throw all the books
    for book in books_of_bible:
        get_verses(book)

    # get_verses('revelation') => call for just one book
    
