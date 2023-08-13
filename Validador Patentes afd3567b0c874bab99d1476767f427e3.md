# Validador Patentes

La latente o matricula vehicular tambien conocidas como Placa Patente Unica (PPU) es un mecanismo de identificacion para vehiculos en el estado de chile, el sistema actual de tipo ABXXXX es utilizado desde 1985 y consta de dos formatos.  

## Formatos de patentes.

****Formato AA·10-00 (1985-2007)****

consiste en dos letras unidas con dos numeros y esta unido a otro par de numeros con un guion. Solo las siguientes letras son permitidas : A, B, C, E, F, G, H, D, K, L, N, P, R, S, T, U, V, X, Y, Z, W y M.

Esta combinación permitía un parque automotriz de 5.289.999 vehículos.

### Reglas

- Patentes que inician en ‘O’ pueden solo ser diplomaticas.
- No existen patentes con letra I.
- La I Solo puede ser usada en DI
- La J Inicial Solo para registro de remolques.
- Los numeros inician desde el 1000 hasta el 9999.

![Untitled](Validador%20Patentes%20afd3567b0c874bab99d1476767f427e3/Untitled.png)

---

### Formato actual.

Contiene las siguientes letras: B, C, D, F, G, H, J, K, L, P, R, S, T, V, W, X, Y y Z. La letra A fue eliminada por su parecido con el 4, la N con la Ñ, 0 con el 0  y la Q, la I con la J.

### Reglas

- Los valores numericos van desde el 10 hasta el 00.
- Complir con  la lista de letras permitidas.

## Ejemplo:

```jsx
validar_patente('WNTR99') # Retornara True or False, True si comple con las reglas
False de caso contrario.
```

## Para futuro.

- [ ]  Agregar implementacion en JavaScript.
- [ ]  Implementar en Java.
- [ ]  Implementar en Rust.
- [ ]  Diferenciar Patente de Carabinero y Ejercito.