import matplotlib.pyplot as plt

# четрый цвет фона

plt.style.use('dark_background')




fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.grid(True, which='both')
ax.set_ylim(0, 20)
ax.set_xlim(0, 20)



plt.rcParams.update({'figure.figsize': (5, 5)})


fig, ax = plt.subplots()
ax.plot(ag, label='ag')
ax.plot(pb, label='pb')
ax.plot(au, label='au')
ax.legend()
ax.set_xlabel('Этап')
ax.set_ylabel('Средняя концентрация по этапу')
