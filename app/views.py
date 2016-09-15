from flask import Flask, request, send_from_directory, send_file
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from app import app
import random
import colorsys

DEG30 = 30/360.
def adjacent_colors((r, g, b), d=DEG30): # Assumption: r, g, b in [0, 255]
    r, g, b = map(lambda x: x/255., [r, g, b]) # Convert to [0, 1]
    h, l, s = colorsys.rgb_to_hls(r, g, b)     # RGB -> HLS
    h = [(h+d) % 1 for d in (-d, d * 2, d * 2, d * 2, d * 2)] # Rotation by d
    # h = [(h+d) % 1 for d in (-d * 5, d * 5)] # Rotation by d
    # h = [(h+d) % 1 for d in (-d, d, -d * 2, d * 2, -d * 3, d * 3)] # Rotation by d
    # multipliers = [1, 2, 3, 4, 5]
    # h = [(h+d) % 1 for d in ((-d * x, d * x) for x in multipliers]) # Rotation by d
    adjacent = [map(lambda x: int(round(x*255)), colorsys.hls_to_rgb(hi, l, s))
            for hi in h] # H'LS -> new RGB
    return adjacent


def rnd(max_val, min_val=None):
    min_val = min_val
    if min_val:
        pass
    else:
        min_val = 0
    return random.randrange(min_val, max_val, 5)

def img_rtn(w, h, colors):
    colors = [list(colors)]
    print colors

    # Generate new image
    temp_image = Image.new('RGBA', (w, h))

    r_w = rnd(w + h)
    r_h = rnd(h)
    colors += adjacent_colors(colors[0])
    random.shuffle(colors)

    colors.append(rnd(255))

    draw = ImageDraw.Draw(temp_image)
    draw.line(
        (r_w, 0 - 80) + (r_w - (h / 3), h + 80),
        fill=(
            colors[0][0],
            colors[0][1],
            colors[0][2],
            colors[0].pop()),
        width=rnd(270, min_val=130)
    )
    blurry = temp_image.filter(ImageFilter.GaussianBlur(radius=20))
    return blurry


@app.route('/if', methods=['GET'])
def fractal():
    ''' Takes incoming query string parameters and returns built image
    '''
    # Collect user_id and group
    user_id = 'default'
    group = 'default'
    user_id = request.args.get('i')
    group = request.args.get('g')

    # Open base image
    im = Image.open('app/scaled.png')

    # Create overlay image with Alpha channel
    over = Image.new('RGBA', (im.width, im.height), (255, 255, 255, 0))
    back = Image.new('RGBA', (im.width, im.height), (127, 127, 127, 255))

    # Set random colors or
    colors = [rnd(255), rnd(255), rnd(255)]
    # colors = (29, 189, 242)
    # colors = (255, 112, 10)
    # colors = (220, 245, 200)
    # colors = (55, 215, 30)
    colors = (150, 190, 135)
    # print 'colors: %s' % str(colors)

    for x in range(0, 10):
        temp_image = img_rtn(im.width, im.height, colors)
        back.paste(temp_image, mask=temp_image)

    # Create Draw class
    draw = ImageDraw.Draw(over)

    # Set up fonts
    font_header = ImageFont.truetype("app/OpenSans-Regular.ttf", 20)
    font = ImageFont.truetype("app/OpenSans-Regular.ttf", 16)

    # Draw alpha overlay line
    draw.line((0, 0) + (im.width, 0), fill=(30, 30, 30, 170), width=120)

    # Draw text onto overlay
    txt_clr = (255, 255, 255)
    draw.text((20, 10), "Member ID:", txt_clr, font=font_header)
    draw.text((20, 34), user_id, txt_clr, font=font)
    draw.text((450, 10), "Group:", txt_clr, font=font_header)
    draw.text((450, 34), group, txt_clr, font=font)

    # Merge images, overlay on top
    # im.paste(over, mask=over)
    back.paste(over, mask=over)
    back.save('app/img2.png')
    # im.save('app/img2.png')

    # Return final
    return send_file('img2.png', mimetype='image/png')


@app.route('/af', methods=['GET'])
def aber():
    ''' Takes incoming query string parameters and returns built image
    '''
    # Collect user_id and group
    user_id = request.args.get('i')
    group = request.args.get('g')

    # Open base image
    im = Image.open('app/aber.jpg')

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
    txt_clr = (255, 255, 255)
    draw.text((20, 10), "Member ID:", txt_clr, font=font_header)
    draw.text((20, 34), user_id, txt_clr, font=font)
    draw.text((450, 10), "Group:", txt_clr, font=font_header)
    draw.text((450, 34), group, txt_clr, font=font)

    # Merge images, overlay on top
    im.paste(back, mask=back)
    im.save('app/img2.png')

    # Return final
    return send_file('img2.png', mimetype='image/png')


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
    txt_clr = (255, 255, 255)
    draw.text((20, 10), "Member ID:", txt_clr, font=font_header)
    draw.text((20, 34), user_id, txt_clr, font=font)
    draw.text((450, 10), "Group:", txt_clr, font=font_header)
    draw.text((450, 34), group, txt_clr, font=font)

    # Merge images, overlay on top
    im.paste(back, mask=back)
    im.save('app/img2.png')

    # Return final
    return send_file('img2.png', mimetype='image/png')


@app.route('/g', methods=['GET'])
def grain():
    ''' Takes incoming query string parameters and returns built image
    '''
    # Collect user_id and group
    user_id = request.args.get('i')
    group = request.args.get('g')

    # Open base image
    im = Image.open('app/dark.png')

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
    txt_clr = (255, 255, 255)
    draw.text((20, 10), "Member ID:", txt_clr, font=font_header)
    draw.text((20, 34), user_id, txt_clr, font=font)
    draw.text((450, 10), "Group:", txt_clr, font=font_header)
    draw.text((450, 34), group, txt_clr, font=font)

    # Merge images, overlay on top
    im.paste(back, mask=back)
    im.save('app/img2.png')

    # Return final
    return send_file('img2.png', mimetype='image/png')


@app.route('/sb', methods=['GET'])
def smell_bad():
    ''' Takes incoming query string parameters and returns built image
    '''
    # Collect user_id and group
    user_id = request.args.get('i')
    group = request.args.get('g')

    # Open base image
    im = Image.open('app/smellbad.png')

    # Create overlay image with Alpha channel
    back = Image.new('RGBA', (im.width, im.height), (255, 0, 0, 0))

    # Create Draw class
    draw = ImageDraw.Draw(back)

    # Set up fonts
    font_header = ImageFont.truetype("app/OpenSans-Regular.ttf", 20)
    font = ImageFont.truetype("app/OpenSans-Regular.ttf", 16)

    # Draw alpha overlay line
    draw.line(
        (0, im.height) + (im.width, im.height),
        fill=(108, 108, 108, 170),
        width=120
    )

    # Draw text onto overlay
    txt_clr = (255, 255, 255)
    draw.text((20, im.height - 56), "Member ID:", txt_clr, font=font_header)
    draw.text((20, im.height - 32), user_id, txt_clr, font=font)
    draw.text((450, im.height - 56), "Group:", txt_clr, font=font_header)
    draw.text((450, im.height - 32), group, txt_clr, font=font)

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
