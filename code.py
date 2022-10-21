# Load packages
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

# Upload your data as a .txt file and load it as a data frame 
text = open('data.txt', 
            mode='r', 
            encoding='utf-8') \
            .read().replace('\n','')
text[:1000]

# change the value to black
def black_color_func(word, font_size, position,orientation,random_state=None, **kwargs):
    return("hsl(0,100%, 1%)")

wc = WordCloud(background_color="white",           # select background color
               width=3000,                         # set wight
               height=2000,                        # set height
               max_words=500).generate(text)       # set max amount of words

wc.recolor(color_func = black_color_func)          # set the word color to black
plt.figure(figsize=[15,10])                        # set the figsize
plt.imshow(wc, interpolation="bilinear")           # plot the wordcloud
plt.axis("off")                                    # remove plot axes
plt.savefig('wordcloud.png')                       # save as png
plt.show()