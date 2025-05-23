# MSF-ProyectoFinal 
# Efecto de la terapia de Presión Negativa en Pie Diabético

Objetivo
Desarrollar un modelo matemático y diseñar un controlador para la terapia de presión negativa aplicada a úlceras de pie diabético, con el fin de regular dinámicamente la extracción del exudado y la estimulación del tejido. Se busca analizar la respuesta tisular ante diferentes niveles de presión negativa.

Descripción del efecto
La terapia de presión negativa (TPN) es una estrategia avanzada para el tratamiento de úlceras en pie diabético, basada en la aplicación de presión subatmosférica controlada sobre la herida. Este mecanismo favorece la eliminación de exudado, estimula la formación de tejido de granulación y mejora la perfusión sanguínea en el área afectada.

Modelado del sistema fisiológico
El comportamiento del tejido durante la terapia se modela mediante un circuito eléctrico de dos mallas:

1. Malla de aplicación de presión:
Incluye una fuente de voltaje variable Pao(t) que representa la presión negativa generada por el equipo de TPN.
Contiene un resistor Re, que simula la resistencia de la esponja porosa al paso del fluido.
Q(t) representa el flujo inicial de exudado a través de la esponja.

3. Malla de respuesta del tejido:
Formada por un capacitor Ce en paralelo con un arreglo en serie de un resistor Rt y un capacitor Ct.
Ce indica la capacidad de la esponja para almacenar temporalmente el exudado.
Rt representa la resistencia del tejido a la absorción del fluido.
Ct Modela la capacidad del tejido para acumular líquidos con el tiempo, como en casos de inflamación.

5. Flujos del sistema
Q(t) flujo inicial de exudado a través de la esponja.
QA(t) Flujo arterial
Q(t) - QA(t) Diferencia entre el flujo volumétrico total y el flujo arterial 
