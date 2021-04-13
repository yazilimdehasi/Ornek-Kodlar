from PIL import Image, ImageDraw, ImageFont
import os
import textwrap 
import math

def create_rounded_rectangle_mask(size, radius, alpha=255):
    factor = 5  # Factor to increase the image size that I can later antialiaze the corners
    radius = radius * factor
    image = Image.new('RGBA', (size[0] * factor, size[1] * factor), (0, 0, 0, 0))

    # create corner
    corner = Image.new('RGBA', (radius, radius), (0, 0, 0, 0))
    draw = ImageDraw.Draw(corner)
    # added the fill = .. you only drew a line, no fill
    draw.pieslice((0, 0, radius * 2, radius * 2), 180, 270, fill=(50, 50, 50, alpha + 55))

    # max_x, max_y
    mx, my = (size[0] * factor, size[1] * factor)

    # paste corner rotated as needed
    # use corners alpha channel as mask
    image.paste(corner, (0, 0), corner)
    image.paste(corner.rotate(90), (0, my - radius), corner.rotate(90))
    image.paste(corner.rotate(180), (mx - radius, my - radius), corner.rotate(180))
    image.paste(corner.rotate(270), (mx - radius, 0), corner.rotate(270))

    # draw both inner rects
    draw = ImageDraw.Draw(image)
    draw.rectangle([(radius, 0), (mx - radius, my)], fill=(50, 50, 50, alpha))
    draw.rectangle([(0, radius), (mx, my - radius)], fill=(50, 50, 50, alpha))
    image = image.resize(size, Image.ANTIALIAS)  # Smooth the corners

    return image

def get_text_dimensions(text_string, font):
    # https://stackoverflow.com/a/46220683/9263761
    ascent, descent = font.getmetrics()

    text_width = font.getmask(text_string).getbbox()[2]
    text_height = font.getmask(text_string).getbbox()[3] + descent

    return (text_width, text_height)

def generateSnapshot(name, username, tweet, time, date, outputName, savePath, commentCount, retweetCount, likeCount):
    userPhoto = "Images\\user_photo.png"
    contextPhoto = "Images\\context_image.jpg"
    fontName = ImageFont.truetype('Fonts/arial.ttf', 50)
    tweets = textwrap.wrap(tweet, width=34)
    tweet = ""
    lineCount = 0
    for twt in tweets:
        lineCount += 1
        tweet = tweet + "\n" + twt

    width, height = get_text_dimensions(twt, fontName)
    #332
    offset = math.ceil(((1920 - (500 + (height * lineCount) + 695 - 332)) / 2))

    background = Image.new('RGB', (1080, 1920), color = (21, 32, 43))
    
    user_photo = Image.open(userPhoto, 'r')
    user_photo = user_photo.resize((167,167), Image.ANTIALIAS)
    background.paste(user_photo, (108,offset), mask=user_photo)

    twitterIcon = Image.open('Images/twitter.png', 'r')
    twitterIcon = twitterIcon.resize((82,67), Image.ANTIALIAS)
    background.paste(twitterIcon, (890,offset+50), mask=twitterIcon)


    fontName = ImageFont.truetype('Fonts/HelveticaNeueBd.ttf', 43)
    nameText = ImageDraw.Draw(background)
    nameText.text((297,offset+18), name, font=fontName, fill=(255, 255, 255))

    fontName = ImageFont.truetype('Fonts/arial.ttf', 43)
    userNameText = ImageDraw.Draw(background)
    userNameText.text((297,offset+91), ("@"+username), font=fontName, fill=(200, 206, 212))

    
    tweetText = ImageDraw.Draw(background)
    
    tweetText.text((108,offset+143), tweet, font=fontName, fill=(255,255,255))
    

    contextImage = Image.open(contextPhoto, 'r')
    contextImage = contextImage.resize((864,576), Image.ANTIALIAS)
    background.paste(contextImage, (108,offset+168 + (height * lineCount) + 20), mask=create_rounded_rectangle_mask((864,576),20))


    fontName = ImageFont.truetype('Fonts/arial.ttf', 43)
    timeAndDateText = ImageDraw.Draw(background)
    timeAndDateText.text((108,offset+168 + (height * lineCount) + 600 + 20), (time + " • " + date), font=fontName, fill=(200, 206, 212))


    commentCountStr = ""
    retweetCountStr = ""
    likeCountStr = ""

    if(commentCount > 0):
        commentCountStr = str(commentCount)
    
    if(retweetCount > 0):
        retweetCountStr = str(retweetCount)

    if(likeCount > 0):
        likeCountStr = str(likeCount)

    commentIcon = Image.open('Images/comment.png', 'r')
    commentIcon = commentIcon.resize((51,51), Image.ANTIALIAS)
    background.paste(commentIcon, (122,offset+168 + (height * lineCount) + 700 + 20), mask=commentIcon)

    fontName = ImageFont.truetype('Fonts/arial.ttf', 43)
    commentCountText = ImageDraw.Draw(background)
    commentCountText.text((201,offset+168 + (height * lineCount) + 700 + 20), (commentCountStr), font=fontName, fill=(200, 206, 212))



    retweetIcon = Image.open('Images/retweet.png', 'r')
    retweetIcon = retweetIcon.resize((78,45), Image.ANTIALIAS)
    background.paste(retweetIcon, (372,offset+168 + (height * lineCount) + 700 + 20), mask=retweetIcon)

    fontName = ImageFont.truetype('Fonts/arial.ttf', 43)
    retweetCountText = ImageDraw.Draw(background)
    retweetCountText.text((474,offset+168 + (height * lineCount) + 700 + 20), (retweetCountStr), font=fontName, fill=(200, 206, 212))

    likeIcon = Image.open('Images/like.png', 'r')
    likeIcon = likeIcon.resize((61,54), Image.ANTIALIAS)
    background.paste(likeIcon, (645,offset+168 + (height * lineCount) + 700 + 20), mask=likeIcon)

    fontName = ImageFont.truetype('Fonts/arial.ttf', 43)
    likeCountText = ImageDraw.Draw(background)
    likeCountText.text((732,offset+168 + (height * lineCount) + 700 + 20), (likeCountStr), font=fontName, fill=(200, 206, 212))

    shareIcon = Image.open('Images/share.png', 'r')
    shareIcon = shareIcon.resize((54,60), Image.ANTIALIAS)
    background.paste(shareIcon, (904,offset+168 + (height * lineCount) + 695 + 20), mask=shareIcon)

    background.save(savePath + outputName + ".png")





