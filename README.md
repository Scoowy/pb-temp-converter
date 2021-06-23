# Taller Nro. 1 - Módulos y Paquetes

## Integrantes

- Juan José Gahona Cañar - @Scoowy
- David Alejandro Paredes Sinchiri - @davidalejo
  
## Descripción

Paquete que permite la conversión de temperaturas.

### Funciones

Dentro del modulo `converters` se encuentran las siguientes funciones:

- `F_to_K` función que convierte temperaturas en Fahrenheit a Kelvin.
- `C_to_R` función que convierte temperaturas en Celsius a Rankine.
- `C_to_F` función que convierte temperaturas en Celsius a Fahrenheit.

## Modo de uso

```python
from pb_temp_converter.converters import F_to_K

fahrenheit_degrees = 32
kelvin_degrees = F_to_K(fahrenheit_degrees)
```

## Changelog

### version 0.1.0

- Funciones `F_to_K`, `C_to_R` y `C_to_F` añadidas.
- Pruebas unitarias escritas.
- Documentación inicial.