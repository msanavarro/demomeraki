**API Registro al webhook para alarma Equipo Fijo DEMO ISAT Meraki**
----
Registro a las notificaciones del webhook que funciona como alarma de equipo fijo. Consultarlo con el la documentación de la llamada en **API_EquipoFijo** para más información.


* **/v1/report/webhookregistry**


* **Method:**

  `[POST, DELETE]`


*  **URL Params**

   **Required [POST]:**

    * `clientUrl:(str)`

  **Required [DELETE]:**

    * `clientUrl:(str)`

   **Optional:**

   `NA`

* **Data Params**

   `NA`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:**

      `NA`

* **Error Response:**

  * **Code:** 4xx Bad Request <br />
    * **Content:** `{ errorid: 400 , error : "Error de parametros" }`
    **Content:** `{ errorid: 401 , error : "Registro repetido" }`
    **Content:** `{ errorid: 402 , error : "Registro no esta en base de datos" }`
 <br/>

  OR

  * **Code:** 403 Forbidden <br />
    **Content:** `{ error : "credenciales erroneas" }`

  OR

  * **Code:** 404 Not Found <br />
    **Content:** `{ error : "el recurso que esta buscando no esta disponible" }`

  OR

  * **Code:** 500 server error <br />
    **Content:** `{ error : "error en servidor" }`

  OR

  * **Code:** 501 not implemented <br />
    **Content:** `{ error : "el servidor no tiene un metodo para atender esta solicitud" }`


* **Sample Call[POST]:** `curl -L -X POST 'htttps://url:port/v1/report/registro_wh' -H 'Content-Type: application/json' --data-raw '{
    '\''url'\'': '\''https://cliente:port/ejemplo/abc'\'',
    '\''metodo'\'': '\''POST'\''
}'`

* **Sample Call[DELETE]:** `curl -L -X DELETE 'htttps://url:port/v1/report/registro_wh' -H 'Content-Type: application/json' --data-raw '{
    '\''url'\'': '\''https://cliente:port/ejemplo/abc'\'',
}'`

* **Notes:**
Para más información respecto al funcionamiento del callback, ver la documentación de la llamada **API_EquipoFijo**
