import platform, pygame

pygame.init()

if platform.system() == "Windows":
    pygame.mixer.init()
    willhelm = pygame.mixer.Sound("assets\willhelm.wav")
    mlem = pygame.mixer.Sound("assets\mlem.wav")
    win = pygame.mixer.Sound("assets\win.wav")
else:
    pygame.mixer.init()
    willhelm = pygame.mixer.Sound("assets/willhelm.wav")
    mlem = pygame.mixer.Sound("assets/mlem.wav")
    win = pygame.mixer.Sound("assets/win.wav")
