<br>

# **Challenge 1: Apache Nifi with local file and API**

## **First step**: Download the Apache Nifi from Docker Hub with a "docker pull" command

In the host CLI we execute the following command:

```bash
docker pull apache/nifi
```

Because a version is not specified in the command, the lastest will be downloaded in our local image repository. Once downloaded, we can execute the command:

```bash
docker images
```

and a detailed list of the available downloaded images will be displayed.

![img1](pics/pic2_1.png)

<br>

## **Second step**: Instantiate the apache/nifi image

In other words,

![img2](pics/pic2_2.png)

Abrimos en el puerto 8443 el Nifi, y adjudicamos una contraseña cualquiera a la sesion del usuario admin. Podemos comprobar con el comando docker ps que el contenedor está funcionando. Alternativamente, podemos verlo en Docker Desktop.

![img3](pics/pic2_3.png)

<br>

## **Tercer paso**: Copiamos el archivo que tenemos en el host en el contenedor en el cual estamos trabajando

Para poder hacer esta copia, primero de todo debemos saber en qué directorio estamos trabajando ejecutando un pwd en un prompt del contenedor. El directorio de trabajo en el contenedor es: **/opt/nifi/nifi-current**. Aquí, crearemos las carpetas input_files y output_files con el comando mkdir para diferenciar cuáles son los archivos input y output.
Una vez creados los directorios, copiaremos el archivo netflix.csv desde el host hasta el contenedor con el siguiente comando.

![img4](pics/pic2_6.png)
![img5](pics/pic2_5.png)

<br>

## **Cuarto paso**: Empezamos a crear el pipeline con la ingesta del csv

Escribimos el nombre del directorio y el file que queremos que coja.
![img6](pics/pic2_8.png)

Posteriormente le adjudicamos al flowfile un schema que se llamará _netflix_.
![img7](pics/pic2_9.png)

<br>

## **Quinto paso**: Filtramos los records deseados mediante una query SQL

Con el processor QueryRecord filtramos las peliculas aptas para mayores de 14, o dicho de otra manera las que no pueden ver menores de 14. Con la query:

> SELECT \* FROM FlowFile WHERE type LIKE '%Movie%' AND rating NOT IN ('TV-MA', 'NC-17','R')

poderemos filtrar las peliculas que no tengan los ratings:

- TV-MA: _"Mature Audience Only"_
- NC-17: _"No One under 17 and under Admitted"_
- R: _"Restricted"_

![img8](pics/pic2_10.png)

<br>

## **Sexto paso**: Transformamos el csv a json definiendo su esquema

Con el processor ConvertRecord, leemos el csv y lo escribimos como un json. El CSVReader inferirá el esquema, tendrá como delimitador una coma (véase en el mismo documento), e incluye los headers.

![img9](pics/pic2_18.png)

Por su parte, el JsonRecordSetWriter cogerá el schema que definamos en un registro de esquema Avro.

![img10](pics/pic2_20.png)

En la definición de esquema, debemos utilizar el mismo nombre de esquema que hemos utilizado en el UpdateAttribute del principio donde hemos definido su nombre. En este caso, lo hemos llamado _netflix_. Pasamos a definir todos sus campos como strings.

![img11](pics/pic2_16.png)

<br>

## **Séptimo paso**: Creamos el documento el el directorio output_files

Con el processor PutFile, configuramos el directorio donde queremos dejarlo.

![img12](pics/pic2_13.png)

<br>

## **Octavo paso**: Copiamos el archivo desde el contenedor hasta la carpeta host dónde estamos trabajando

De forma análoga a lo que hicimos para copiar el archivo netflix.csv desde el host hasta el contenedor, ahora copiamos el archivo resultante desde la carpeta output_files del contenedor hasta nuestro lugar de trabajo /RETO 3.

![img12](pics/pic2_17.png)
