from time import sleep

def carregar():
    print("À carregar",end="", flush=True)
    for n in range(3):
        sleep(0.5)
        print(".",end="", flush=True)
        sleep(0.75)
carregar()