import requests as rq
import os

url = "https://gsom.spbu.ru/en/"
r = rq.get(url)

if r.status_code == 200:
    r_content = r.text #converting to string
    png_n = r_content.count('.png')
    print(f"Number of .png images: {png_n}")

    png_1_ind = r_content.find('.png') #index of first png

    if png_1_ind != -1: #this means we found the string
        link_start_ind = png_1_ind
        #now we need to find the start of the link by going back
        while link_start_ind > 0 and r_content[link_start_ind] not in ['"', "'"]:
            link_start_ind -= 1 #every iteration substacts one index point
        
        png_address = r_content[link_start_ind + 1:png_1_ind +4] # +1 to exclude " +4 to add all .png letters
        
        full_png_address = "https://gsom.spbu.ru"+png_address
        print(f"1st image address: {full_png_address}")
        image_request = rq.get(full_png_address)
        file = open(f'{os.getcwd()}/image.png', 'wb')
        file.write(image_request.content)
        file.close()
        print("Image fetched successfully, see image.png")
    else:
        ('No .png found')
else:
    print('Failed to fetch data')
        