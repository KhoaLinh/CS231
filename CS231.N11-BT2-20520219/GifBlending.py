import cv2
import imageio
# đọc ảnh foreground
fg = cv2.imread('KLnen.jpg', cv2.IMREAD_UNCHANGED)
fg = cv2.cvtColor(fg, cv2.COLOR_BGR2RGBA)
mask = cv2.imread('KLnen-removebg.png', cv2.IMREAD_UNCHANGED)

url = "https://media.giphy.com/media/eNXAPFG7bRm1Dn149B/giphy.gif"
frames = imageio.mimread(imageio.core.urlopen(url).read(), '.gif')

h, w, c = fg.shape
frames = [cv2.resize(frame, (w, h)) for frame in frames]

nums = len(frames)
alpha = 1
for i in range(nums):
    frames[i][mask[:, :, 3] != 0] = fg[mask[:, :, 3] != 0] * alpha \
        + frames[i][mask[:, :, 3] != 0] * (1 - alpha)
    if i < nums/2:
        alpha -= 0.009
    else:
        alpha += 0.009

imageio.mimsave('result.gif', frames, 'GIF', duration=0.1)
