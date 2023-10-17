import pygame as pg

white = (255, 255, 255)

def main():
  screen = pg.display.set_mode((400, 300))
  screen.fill(white)
  clock = pg.time.Clock()

  while True:
    pg.display.flip()

    clock.tick(60)
  
if __name__ == "__main__":
  main()
