# Ejemplo de uso de Flask en Python

## Levantar el proyecto

1. Establece las variables de entorno.
    - Renombra .env.template como .env
    - Da valores para EMAIL_USER y EMAIL_TOKEN (el token lo obtienes de tu proveedor de correo electrónico.)

2. Crea la imagen de Docker:
    ```
    docker build --force-rm -t FlaskApp/latest . --no-cache
    ```

3. Crea el contenedor Docker:
    ```
    docker compose up -d 
    ```

4. Prueba desde el navegador:
    ```
    localhost:5010
    ```

## End-points de prueba:

    GET localhost:5010/lista -> muestra una lista de frutas.
    GET localhost:5010/numeros -> muestra una lista de números indicando cuales son pares y cuales impares.
    GET localhost:5010/web -> Prueba del servidor.
    GET localhost:5010/web/usuario/<nombre>/<apellido> -> Muestra 'Hola <nombre> <apellido>'.
    GET localhost:5010/web/edad/<edad> -> Muestra 'Tienes <edad> años'.
    GET localhost:5010/web/contacto -> Muestra un formulario de datos de contacto.
    POST localhost:5010/web/contacto (Se ejecuta al enviar el formuilario) -> 'Mensaje enviado'.
    GET localhost:5010/web/sumar -> Muestra un formulario que pide dos números.
    POST localhost:5010/web/sumas (Se ejecuta al enviar el formulario) -> Muestra el resultado de la suma en la parte inferior del formulario.
    GET localhost:5010/email -> Muestra un formulario para enviar correo electrónico. Imprescindible tener las variables de entorno bien configuradas.
    PORT localhost:5010/email (Se ejecuta al enviar el formulario) -> Muestra 'Correo enviado'  y envía el correo.


