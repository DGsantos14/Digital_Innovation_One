from threading import Thread
import  time



def carro(velocidade,piloto):
    trajeto = 0
    while trajeto <= 100:
        print('Carro: ',piloto, trajeto)
        trajeto+=velocidade
        time.sleep(0.5)
        print('Piloto: {} km: {} \n'.format(piloto, trajeto))



t_carro_1 = Thread(target=carro, args=[1, 'Bruno'])
t_carro_2 = Thread(target=carro, args=[2, 'João'])


t_carro_1.start()
t_carro_2.start()