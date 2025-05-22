"""
Proyecto final: Efecto de la terapia de Presión Negativa en Úlceras de Pie Diabético

Departamento de Ingeniería Eléctrica y Electrónica, Ingeniería Biomédica
Tecnológico Nacional de México [TecNM - Tijuana]
Blvd. Alberto Limón Padilla s/n, C.P. 22454, Tijuana, B.C., México

Nombre del alumno: Gonzalez Garcia Josselin
Número de control: C21210380
Correo institucional: l21210380@tectijuana.edu.mx

Asignatura: Modelado de Sistemas Fisiológicos
Docente: Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx
"""
# Instalar librerias en consola
#!pip install control
#!pip install slycot

# Librerías 
import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# Configuración del tiempo
x0, t0, tend, dt = 0, 0, 20, 1E-3
N = round((tend - t0) / dt) + 1
t = np.linspace(t0, tend, N)

# Entradas: escalón y pulso
u_step = np.where(t >= 0, 1.0, 0.0)
u_pulse = np.where((t >= 0) & (t <= 2), 1.0, 0.0)

# Parámetros: Herida leve (control) y severa (caso)
Re_leve, Rt_leve = 5E3, 2E3
Ce_leve, Ct_leve = 10E-6, 50E-6
Re_severa, Rt_severa = 20E3, 15E3
Ce_severa, Ct_severa = 100E-6, 220E-6

# Función de transferencia para terapia
def sys_TPN(Re, Ce, Rt, Ct):
    a2 = Re * Rt * Ce * Ct
    a1 = Ct * Re + Ct * Rt + Ce * Re
    a0 = 1
    return ctrl.tf([1], [a2, a1, a0])

sysL = sys_TPN(Re_leve, Ce_leve, Rt_leve, Ct_leve)
sysS = sys_TPN(Re_severa, Ce_severa, Rt_severa, Ct_severa)

# Parámetros del PID
Cr = 1E-6
kP = 721.1926
kI = 271.4443
kD = 425.7384
Re = 1 / (kI * Cr)
Rr = kP * Re
Ce = kD / Rr

# Controlador PID
def tratamiento(Cr, Re, Rr, Ce, sysE):
    numPID = [Re * Rr * Ce * Cr, Re * Ce + Rr * Cr, 1]
    denPID = [Re * Cr, 0]
    PID = ctrl.tf(numPID, denPID)
    return ctrl.feedback(ctrl.series(PID, sysE), 1, sign=-1)

sysPID = tratamiento(Cr, Re, Rr, Ce, sysS)

# --- Gráfica 1: Entrada escalón ---
_, Vs_step = ctrl.forced_response(sysL, t, u_step, x0)
_, Ve_step = ctrl.forced_response(sysS, t, u_step, x0)
_, pid_step = ctrl.forced_response(sysPID, t, Vs_step, x0)

plt.figure()
plt.plot(t, Vs_step, '-', color=[0.1, 0.3, 0.9], label='$P_A(t): Control$')
plt.plot(t, Ve_step, '-', color=[0.3, 0.8, 0.8], label='$P_A(t): Caso$')
plt.plot(t, pid_step, ':', linewidth=3, color=[0.9, 0.7, 0.9], label='$VPID(t): Tratamiento$')
plt.title("Respuesta a Entrada Escalón")
plt.xlabel('$t$ [s]')
plt.ylabel('$V(t)$ [V]')
plt.grid(True)
plt.xlim(0, 20)
plt.ylim(-0.2, 1.2)
plt.legend(bbox_to_anchor=(0.5, -0.25), loc='center', ncol=3, fontsize=8, frameon=False)
plt.tight_layout()

# --- Gráfica 2: Entrada pulso ---
_, Vs_pulse = ctrl.forced_response(sysL, t, u_pulse, x0)
_, Ve_pulse = ctrl.forced_response(sysS, t, u_pulse, x0)
_, pid_pulse = ctrl.forced_response(sysPID, t, Vs_pulse, x0)

plt.figure()
plt.plot(t, Vs_pulse, '-', color=[0.1, 0.3, 0.9], label='$P_A(t): Control$')
plt.plot(t, Ve_pulse, '-', color=[0.3, 0.8, 0.8], label='$P_A(t): Caso$')
plt.plot(t, pid_pulse, ':', linewidth=3, color=[0.9, 0.7, 0.9], label='$VPID(t): Tratamiento$')
plt.title("Respuesta a Entrada Pulso")
plt.xlabel('$t$ [s]')
plt.ylabel('$V(t)$ [V]')
plt.grid(True)
plt.xlim(0, 20)
plt.ylim(-0.2, 1.2)
plt.legend(bbox_to_anchor=(0.5, -0.25), loc='center', ncol=3, fontsize=8, frameon=False)
plt.tight_layout()

# Mostrar ambas figuras
plt.show()