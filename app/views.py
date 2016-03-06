from flask import Flask, request, send_from_directory, send_file
from PIL import Image, ImageDraw, ImageFont
from app import app


@app.route('/is', methods=['GET'])
def overlay():
    ''' Takes incoming query string parameters and returns built image
    '''
    # Collect user_id and group
    user_id = request.args.get('i')
    group = request.args.get('g')
    
    # Open base image
    im = Image.open('app/scaled.png')

    # Create overlay image with Alpha channel
    back = Image.new('RGBA', (im.width, im.height), (255, 0, 0, 0))

    # Create Draw class
    draw = ImageDraw.Draw(back)

    # Set up fonts
    font_header = ImageFont.truetype("app/OpenSans-Regular.ttf", 20)
    font = ImageFont.truetype("app/OpenSans-Regular.ttf", 16)

    # Draw alpha overlay line
    draw.line((0, 0) + (im.width, 0), fill=(128, 128, 128, 170), width=120)

    # Draw text onto overlay
    draw.text((20, 10), "Member ID:", (255, 255, 255), font=font_header)
    draw.text((20, 34), user_id, (255, 255, 255), font=font)
    draw.text((450, 10), "Group:", (255, 255, 255), font=font_header)
    draw.text((450, 34), group, (255, 255, 255), font=font)

    # Merge images, overlay on top
    im.paste(back, mask=back)
    im.save('app/img2.png')

    # Return final
    return send_file('img2.png', mimetype='image/png')


''' Example URL to return an image '''
''' 
Query String URL
http://localhost:5000/?i=some%20name&g=some%20group%20id


'''
